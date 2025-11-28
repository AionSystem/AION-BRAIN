"""
EXPLANATION ENGINE v1.0 - Configuration
=========================================

Configuration options for the Explanation Engine.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List


class AudienceLevel(Enum):
    """Target audience expertise level."""
    EXECUTIVE = "executive"
    TECHNICAL = "technical"
    DOMAIN_EXPERT = "domain_expert"
    GENERAL_PUBLIC = "general_public"
    STAKEHOLDER = "stakeholder"


class ExplanationStyle(Enum):
    """Style of explanation."""
    NARRATIVE = "narrative"
    STRUCTURED = "structured"
    VISUAL = "visual"
    CONVERSATIONAL = "conversational"
    FORMAL = "formal"


class ExplanationDepth(Enum):
    """Depth of explanation."""
    SUMMARY = "summary"
    STANDARD = "standard"
    DETAILED = "detailed"
    COMPREHENSIVE = "comprehensive"


@dataclass
class ExplanationConfig:
    """
    Configuration for Explanation Engine.
    
    Attributes:
        audience_level: Target audience expertise
        style: Explanation style
        depth: Explanation depth
        include_counterfactuals: Generate "what if" scenarios
        include_confidence: Show confidence levels
        include_evidence: Include supporting evidence
    """
    audience_level: AudienceLevel = AudienceLevel.STAKEHOLDER
    style: ExplanationStyle = ExplanationStyle.STRUCTURED
    depth: ExplanationDepth = ExplanationDepth.STANDARD
    include_counterfactuals: bool = True
    include_confidence: bool = True
    include_evidence: bool = True
    max_layers: int = 4
    
    @classmethod
    def for_executives(cls) -> "ExplanationConfig":
        """Executive summary configuration."""
        return cls(
            audience_level=AudienceLevel.EXECUTIVE,
            style=ExplanationStyle.NARRATIVE,
            depth=ExplanationDepth.SUMMARY,
            include_counterfactuals=False,
            max_layers=2
        )
    
    @classmethod
    def for_technical(cls) -> "ExplanationConfig":
        """Technical deep-dive configuration."""
        return cls(
            audience_level=AudienceLevel.TECHNICAL,
            style=ExplanationStyle.STRUCTURED,
            depth=ExplanationDepth.COMPREHENSIVE,
            include_counterfactuals=True,
            max_layers=5
        )
    
    @classmethod
    def for_stakeholders(cls) -> "ExplanationConfig":
        """Stakeholder briefing configuration."""
        return cls(
            audience_level=AudienceLevel.STAKEHOLDER,
            style=ExplanationStyle.STRUCTURED,
            depth=ExplanationDepth.STANDARD,
            include_counterfactuals=True
        )
