"""
Oracle Layer Verification Module
================================

Classes for handling verification, confidence scoring, and reasoning traces.
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum
import hashlib
import json


class VerificationStatus(Enum):
    """Status of a verification check."""
    VERIFIED = "verified"
    UNVERIFIED = "unverified"
    REQUIRES_REVIEW = "requires_review"
    FAILED = "failed"


class TrinityRole(Enum):
    """Roles in Trinity cross-validation."""
    ADVOCATE = "advocate"
    SKEPTIC = "skeptic"
    ARBITER = "arbiter"


@dataclass
class ConfidenceScore:
    """
    Represents a confidence score with uncertainty bounds.
    
    Attributes:
        value: Point estimate (0.0-1.0)
        epistemic_uncertainty: Reducible uncertainty from limited data
        aleatoric_uncertainty: Irreducible uncertainty from domain variability
    """
    value: float
    epistemic_uncertainty: float = 0.0
    aleatoric_uncertainty: float = 0.0
    
    def __post_init__(self):
        if not 0.0 <= self.value <= 1.0:
            raise ValueError("Confidence value must be between 0.0 and 1.0")
    
    @property
    def total_uncertainty(self) -> float:
        """Combined uncertainty (root sum of squares)."""
        return (self.epistemic_uncertainty**2 + self.aleatoric_uncertainty**2) ** 0.5
    
    @property
    def lower_bound(self) -> float:
        """Conservative lower bound of confidence."""
        return max(0.0, self.value - self.total_uncertainty)
    
    @property
    def upper_bound(self) -> float:
        """Upper bound of confidence."""
        return min(1.0, self.value + self.total_uncertainty)
    
    def meets_threshold(self, threshold: float, conservative: bool = True) -> bool:
        """Check if confidence meets threshold."""
        check_value = self.lower_bound if conservative else self.value
        return check_value >= threshold
    
    def to_string(self) -> str:
        """Format as string with uncertainty."""
        if self.total_uncertainty > 0:
            return f"{self.value:.2f} ±{self.total_uncertainty:.2f}"
        return f"{self.value:.2f}"
    
    def __str__(self) -> str:
        return self.to_string()


@dataclass
class ReasoningStep:
    """A single step in a reasoning trace."""
    step_number: int
    input_data: str
    analysis: str
    conclusion: str
    confidence: ConfidenceScore
    uncertainty_sources: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "step": self.step_number,
            "input": self.input_data,
            "analysis": self.analysis,
            "conclusion": self.conclusion,
            "confidence": self.confidence.to_string(),
            "uncertainty_sources": self.uncertainty_sources
        }


@dataclass
class ReasoningTrace:
    """
    Complete reasoning trace showing decision process.
    
    Implements the REASONING_TRACE_PROTOCOL from Oracle Layer spec.
    """
    steps: List[ReasoningStep] = field(default_factory=list)
    final_conclusion: Optional[str] = None
    combined_confidence: Optional[ConfidenceScore] = None
    caveats: List[str] = field(default_factory=list)
    
    def add_step(self, input_data: str, analysis: str, conclusion: str,
                 confidence: float, uncertainty: float = 0.0,
                 uncertainty_sources: List[str] = None) -> ReasoningStep:
        """Add a reasoning step."""
        step = ReasoningStep(
            step_number=len(self.steps) + 1,
            input_data=input_data,
            analysis=analysis,
            conclusion=conclusion,
            confidence=ConfidenceScore(confidence, uncertainty),
            uncertainty_sources=uncertainty_sources or []
        )
        self.steps.append(step)
        return step
    
    def synthesize(self, conclusion: str, caveats: List[str] = None) -> None:
        """Synthesize final conclusion from steps."""
        self.final_conclusion = conclusion
        self.caveats = caveats or []
        
        if self.steps:
            avg_confidence = sum(s.confidence.value for s in self.steps) / len(self.steps)
            max_uncertainty = max(s.confidence.total_uncertainty for s in self.steps)
            self.combined_confidence = ConfidenceScore(avg_confidence, max_uncertainty)
    
    def to_prompt_format(self) -> str:
        """Format as Oracle Layer prompt output."""
        lines = []
        for step in self.steps:
            lines.append(f"[REASONING_STEP_{step.step_number}]")
            lines.append(f"├─ INPUT: {step.input_data}")
            lines.append(f"├─ ANALYSIS: {step.analysis}")
            lines.append(f"├─ CONCLUSION: {step.conclusion}")
            lines.append(f"├─ CONFIDENCE: {step.confidence}")
            if step.uncertainty_sources:
                lines.append(f"└─ UNCERTAINTY: {', '.join(step.uncertainty_sources)}")
            lines.append("")
        
        if self.final_conclusion:
            lines.append("[FINAL_SYNTHESIS]")
            lines.append(f"├─ CONCLUSION: {self.final_conclusion}")
            if self.combined_confidence:
                lines.append(f"├─ CONFIDENCE: {self.combined_confidence}")
            if self.caveats:
                lines.append(f"└─ CAVEATS: {'; '.join(self.caveats)}")
        
        return "\n".join(lines)


@dataclass
class TrinityPerspective:
    """One perspective in Trinity cross-validation."""
    role: TrinityRole
    evidence: List[str]
    confidence: ConfidenceScore
    conclusion: str
    
    def to_prompt_format(self) -> str:
        """Format as Oracle Layer prompt output."""
        role_name = self.role.value.upper()
        lines = [f"[PERSPECTIVE: {role_name} ANALYSIS]"]
        lines.append(f"├─ Role: Build {'case FOR' if self.role == TrinityRole.ADVOCATE else 'case AGAINST' if self.role == TrinityRole.SKEPTIC else 'balanced judgment'}")
        lines.append(f"├─ Evidence: {'; '.join(self.evidence)}")
        lines.append(f"├─ Confidence: {self.confidence}")
        lines.append(f"└─ Conclusion: {self.conclusion}")
        return "\n".join(lines)


@dataclass
class TrinityVerification:
    """
    Trinity cross-validation: Advocate, Skeptic, Arbiter.
    
    Implements CROSS_VALIDATION_PROTOCOL from Oracle Layer spec.
    """
    claim: str
    advocate: Optional[TrinityPerspective] = None
    skeptic: Optional[TrinityPerspective] = None
    arbiter: Optional[TrinityPerspective] = None
    final_decision: Optional[str] = None
    
    def set_advocate(self, evidence: List[str], confidence: float, 
                     conclusion: str, uncertainty: float = 0.0) -> None:
        """Set advocate perspective."""
        self.advocate = TrinityPerspective(
            role=TrinityRole.ADVOCATE,
            evidence=evidence,
            confidence=ConfidenceScore(confidence, uncertainty),
            conclusion=conclusion
        )
    
    def set_skeptic(self, evidence: List[str], confidence: float,
                    conclusion: str, uncertainty: float = 0.0) -> None:
        """Set skeptic perspective."""
        self.skeptic = TrinityPerspective(
            role=TrinityRole.SKEPTIC,
            evidence=evidence,
            confidence=ConfidenceScore(confidence, uncertainty),
            conclusion=conclusion
        )
    
    def set_arbiter(self, evidence: List[str], confidence: float,
                    conclusion: str, decision: str, uncertainty: float = 0.0) -> None:
        """Set arbiter perspective and final decision."""
        self.arbiter = TrinityPerspective(
            role=TrinityRole.ARBITER,
            evidence=evidence,
            confidence=ConfidenceScore(confidence, uncertainty),
            conclusion=conclusion
        )
        self.final_decision = decision
    
    def to_prompt_format(self) -> str:
        """Format as Oracle Layer prompt output."""
        lines = [f"[TRINITY VERIFICATION]", f"CLAIM: \"{self.claim}\"", ""]
        
        if self.advocate:
            lines.append(self.advocate.to_prompt_format())
            lines.append("")
        if self.skeptic:
            lines.append(self.skeptic.to_prompt_format())
            lines.append("")
        if self.arbiter:
            lines.append(self.arbiter.to_prompt_format())
            lines.append("")
        
        if self.final_decision:
            lines.append(f"[TRINITY DECISION]: {self.final_decision}")
        
        return "\n".join(lines)


@dataclass 
class VerificationResult:
    """
    Result of verifying a claim or response.
    
    Implements the FORMAL_VERIFICATION_PROTOCOL from Oracle Layer spec.
    """
    claim: str
    status: VerificationStatus
    confidence: ConfidenceScore
    source: Optional[str] = None
    reasoning: Optional[ReasoningTrace] = None
    trinity: Optional[TrinityVerification] = None
    timestamp: datetime = field(default_factory=datetime.utcnow)
    hash: Optional[str] = None
    
    def __post_init__(self):
        if self.hash is None:
            self.hash = self._compute_hash()
    
    def _compute_hash(self) -> str:
        """Compute SHA-256 hash for chain-of-custody."""
        content = f"{self.claim}|{self.status.value}|{self.confidence.value}|{self.timestamp.isoformat()}"
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def to_prompt_format(self) -> str:
        """Format as Oracle Layer prompt output."""
        status_icon = "✅" if self.status == VerificationStatus.VERIFIED else "❌"
        lines = [
            f"[VERIFICATION RESULT]",
            f"├─ CLAIM: \"{self.claim}\"",
            f"├─ STATUS: {status_icon} {self.status.value.upper()}",
            f"├─ CONFIDENCE: {self.confidence}",
        ]
        if self.source:
            lines.append(f"├─ SOURCE: {self.source}")
        lines.append(f"└─ HASH: {self.hash}")
        return "\n".join(lines)


@dataclass
class ChainOfCustody:
    """
    Immutable audit trail of verification decisions.
    
    Implements CHAIN_OF_CUSTODY_VERIFICATION from Oracle Layer spec.
    """
    entries: List[VerificationResult] = field(default_factory=list)
    
    def add(self, result: VerificationResult) -> None:
        """Add a verification result to the chain."""
        self.entries.append(result)
    
    def verify_integrity(self) -> bool:
        """Verify no entries have been tampered with."""
        for entry in self.entries:
            if entry.hash != entry._compute_hash():
                return False
        return True
    
    def to_audit_report(self) -> str:
        """Generate audit report."""
        lines = [
            "=" * 60,
            "CHAIN OF CUSTODY AUDIT REPORT",
            f"Generated: {datetime.utcnow().isoformat()}",
            f"Total Entries: {len(self.entries)}",
            f"Integrity: {'VERIFIED' if self.verify_integrity() else 'COMPROMISED'}",
            "=" * 60,
            ""
        ]
        
        for i, entry in enumerate(self.entries):
            lines.append(f"Entry {i+1}:")
            lines.append(entry.to_prompt_format())
            lines.append("")
        
        return "\n".join(lines)
