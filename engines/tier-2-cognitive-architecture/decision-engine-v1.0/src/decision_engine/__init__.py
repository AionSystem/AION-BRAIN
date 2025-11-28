"""
DECISION ENGINE v1.0 - DECIDERE
================================

Personal Decision Analysis Framework integrating 5 specialized frameworks.

Codename: DECIDERE
Classification: TIER 1 - FOUNDATION
Author: Sheldon K. Salmon
License: Apache 2.0
"""

from .core import DecisionEngine
from .config import DecisionConfig, AnalysisMode
from .scoring import (
    BiasAssessment, BiasType, DebiasingStrategy,
    AspirationalLevel, SatisficingResult,
    FragilityCategory, OptionalityScore,
    TemporalPhase, TemporalAlignment, TemporalVerdict,
    EthicalVerdict, StakeholderImpact, EthicalAssessment, MoralCircle,
    ConfidenceLevel, TimelineVerdict
)
from .frameworks import (
    KahnemanFramework,
    SimonFramework,
    TalebFramework,
    BergsonFramework,
    RawlsSingerFramework
)
from .analysis import DecisionAnalysis, DecisionRecommendation

__version__ = "1.0.0"
__author__ = "Sheldon K. Salmon"
__codename__ = "DECIDERE"

__all__ = [
    "DecisionEngine",
    "DecisionConfig",
    "AnalysisMode",
    "BiasAssessment",
    "BiasType",
    "DebiasingStrategy",
    "AspirationalLevel",
    "SatisficingResult",
    "FragilityCategory",
    "OptionalityScore",
    "TemporalPhase",
    "TemporalAlignment",
    "TemporalVerdict",
    "EthicalVerdict",
    "EthicalAssessment",
    "StakeholderImpact",
    "MoralCircle",
    "ConfidenceLevel",
    "TimelineVerdict",
    "KahnemanFramework",
    "SimonFramework",
    "TalebFramework",
    "BergsonFramework",
    "RawlsSingerFramework",
    "DecisionAnalysis",
    "DecisionRecommendation",
]
