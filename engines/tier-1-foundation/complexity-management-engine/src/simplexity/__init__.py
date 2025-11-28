"""
SIMPLEXITY v2.0 - Complexity Management Engine
===============================================

The intelligent complexity navigator that transforms overwhelming
complexity into actionable understanding.

Codename: SIMPLEXITY
Classification: TIER 1 - FOUNDATION
Author: Sheldon K. Salmon
License: Apache 2.0
"""

from .core import Simplexity
from .config import SimplexityConfig, OperationalMode, OutputLevel
from .scoring import (
    ComplexityScore,
    ComplexityDimension,
    ComplexityTrajectory,
    TransferScore,
    FragilityScore,
    ReversibilityLevel
)
from .modules import (
    AbstractionLevel,
    EmergenceType,
    DecompositionStrategy,
    SimplificationLevel,
    CognitiveProfile
)
from .analysis import (
    ComplexityAnalysis,
    DecompositionResult,
    SimplificationResult,
    CalibrationResult,
    TransferAnalysis,
    MVCResult
)

__version__ = "2.0.0"
__author__ = "Sheldon K. Salmon"
__codename__ = "SIMPLEXITY"

__all__ = [
    "Simplexity",
    "SimplexityConfig",
    "OperationalMode",
    "OutputLevel",
    "ComplexityScore",
    "ComplexityDimension",
    "ComplexityTrajectory",
    "TransferScore",
    "FragilityScore",
    "ReversibilityLevel",
    "AbstractionLevel",
    "EmergenceType",
    "DecompositionStrategy",
    "SimplificationLevel",
    "CognitiveProfile",
    "ComplexityAnalysis",
    "DecompositionResult",
    "SimplificationResult",
    "CalibrationResult",
    "TransferAnalysis",
    "MVCResult",
]
