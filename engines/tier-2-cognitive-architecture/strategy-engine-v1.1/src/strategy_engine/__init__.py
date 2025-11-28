"""
STRATEGY ENGINE v1.1 - The Strategist's Edge
=============================================

A 5-framework strategic analysis system for competitive strategy,
market positioning, and sustainable advantage creation.

Codename: The Strategist's Edge
Classification: TIER 2 - COGNITIVE ARCHITECTURE
Author: Sheldon K. Salmon
License: Apache 2.0
"""

from .core import StrategyEngine
from .config import StrategyConfig, AnalysisMode
from .scoring import (
    MoatDurabilityIndex,
    MoatStrength,
    CompetitorProfile,
    ResponseProbability,
    PayoffMatrix,
    EthicsFlag
)
from .frameworks import (
    TerrainAnalysis,
    LeveragePoint,
    NetworkDynamics,
    CausalModel,
    ResourceGovernance
)
from .analysis import (
    StrategicAnalysis,
    CompetitiveResponse,
    StrategicSynthesis
)

__version__ = "1.1.0"
__author__ = "Sheldon K. Salmon"
__codename__ = "The Strategist's Edge"

__all__ = [
    "StrategyEngine",
    "StrategyConfig",
    "AnalysisMode",
    "MoatDurabilityIndex",
    "MoatStrength",
    "CompetitorProfile",
    "ResponseProbability",
    "PayoffMatrix",
    "EthicsFlag",
    "TerrainAnalysis",
    "LeveragePoint",
    "NetworkDynamics",
    "CausalModel",
    "ResourceGovernance",
    "StrategicAnalysis",
    "CompetitiveResponse",
    "StrategicSynthesis",
]
