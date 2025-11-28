"""
Oracle Layer Core
=================

Main OracleLayer class that provides the high-level API for using the engine.
"""

from typing import Optional, List, Dict, Any, Union
from dataclasses import dataclass, field
from datetime import datetime

from .config import OracleConfig, VerificationLevel
from .providers import AIProvider, AIResponse, ProviderFactory
from .prompts import PromptBuilder
from .verification import (
    VerificationResult, VerificationStatus, ConfidenceScore,
    ReasoningTrace, TrinityVerification, ChainOfCustody
)


@dataclass
class OracleResponse:
    """
    Response from Oracle Layer enhanced AI call.
    
    Attributes:
        content: The AI's response text
        raw_response: Original AIResponse from provider
        verification_markers: Extracted verification markers from response
        verify_required_count: Number of [VERIFY_REQUIRED] tags found
        confidence_scores: Extracted confidence scores
        passed_verification: Whether response meets Oracle standards
        reasoning_trace: Extracted reasoning (if enabled)
        chain_of_custody: Audit trail (if enabled)
        warnings: Any warnings generated during processing
    """
    content: str
    raw_response: AIResponse
    verification_markers: Dict[str, List[str]] = field(default_factory=dict)
    verify_required_count: int = 0
    confidence_scores: List[ConfidenceScore] = field(default_factory=list)
    passed_verification: bool = True
    reasoning_trace: Optional[ReasoningTrace] = None
    chain_of_custody: Optional[ChainOfCustody] = None
    warnings: List[str] = field(default_factory=list)
    processing_time_ms: float = 0.0
    
    def has_unverified_claims(self) -> bool:
        """Check if response contains unverified claims."""
        return self.verify_required_count > 0
    
    def get_sources(self) -> List[str]:
        """Get all cited sources from response."""
        return self.verification_markers.get("sources", [])
    
    def average_confidence(self) -> Optional[float]:
        """Calculate average confidence across all scores."""
        if not self.confidence_scores:
            return None
        return sum(s.value for s in self.confidence_scores) / len(self.confidence_scores)


class ResponseParser:
    """Parser for extracting Oracle Layer markers from AI responses."""
    
    @staticmethod
    def extract_markers(response_text: str) -> Dict[str, List[str]]:
        """Extract all Oracle Layer markers from response."""
        import re
        
        markers = {
            "sources": [],
            "verify_required": [],
            "confidence": [],
            "reasoning": [],
            "safety_flags": [],
            "holdings": [],
        }
        
        source_pattern = r'\[SOURCE:([^\]]+)\]'
        markers["sources"] = re.findall(source_pattern, response_text)
        
        verify_pattern = r'\[VERIFY_REQUIRED(?::([^\]]+))?\]'
        markers["verify_required"] = re.findall(verify_pattern, response_text)
        
        confidence_pattern = r'\[CONFIDENCE:([0-9.]+)(?:\s*±\s*([0-9.]+))?\]'
        markers["confidence"] = re.findall(confidence_pattern, response_text)
        
        safety_pattern = r'SAFETY FLAG:([^\n]+)'
        markers["safety_flags"] = re.findall(safety_pattern, response_text)
        
        holding_pattern = r'\[HOLDING\]:?\s*([^\n\[]+)'
        markers["holdings"] = re.findall(holding_pattern, response_text)
        
        return markers
    
    @staticmethod
    def extract_confidence_scores(markers: Dict[str, List[str]]) -> List[ConfidenceScore]:
        """Convert extracted confidence strings to ConfidenceScore objects."""
        scores = []
        for match in markers.get("confidence", []):
            if isinstance(match, tuple):
                value = float(match[0])
                uncertainty = float(match[1]) if match[1] else 0.0
            else:
                value = float(match)
                uncertainty = 0.0
            scores.append(ConfidenceScore(value, uncertainty))
        return scores
    
    @staticmethod
    def count_verify_required(markers: Dict[str, List[str]]) -> int:
        """Count VERIFY_REQUIRED markers."""
        return len(markers.get("verify_required", []))


class OracleLayer:
    """
    Oracle Layer v2.1 - Embedded Intelligence Protocol
    
    Makes ANY AI self-correct, self-explain, and self-document during execution.
    
    Usage:
        # Basic usage
        oracle = OracleLayer()
        response = oracle.query("What is the capital of France?")
        
        # With specific provider
        oracle = OracleLayer(provider=OpenAIProvider(model="gpt-4"))
        
        # With custom config
        oracle = OracleLayer(config=OracleConfig.medical())
        
        # Just get the prompt (for manual use)
        prompt = oracle.generate_system_prompt()
    
    Attributes:
        config: OracleConfig controlling behavior
        provider: AIProvider for making AI calls (optional)
        chain_of_custody: Running audit trail of verifications
    """
    
    VERSION = "2.1.0"
    CODENAME = "PROMETHEUS"
    
    def __init__(
        self,
        config: Optional[OracleConfig] = None,
        provider: Optional[AIProvider] = None,
        auto_detect_provider: bool = True
    ):
        """
        Initialize Oracle Layer.
        
        Args:
            config: Configuration for Oracle behavior (defaults to standard)
            provider: AI provider to use for queries
            auto_detect_provider: If True and no provider given, auto-detect
        """
        self.config = config or OracleConfig.standard()
        self.provider = provider
        
        if self.provider is None and auto_detect_provider:
            self.provider = ProviderFactory.auto_detect()
        
        self.chain_of_custody = ChainOfCustody() if self.config.enable_chain_of_custody else None
        self._system_prompt_cache: Optional[str] = None
    
    def generate_system_prompt(self, compact: bool = False) -> str:
        """
        Generate the Oracle Layer system prompt.
        
        This is the prompt that gets embedded with AI requests to enable
        self-correction, verification, and safety features.
        
        Args:
            compact: If True, generate token-efficient version
            
        Returns:
            Complete Oracle Layer system prompt
        """
        if compact:
            return PromptBuilder.build_compact_prompt(self.config)
        
        if self._system_prompt_cache is None:
            self._system_prompt_cache = PromptBuilder.build_system_prompt(self.config)
        
        return self._system_prompt_cache
    
    def query(
        self,
        prompt: str,
        additional_context: Optional[str] = None,
        temperature: float = 0.7,
        max_tokens: int = 4096,
        compact_mode: bool = False
    ) -> OracleResponse:
        """
        Send a query through Oracle Layer enhanced AI.
        
        Args:
            prompt: The user's question or request
            additional_context: Extra context to include
            temperature: AI creativity level (0.0-1.0)
            max_tokens: Maximum response length
            compact_mode: Use token-efficient prompt
            
        Returns:
            OracleResponse with enhanced verification metadata
            
        Raises:
            ValueError: If no provider is configured
        """
        if self.provider is None:
            raise ValueError(
                "No AI provider configured. Either:\n"
                "1. Pass a provider: OracleLayer(provider=OpenAIProvider())\n"
                "2. Set OPENAI_API_KEY or ANTHROPIC_API_KEY environment variable\n"
                "3. Use generate_system_prompt() to get the prompt for manual use"
            )
        
        import time
        start_time = time.time()
        
        system_prompt = self.generate_system_prompt(compact=compact_mode)
        
        full_prompt = prompt
        if additional_context:
            full_prompt = f"CONTEXT:\n{additional_context}\n\nQUERY:\n{prompt}"
        
        raw_response = self.provider.complete(
            prompt=full_prompt,
            system_prompt=system_prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        markers = ResponseParser.extract_markers(raw_response.content)
        confidence_scores = ResponseParser.extract_confidence_scores(markers)
        verify_required_count = ResponseParser.count_verify_required(markers)
        
        warnings = []
        passed = True
        
        if verify_required_count >= self.config.max_verify_required_tags:
            warnings.append(
                f"Response contains {verify_required_count} unverified claims "
                f"(threshold: {self.config.max_verify_required_tags})"
            )
            passed = False
        
        if confidence_scores:
            low_confidence = [s for s in confidence_scores 
                           if s.value < self.config.confidence_threshold]
            if low_confidence:
                warnings.append(
                    f"{len(low_confidence)} claims below confidence threshold "
                    f"({self.config.confidence_threshold})"
                )
        
        if markers.get("safety_flags"):
            warnings.append(f"Safety flags present: {len(markers['safety_flags'])}")
        
        processing_time = (time.time() - start_time) * 1000
        
        response = OracleResponse(
            content=raw_response.content,
            raw_response=raw_response,
            verification_markers=markers,
            verify_required_count=verify_required_count,
            confidence_scores=confidence_scores,
            passed_verification=passed,
            warnings=warnings,
            processing_time_ms=processing_time
        )
        
        if self.chain_of_custody:
            avg_conf = response.average_confidence() or 0.5
            result = VerificationResult(
                claim=prompt[:100],
                status=VerificationStatus.VERIFIED if passed else VerificationStatus.REQUIRES_REVIEW,
                confidence=ConfidenceScore(avg_conf),
                source=self.provider.name,
            )
            self.chain_of_custody.add(result)
            response.chain_of_custody = self.chain_of_custody
        
        return response
    
    def verify_claim(self, claim: str, context: Optional[str] = None) -> VerificationResult:
        """
        Verify a specific claim using Trinity verification.
        
        Args:
            claim: The claim to verify
            context: Optional context for the claim
            
        Returns:
            VerificationResult with detailed analysis
        """
        if self.provider is None:
            raise ValueError("No AI provider configured for verification")
        
        verification_prompt = f"""Apply Trinity Verification to this claim:

CLAIM: "{claim}"

{f'CONTEXT: {context}' if context else ''}

Analyze as:
1. ADVOCATE: Build the strongest case FOR this claim
2. SKEPTIC: Build the strongest case AGAINST this claim  
3. ARBITER: Synthesize and provide final judgment

Output your analysis with [CONFIDENCE:X.XX] scores for each perspective.
End with a clear [VERIFICATION_STATUS: VERIFIED/UNVERIFIED/UNCERTAIN]"""

        response = self.query(verification_prompt)
        
        if "VERIFIED" in response.content and "UNVERIFIED" not in response.content:
            status = VerificationStatus.VERIFIED
        elif "UNVERIFIED" in response.content:
            status = VerificationStatus.UNVERIFIED
        else:
            status = VerificationStatus.REQUIRES_REVIEW
        
        avg_conf = response.average_confidence() or 0.5
        
        return VerificationResult(
            claim=claim,
            status=status,
            confidence=ConfidenceScore(avg_conf),
            source=self.provider.name,
        )
    
    def analyze_with_reasoning(self, query: str) -> tuple[str, ReasoningTrace]:
        """
        Analyze a query with full reasoning trace.
        
        Args:
            query: The query to analyze
            
        Returns:
            Tuple of (response_content, reasoning_trace)
        """
        reasoning_prompt = f"""Analyze this query with explicit reasoning trace:

QUERY: {query}

For each step of your analysis, show:
[REASONING_STEP_N]
├─ INPUT: What information you're processing
├─ ANALYSIS: How you're evaluating it
├─ CONCLUSION: What you determined
├─ CONFIDENCE: [0.00-1.00]
└─ UNCERTAINTY: What reduces your confidence

End with:
[FINAL_SYNTHESIS]
├─ CONCLUSION: Your final answer
├─ CONFIDENCE: Overall confidence
└─ CAVEATS: Important qualifications"""

        response = self.query(reasoning_prompt)
        
        trace = ReasoningTrace()
        trace.add_step(
            input_data=query,
            analysis="Query processed through Oracle Layer",
            conclusion="See response content",
            confidence=response.average_confidence() or 0.7,
        )
        trace.synthesize(
            conclusion="Analysis complete",
            caveats=response.warnings if response.warnings else None
        )
        
        return response.content, trace
    
    def get_audit_report(self) -> Optional[str]:
        """Get chain-of-custody audit report if enabled."""
        if self.chain_of_custody:
            return self.chain_of_custody.to_audit_report()
        return None
    
    @classmethod
    def quick_check(cls, claim: str, provider: Optional[AIProvider] = None) -> bool:
        """
        Quick verification check for a single claim.
        
        Args:
            claim: The claim to check
            provider: AI provider (auto-detects if not provided)
            
        Returns:
            True if claim passes basic verification
        """
        oracle = cls(config=OracleConfig.minimal(), provider=provider)
        try:
            result = oracle.verify_claim(claim)
            return result.status == VerificationStatus.VERIFIED
        except Exception:
            return False
    
    def __repr__(self) -> str:
        provider_name = self.provider.name if self.provider else "None"
        return (
            f"OracleLayer(version={self.VERSION}, "
            f"provider={provider_name}, "
            f"verification={self.config.verification_level.value})"
        )
