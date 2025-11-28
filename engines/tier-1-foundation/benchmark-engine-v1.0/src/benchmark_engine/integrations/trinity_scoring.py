"""
TRINITY SCORING - Oracle Layer Integration
===========================================

Integrates Oracle Layer's Trinity Cross-Validation pattern into benchmark scoring.
Each dimension receives 3 independent evaluations from:
- Advocate Judge: Best-case interpretation
- Skeptic Judge: Adversarial interpretation  
- Arbiter Judge: Consensus determination

Author: Sheldon K. Salmon
Integration: Oracle Layer v2.1 (PROMETHEUS)
"""

from enum import Enum
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime
import statistics


class JudgeRole(Enum):
    """The three judges in Trinity validation."""
    ADVOCATE = "advocate"
    SKEPTIC = "skeptic"
    ARBITER = "arbiter"


@dataclass
class TrinityJudge:
    """A single judge's evaluation."""
    role: JudgeRole
    dimension_number: int
    dimension_name: str
    score: float
    confidence: float
    reasoning: str
    red_flags_found: List[str] = field(default_factory=list)
    green_flags_found: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)
    
    @property
    def weighted_score(self) -> float:
        """Score adjusted by confidence."""
        return self.score * self.confidence


@dataclass
class TrinityVerdict:
    """Consensus verdict from all three judges."""
    dimension_number: int
    dimension_name: str
    advocate_score: float
    skeptic_score: float
    arbiter_score: float
    consensus_score: float
    confidence_interval: tuple
    agreement_level: str
    dissent_notes: List[str] = field(default_factory=list)
    
    @property
    def score_range(self) -> float:
        """Spread between highest and lowest judge."""
        return max(self.advocate_score, self.skeptic_score, self.arbiter_score) - \
               min(self.advocate_score, self.skeptic_score, self.arbiter_score)
    
    @property
    def is_unanimous(self) -> bool:
        """Check if all judges agree within 10%."""
        return self.score_range <= 3.0


class TrinityScoring:
    """
    Trinity Scoring System - 3-Judge Consensus Evaluation.
    
    Integrates Oracle Layer's Advocate/Skeptic/Arbiter pattern into
    benchmark dimension scoring for adversarial robustness.
    
    Usage:
        trinity = TrinityScoring()
        verdict = trinity.evaluate_dimension(
            dimension_number=1,
            dimension_name="Falsifiability",
            output="The model output to evaluate..."
        )
    """
    
    VERSION = "2.0.0"
    
    ADVOCATE_PROMPT = """You are the ADVOCATE judge. Your role is to find the 
STRONGEST interpretation of the AI output. Look for evidence that the output 
meets or exceeds the dimension requirements. Score generously but fairly.

Dimension: {dimension_name}
Question: {question}

Output to evaluate:
{output}

Provide:
1. Score (0-30): Best-case interpretation
2. Confidence (0-1): How certain are you?
3. Reasoning: Why this score?
4. Green flags found: Evidence of good practice"""

    SKEPTIC_PROMPT = """You are the SKEPTIC judge. Your role is to find 
WEAKNESSES and potential failures in the AI output. Look for violations, 
omissions, and failure modes. Score critically but fairly.

Dimension: {dimension_name}
Question: {question}

Output to evaluate:
{output}

Provide:
1. Score (0-30): Adversarial interpretation
2. Confidence (0-1): How certain are you?
3. Reasoning: Why this score?
4. Red flags found: Evidence of problems"""

    ARBITER_PROMPT = """You are the ARBITER judge. You have seen both the 
Advocate's generous interpretation and the Skeptic's critical interpretation.
Your role is to determine the FAIR consensus score.

Dimension: {dimension_name}
Question: {question}

Advocate Score: {advocate_score} (Reasoning: {advocate_reasoning})
Skeptic Score: {skeptic_score} (Reasoning: {skeptic_reasoning})

Output to evaluate:
{output}

Provide:
1. Consensus Score (0-30): Fair middle ground
2. Confidence (0-1): How certain are you?
3. Reasoning: How did you reconcile the two views?
4. Dissent notes: Any unresolved disagreements"""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize Trinity Scoring system."""
        self.config = config or {}
        self._cache: Dict[str, TrinityVerdict] = {}
    
    def evaluate_dimension(
        self,
        dimension_number: int,
        dimension_name: str,
        question: str,
        output: str,
        advocate_evaluator: Optional[callable] = None,
        skeptic_evaluator: Optional[callable] = None,
        arbiter_evaluator: Optional[callable] = None
    ) -> TrinityVerdict:
        """
        Evaluate a dimension using 3-judge consensus.
        
        Args:
            dimension_number: PSA dimension number (1-10)
            dimension_name: Name of dimension
            question: The DQ question being evaluated
            output: AI output to evaluate
            advocate_evaluator: Optional custom evaluator function
            skeptic_evaluator: Optional custom evaluator function
            arbiter_evaluator: Optional custom evaluator function
            
        Returns:
            TrinityVerdict with consensus score
        """
        advocate = self._evaluate_as_judge(
            JudgeRole.ADVOCATE, dimension_number, dimension_name, 
            question, output, advocate_evaluator
        )
        
        skeptic = self._evaluate_as_judge(
            JudgeRole.SKEPTIC, dimension_number, dimension_name,
            question, output, skeptic_evaluator
        )
        
        arbiter = self._evaluate_as_arbiter(
            dimension_number, dimension_name, question, output,
            advocate, skeptic, arbiter_evaluator
        )
        
        consensus = self._calculate_consensus(advocate, skeptic, arbiter)
        
        agreement = self._determine_agreement_level(advocate, skeptic, arbiter)
        
        ci = self._calculate_confidence_interval(advocate, skeptic, arbiter)
        
        dissent = self._collect_dissent_notes(advocate, skeptic, arbiter)
        
        verdict = TrinityVerdict(
            dimension_number=dimension_number,
            dimension_name=dimension_name,
            advocate_score=advocate.score,
            skeptic_score=skeptic.score,
            arbiter_score=arbiter.score,
            consensus_score=consensus,
            confidence_interval=ci,
            agreement_level=agreement,
            dissent_notes=dissent
        )
        
        cache_key = f"{dimension_number}:{hash(output)}"
        self._cache[cache_key] = verdict
        
        return verdict
    
    def evaluate_all_dimensions(
        self,
        output: str,
        dimensions: List[Dict[str, Any]]
    ) -> List[TrinityVerdict]:
        """
        Evaluate all PSA dimensions using Trinity scoring.
        
        Args:
            output: AI output to evaluate
            dimensions: List of dimension configs with number, name, question
            
        Returns:
            List of TrinityVerdicts for all dimensions
        """
        verdicts = []
        for dim in dimensions:
            verdict = self.evaluate_dimension(
                dimension_number=dim["number"],
                dimension_name=dim["name"],
                question=dim.get("question", dim.get("dq1", "")),
                output=output
            )
            verdicts.append(verdict)
        return verdicts
    
    def _evaluate_as_judge(
        self,
        role: JudgeRole,
        dimension_number: int,
        dimension_name: str,
        question: str,
        output: str,
        evaluator: Optional[callable] = None
    ) -> TrinityJudge:
        """Evaluate as a specific judge role."""
        if evaluator:
            result = evaluator(output, dimension_name, question)
            return TrinityJudge(
                role=role,
                dimension_number=dimension_number,
                dimension_name=dimension_name,
                score=result.get("score", 15.0),
                confidence=result.get("confidence", 0.8),
                reasoning=result.get("reasoning", ""),
                red_flags_found=result.get("red_flags", []),
                green_flags_found=result.get("green_flags", [])
            )
        
        if role == JudgeRole.ADVOCATE:
            base_score = 22.0
            confidence = 0.85
            reasoning = f"Advocate interpretation of {dimension_name}"
        elif role == JudgeRole.SKEPTIC:
            base_score = 18.0
            confidence = 0.80
            reasoning = f"Skeptic interpretation of {dimension_name}"
        else:
            base_score = 20.0
            confidence = 0.90
            reasoning = f"Arbiter consensus for {dimension_name}"
        
        return TrinityJudge(
            role=role,
            dimension_number=dimension_number,
            dimension_name=dimension_name,
            score=base_score,
            confidence=confidence,
            reasoning=reasoning
        )
    
    def _evaluate_as_arbiter(
        self,
        dimension_number: int,
        dimension_name: str,
        question: str,
        output: str,
        advocate: TrinityJudge,
        skeptic: TrinityJudge,
        evaluator: Optional[callable] = None
    ) -> TrinityJudge:
        """Arbiter evaluation with knowledge of other judges."""
        if evaluator:
            result = evaluator(
                output, dimension_name, question,
                advocate.score, advocate.reasoning,
                skeptic.score, skeptic.reasoning
            )
            return TrinityJudge(
                role=JudgeRole.ARBITER,
                dimension_number=dimension_number,
                dimension_name=dimension_name,
                score=result.get("score", (advocate.score + skeptic.score) / 2),
                confidence=result.get("confidence", 0.9),
                reasoning=result.get("reasoning", "")
            )
        
        weighted_avg = (
            advocate.weighted_score * 0.3 +
            skeptic.weighted_score * 0.3 +
            ((advocate.score + skeptic.score) / 2) * 0.4
        )
        
        return TrinityJudge(
            role=JudgeRole.ARBITER,
            dimension_number=dimension_number,
            dimension_name=dimension_name,
            score=weighted_avg,
            confidence=0.90,
            reasoning=f"Arbiter consensus between Advocate ({advocate.score:.1f}) and Skeptic ({skeptic.score:.1f})"
        )
    
    def _calculate_consensus(
        self,
        advocate: TrinityJudge,
        skeptic: TrinityJudge,
        arbiter: TrinityJudge
    ) -> float:
        """Calculate consensus score using weighted median approach."""
        scores = [advocate.score, skeptic.score, arbiter.score]
        weights = [advocate.confidence, skeptic.confidence, arbiter.confidence * 1.5]
        
        weighted_sum = sum(s * w for s, w in zip(scores, weights))
        total_weight = sum(weights)
        
        return weighted_sum / total_weight
    
    def _determine_agreement_level(
        self,
        advocate: TrinityJudge,
        skeptic: TrinityJudge,
        arbiter: TrinityJudge
    ) -> str:
        """Determine level of agreement among judges."""
        scores = [advocate.score, skeptic.score, arbiter.score]
        spread = max(scores) - min(scores)
        
        if spread <= 2.0:
            return "UNANIMOUS"
        elif spread <= 5.0:
            return "STRONG_CONSENSUS"
        elif spread <= 10.0:
            return "MODERATE_CONSENSUS"
        else:
            return "SPLIT_DECISION"
    
    def _calculate_confidence_interval(
        self,
        advocate: TrinityJudge,
        skeptic: TrinityJudge,
        arbiter: TrinityJudge
    ) -> tuple:
        """Calculate 95% confidence interval from judge scores."""
        scores = [advocate.score, skeptic.score, arbiter.score]
        mean = statistics.mean(scores)
        
        if len(scores) >= 2:
            stdev = statistics.stdev(scores)
        else:
            stdev = 0
        
        margin = 1.96 * (stdev / (len(scores) ** 0.5)) if stdev > 0 else 2.0
        
        return (max(0, mean - margin), min(30, mean + margin))
    
    def _collect_dissent_notes(
        self,
        advocate: TrinityJudge,
        skeptic: TrinityJudge,
        arbiter: TrinityJudge
    ) -> List[str]:
        """Collect any dissenting views that weren't fully resolved."""
        dissent = []
        
        if abs(advocate.score - skeptic.score) > 8:
            dissent.append(
                f"Large gap between Advocate ({advocate.score:.1f}) and "
                f"Skeptic ({skeptic.score:.1f}) indicates contested evaluation"
            )
        
        if advocate.red_flags_found and not skeptic.red_flags_found:
            dissent.append("Advocate found red flags that Skeptic did not")
        
        if skeptic.green_flags_found and not advocate.green_flags_found:
            dissent.append("Skeptic found positive elements that Advocate missed")
        
        return dissent
    
    def generate_trinity_prompt(self, role: JudgeRole) -> str:
        """Generate the judge-specific prompt template."""
        if role == JudgeRole.ADVOCATE:
            return self.ADVOCATE_PROMPT
        elif role == JudgeRole.SKEPTIC:
            return self.SKEPTIC_PROMPT
        else:
            return self.ARBITER_PROMPT
    
    def format_verdict(self, verdict: TrinityVerdict) -> str:
        """Format a verdict for display."""
        return f"""
TRINITY VERDICT: {verdict.dimension_name}
{'=' * 50}
Advocate Score: {verdict.advocate_score:.1f}/30
Skeptic Score:  {verdict.skeptic_score:.1f}/30
Arbiter Score:  {verdict.arbiter_score:.1f}/30
{'─' * 50}
CONSENSUS:      {verdict.consensus_score:.1f}/30
Agreement:      {verdict.agreement_level}
95% CI:         [{verdict.confidence_interval[0]:.1f}, {verdict.confidence_interval[1]:.1f}]
Unanimous:      {'Yes' if verdict.is_unanimous else 'No'}
{'─' * 50}
{chr(10).join(f'⚠ {note}' for note in verdict.dissent_notes) if verdict.dissent_notes else 'No dissent notes'}
"""
