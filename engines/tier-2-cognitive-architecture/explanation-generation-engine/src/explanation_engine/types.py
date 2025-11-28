"""
EXPLANATION ENGINE v1.0 - Type Definitions
============================================

Data types for explanations and related concepts.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Any
from datetime import datetime


class LayerType(Enum):
    """Types of explanation layers."""
    HEADLINE = "headline"
    SUMMARY = "summary"
    KEY_FACTORS = "key_factors"
    EVIDENCE = "evidence"
    METHODOLOGY = "methodology"
    LIMITATIONS = "limitations"
    COUNTERFACTUAL = "counterfactual"
    RECOMMENDATIONS = "recommendations"


@dataclass
class ExplanationLayer:
    """A single layer in a multi-level explanation."""
    layer_type: LayerType
    content: str
    confidence: float = 1.0
    supporting_data: Dict = field(default_factory=dict)
    
    def to_dict(self) -> dict:
        return {
            "type": self.layer_type.value,
            "content": self.content,
            "confidence": self.confidence
        }


@dataclass
class AudienceProfile:
    """Profile of target audience."""
    level: str
    domain_knowledge: str
    preferred_format: str
    attention_span: str
    decision_authority: bool = False
    
    @classmethod
    def executive(cls) -> "AudienceProfile":
        return cls(
            level="executive",
            domain_knowledge="high-level",
            preferred_format="bullet points",
            attention_span="short",
            decision_authority=True
        )
    
    @classmethod
    def technical(cls) -> "AudienceProfile":
        return cls(
            level="technical",
            domain_knowledge="deep",
            preferred_format="detailed",
            attention_span="extended",
            decision_authority=False
        )
    
    @classmethod
    def general(cls) -> "AudienceProfile":
        return cls(
            level="general",
            domain_knowledge="basic",
            preferred_format="narrative",
            attention_span="medium",
            decision_authority=False
        )


@dataclass
class CounterfactualExplanation:
    """A counterfactual 'what if' explanation."""
    original_outcome: str
    changed_factor: str
    alternative_outcome: str
    probability_shift: float
    insight: str
    
    def to_dict(self) -> dict:
        return {
            "original": self.original_outcome,
            "if_changed": self.changed_factor,
            "then": self.alternative_outcome,
            "probability_shift": f"{self.probability_shift:+.0%}",
            "insight": self.insight
        }


class QualityLevel(Enum):
    """Quality levels for explanations."""
    EXCELLENT = "excellent"
    GOOD = "good"
    ACCEPTABLE = "acceptable"
    NEEDS_IMPROVEMENT = "needs_improvement"
    POOR = "poor"


@dataclass
class ExplanationQuality:
    """Quality assessment of an explanation."""
    overall_level: QualityLevel
    clarity_score: float
    completeness_score: float
    accuracy_score: float
    audience_fit_score: float
    issues: List[str]
    suggestions: List[str]
    
    def to_dict(self) -> dict:
        return {
            "overall": self.overall_level.value,
            "scores": {
                "clarity": round(self.clarity_score, 2),
                "completeness": round(self.completeness_score, 2),
                "accuracy": round(self.accuracy_score, 2),
                "audience_fit": round(self.audience_fit_score, 2)
            },
            "issues": self.issues,
            "suggestions": self.suggestions
        }


@dataclass
class VerificationResult:
    """Result of explanation verification."""
    is_valid: bool
    factual_accuracy: float
    logical_consistency: float
    source_coverage: float
    issues: List[str]
    
    def to_dict(self) -> dict:
        return {
            "valid": self.is_valid,
            "factual_accuracy": f"{self.factual_accuracy:.0%}",
            "logical_consistency": f"{self.logical_consistency:.0%}",
            "source_coverage": f"{self.source_coverage:.0%}",
            "issues": self.issues
        }


@dataclass
class Explanation:
    """Complete multi-level explanation."""
    topic: str
    audience: AudienceProfile
    layers: List[ExplanationLayer]
    counterfactuals: List[CounterfactualExplanation]
    quality: Optional[ExplanationQuality] = None
    verification: Optional[VerificationResult] = None
    generated_at: datetime = field(default_factory=datetime.now)
    
    def get_layer(self, layer_type: LayerType) -> Optional[ExplanationLayer]:
        """Get a specific layer by type."""
        for layer in self.layers:
            if layer.layer_type == layer_type:
                return layer
        return None
    
    def summary(self) -> str:
        """Generate summary output."""
        lines = [
            "=" * 60,
            f"EXPLANATION: {self.topic}",
            f"Audience: {self.audience.level}",
            "=" * 60
        ]
        
        for layer in self.layers:
            lines.append(f"\n[{layer.layer_type.value.upper()}]")
            lines.append(layer.content)
        
        if self.counterfactuals:
            lines.append("\n[WHAT-IF SCENARIOS]")
            for cf in self.counterfactuals:
                lines.append(f"• If {cf.changed_factor}: {cf.alternative_outcome}")
        
        lines.extend(["", "=" * 60])
        return "\n".join(lines)
    
    def to_dict(self) -> dict:
        return {
            "topic": self.topic,
            "audience": self.audience.level,
            "layers": [l.to_dict() for l in self.layers],
            "counterfactuals": [c.to_dict() for c in self.counterfactuals],
            "quality": self.quality.to_dict() if self.quality else None,
            "verification": self.verification.to_dict() if self.verification else None
        }
