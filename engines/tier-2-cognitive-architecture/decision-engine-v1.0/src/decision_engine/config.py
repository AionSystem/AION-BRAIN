"""
DECISION ENGINE v1.0 - Configuration
=====================================

Configuration options for the Decision Engine.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List


class AnalysisMode(Enum):
    """Analysis modes for Decision Engine."""
    QUICK = "quick"
    STANDARD = "standard"
    DEEP = "deep"


class CulturalLens(Enum):
    """Cultural perspectives for decision analysis."""
    WESTERN = "western"
    CONFUCIAN = "confucian"
    DAOIST = "daoist"
    UBUNTU = "ubuntu"
    INDIGENOUS = "indigenous"
    ISLAMIC_TAWHID = "islamic_tawhid"


@dataclass
class DecisionConfig:
    """
    Configuration for Decision Engine.
    
    Attributes:
        mode: Analysis mode (quick/standard/deep)
        enable_bias_detection: Include Kahneman bias analysis
        enable_satisficing: Include Simon satisficing analysis
        enable_antifragility: Include Taleb optionality analysis
        enable_temporal: Include Bergson timing analysis
        enable_ethics: Include Rawls/Singer ethical validation
        cultural_lens: Optional cultural perspective
    """
    mode: AnalysisMode = AnalysisMode.STANDARD
    enable_bias_detection: bool = True
    enable_satisficing: bool = True
    enable_antifragility: bool = True
    enable_temporal: bool = True
    enable_ethics: bool = True
    cultural_lens: Optional[CulturalLens] = None
    include_premortem: bool = True
    include_expected_value: bool = True
    
    @classmethod
    def quick(cls) -> "DecisionConfig":
        """Quick 5-10 minute analysis."""
        return cls(
            mode=AnalysisMode.QUICK,
            enable_satisficing=False,
            enable_temporal=False,
            include_premortem=False,
            include_expected_value=False
        )
    
    @classmethod
    def standard(cls) -> "DecisionConfig":
        """Standard 15-20 minute analysis."""
        return cls(mode=AnalysisMode.STANDARD)
    
    @classmethod
    def deep(cls) -> "DecisionConfig":
        """Deep 30-45 minute analysis."""
        return cls(
            mode=AnalysisMode.DEEP,
            include_premortem=True,
            include_expected_value=True
        )
    
    @classmethod
    def with_cultural_lens(cls, lens: CulturalLens) -> "DecisionConfig":
        """Deep mode with cultural perspective."""
        return cls(
            mode=AnalysisMode.DEEP,
            cultural_lens=lens
        )


@dataclass
class DecisionContext:
    """Context about the decision being analyzed."""
    decision_statement: str
    surface_question: str = ""
    underlying_question: str = ""
    decision_variables: List[str] = field(default_factory=list)
    success_criteria: List[str] = field(default_factory=list)
    stakeholders: List[str] = field(default_factory=list)
    time_horizon: str = "1 year"
    reversibility: str = "medium"
