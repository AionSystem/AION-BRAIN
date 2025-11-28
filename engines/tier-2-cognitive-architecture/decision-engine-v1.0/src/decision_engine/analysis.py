"""
DECISION ENGINE v1.0 - Analysis Results
========================================

Data classes for decision analysis results.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from .scoring import (
    BiasAssessment, SatisficingResult, OptionalityScore,
    TemporalAlignment, EthicalAssessment, ConfidenceLevel, TimelineVerdict
)


@dataclass
class DecisionRecommendation:
    """Final decision recommendation with IF-THEN rule."""
    proceed: bool
    confidence: ConfidenceLevel
    frameworks_aligned: int
    timeline: TimelineVerdict
    if_conditions: List[str]
    then_action: str
    else_action: str
    next_steps: List[str]
    
    def to_dict(self) -> dict:
        return {
            "proceed": self.proceed,
            "confidence": self.confidence.value,
            "aligned": f"{self.frameworks_aligned}/5",
            "timeline": self.timeline.value,
            "rule": {
                "if": self.if_conditions,
                "then": self.then_action,
                "else": self.else_action
            },
            "next_steps": self.next_steps
        }
    
    def format_rule(self) -> str:
        """Format the IF-THEN decision rule."""
        conditions = "\nAND ".join(f"[{c}]" for c in self.if_conditions)
        return f"""
IF {conditions}
THEN: {self.then_action}
ELSE: {self.else_action}
"""


@dataclass
class DecisionAnalysis:
    """Complete decision analysis result."""
    decision_statement: str
    surface_question: str
    underlying_question: str
    
    bias_assessment: Optional[BiasAssessment] = None
    satisficing_result: Optional[SatisficingResult] = None
    optionality_score: Optional[OptionalityScore] = None
    temporal_alignment: Optional[TemporalAlignment] = None
    ethical_assessment: Optional[EthicalAssessment] = None
    
    recommendation: Optional[DecisionRecommendation] = None
    
    warnings: List[str] = field(default_factory=list)
    insights: List[str] = field(default_factory=list)
    
    processing_time_ms: float = 0.0
    
    def count_aligned_frameworks(self) -> int:
        """Count how many frameworks support proceeding."""
        count = 0
        
        if self.bias_assessment and self.bias_assessment.bias_severity != "high":
            count += 1
        
        if self.satisficing_result and self.satisficing_result.reversibility_assessment != "low":
            count += 1
        
        if self.optionality_score:
            from .scoring import FragilityCategory
            if self.optionality_score.fragility != FragilityCategory.FRAGILE:
                count += 1
        
        if self.temporal_alignment:
            from .scoring import TemporalVerdict
            if self.temporal_alignment.verdict == TemporalVerdict.ACT_NOW:
                count += 1
        
        if self.ethical_assessment:
            from .scoring import EthicalVerdict
            if self.ethical_assessment.verdict != EthicalVerdict.UNJUST:
                count += 1
        
        return count
    
    def summary(self) -> str:
        """Generate human-readable summary."""
        lines = [
            "=" * 70,
            "DECISION ENGINE v1.0 — DECIDERE",
            "=" * 70,
            f"Decision: {self.decision_statement}",
            f"Surface Question: {self.surface_question}",
            f"Underlying Question: {self.underlying_question}",
            ""
        ]
        
        if self.bias_assessment:
            biases = ", ".join(b.value for b in self.bias_assessment.detected_biases)
            lines.append(f"Biases Detected: {biases or 'None'} [{self.bias_assessment.bias_severity.upper()}]")
        
        if self.optionality_score:
            lines.append(f"Fragility: {self.optionality_score.fragility.value.upper()}")
            lines.append(f"Optionality: {self.optionality_score.optionality_level}")
        
        if self.temporal_alignment:
            lines.append(f"Timing: {self.temporal_alignment.phase.value.upper()} → {self.temporal_alignment.verdict.value.upper()}")
        
        if self.ethical_assessment:
            lines.append(f"Ethics: {self.ethical_assessment.verdict.value.upper()} (Net utility: {self.ethical_assessment.net_utility})")
        
        lines.append("")
        
        if self.recommendation:
            lines.extend([
                "=" * 70,
                "RECOMMENDATION",
                "=" * 70,
                f"Proceed: {'YES' if self.recommendation.proceed else 'NO'}",
                f"Confidence: {self.recommendation.confidence.value.upper()}",
                f"Frameworks Aligned: {self.recommendation.frameworks_aligned}/5",
                f"Timeline: {self.recommendation.timeline.value.upper()}",
                "",
                "Decision Rule:",
                self.recommendation.format_rule(),
                "",
                "Next Steps:"
            ])
            for i, step in enumerate(self.recommendation.next_steps, 1):
                lines.append(f"  {i}. {step}")
        
        lines.extend(["", "=" * 70])
        
        return "\n".join(lines)
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "decision": self.decision_statement,
            "surface_question": self.surface_question,
            "underlying_question": self.underlying_question,
            "bias": self.bias_assessment.to_dict() if self.bias_assessment else None,
            "satisficing": self.satisficing_result.to_dict() if self.satisficing_result else None,
            "optionality": self.optionality_score.to_dict() if self.optionality_score else None,
            "temporal": self.temporal_alignment.to_dict() if self.temporal_alignment else None,
            "ethics": self.ethical_assessment.to_dict() if self.ethical_assessment else None,
            "recommendation": self.recommendation.to_dict() if self.recommendation else None,
            "warnings": self.warnings,
            "insights": self.insights
        }
