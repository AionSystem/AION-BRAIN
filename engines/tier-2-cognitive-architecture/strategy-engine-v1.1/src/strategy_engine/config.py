"""
STRATEGY ENGINE v1.1 - Configuration
=====================================

Configuration options for the Strategy Engine.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List


class AnalysisMode(Enum):
    """Analysis modes for Strategy Engine."""
    FULL = "full"
    TERRAIN = "terrain"
    MOAT = "moat"
    RESPONSE = "response"
    QUICK = "quick"


class MarketStructure(Enum):
    """Types of market structure."""
    MONOPOLY = "monopoly"
    OLIGOPOLY = "oligopoly"
    COMPETITIVE = "competitive"
    FRAGMENTED = "fragmented"


class BarrierLevel(Enum):
    """Market entry barrier levels."""
    VERY_HIGH = "very_high"
    HIGH = "high"
    MODERATE = "moderate"
    LOW = "low"
    MINIMAL = "minimal"


class StrategicPosture(Enum):
    """Competitor strategic postures."""
    AGGRESSIVE = "aggressive"
    DEFENSIVE = "defensive"
    OPPORTUNISTIC = "opportunistic"
    INERT = "inert"


class ResourceCapacity(Enum):
    """Resource capacity levels."""
    ABUNDANT = "abundant"
    ADEQUATE = "adequate"
    CONSTRAINED = "constrained"


class ResponseSpeed(Enum):
    """Competitor response speed."""
    FAST = "fast"
    MEDIUM = "medium"
    SLOW = "slow"


class ResponsePattern(Enum):
    """Historical response patterns."""
    RETALIATORY = "retaliatory"
    ACCOMMODATING = "accommodating"
    UNPREDICTABLE = "unpredictable"


class TerrainType(Enum):
    """Strategic terrain types."""
    PURE_BLUE = "pure_blue"
    HYBRID = "hybrid"
    PURE_RED = "pure_red"


class StrategicPosition(Enum):
    """Strategic positioning."""
    BLUE_OCEAN = "blue_ocean"
    RED_OCEAN = "red_ocean"
    HYBRID = "hybrid"


@dataclass
class StrategyConfig:
    """
    Configuration for Strategy Engine.
    
    Attributes:
        mode: Analysis mode (full/terrain/moat/response/quick)
        enable_response_simulator: Include competitive response analysis
        enable_moat_assessment: Include moat durability index
        enable_ethics_check: Apply ethical guardrails
        time_horizon_years: Strategic planning horizon
    """
    mode: AnalysisMode = AnalysisMode.FULL
    enable_response_simulator: bool = True
    enable_moat_assessment: bool = True
    enable_ethics_check: bool = True
    time_horizon_years: int = 3
    
    @classmethod
    def full(cls) -> "StrategyConfig":
        """Full 6-step analysis with all features."""
        return cls(mode=AnalysisMode.FULL)
    
    @classmethod
    def terrain_only(cls) -> "StrategyConfig":
        """Sun Tzu competitive landscape only."""
        return cls(
            mode=AnalysisMode.TERRAIN,
            enable_response_simulator=False,
            enable_moat_assessment=False
        )
    
    @classmethod
    def moat_only(cls) -> "StrategyConfig":
        """Moat durability assessment only."""
        return cls(
            mode=AnalysisMode.MOAT,
            enable_response_simulator=False,
            enable_moat_assessment=True
        )
    
    @classmethod
    def response_only(cls) -> "StrategyConfig":
        """Competitive response simulation only."""
        return cls(
            mode=AnalysisMode.RESPONSE,
            enable_response_simulator=True,
            enable_moat_assessment=False
        )
    
    @classmethod
    def quick(cls) -> "StrategyConfig":
        """Quick 15-minute strategic overview."""
        return cls(
            mode=AnalysisMode.QUICK,
            enable_response_simulator=True,
            enable_moat_assessment=True,
            time_horizon_years=1
        )


@dataclass
class OrganizationContext:
    """Context about the organization being analyzed."""
    name: str
    industry: str
    strategic_question: str
    current_advantages: List[str] = field(default_factory=list)
    resources: str = "adequate"
    funding_stage: Optional[str] = None
    user_count: Optional[int] = None
    market_share: Optional[float] = None
