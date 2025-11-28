"""
SIMPLEXITY v2.0 - Configuration
================================

Configuration options for the Complexity Management Engine.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List


class OperationalMode(Enum):
    """Operational modes for SIMPLEXITY analysis."""
    QUICK = "quick"
    STANDARD = "standard"
    DEEP = "deep"
    MONITOR = "monitor"


class OutputLevel(Enum):
    """Output complexity levels for cognitive calibration."""
    SINGLE_INSIGHT = 1
    EXECUTIVE_SUMMARY = 2
    STANDARD_ANALYSIS = 3
    DEEP_ANALYSIS = 4
    COMPLETE_COMPLEXITY = 5


class ExpertiseLevel(Enum):
    """Audience expertise levels."""
    NOVICE = "novice"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"
    MASTER = "master"


class CognitiveState(Enum):
    """Current cognitive state of audience."""
    FOCUSED = "focused"
    STRESSED = "stressed"
    FATIGUED = "fatigued"
    CRISIS = "crisis"


class TimeAvailable(Enum):
    """Time available for analysis."""
    AMPLE = "ample"
    LIMITED = "limited"
    URGENT = "urgent"
    IMMEDIATE = "immediate"


class DecisionStakes(Enum):
    """Stakes level of the decision."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class SimplexityConfig:
    """
    Configuration for SIMPLEXITY engine.
    
    Attributes:
        mode: Operational mode (quick/standard/deep/monitor)
        complexity_ceiling: Maximum acceptable complexity score
        fragility_floor: Minimum anti-fragility score
        transfer_threshold: Maximum acceptable transfer score
        enable_dynamics: Track complexity over time
        enable_calibration: Calibrate output to audience
        enable_transfer_detection: Detect complexity transfer
        enable_mvc: Find minimum viable complexity
        enable_safety_alerts: Warn on threshold violations
    """
    mode: OperationalMode = OperationalMode.STANDARD
    complexity_ceiling: float = 15.0
    fragility_floor: float = 3.0
    transfer_threshold: float = 6.0
    enable_dynamics: bool = True
    enable_calibration: bool = True
    enable_transfer_detection: bool = True
    enable_mvc: bool = True
    enable_safety_alerts: bool = True
    custom_thresholds: dict = field(default_factory=dict)
    
    @classmethod
    def quick(cls) -> "SimplexityConfig":
        """Quick mode - 5 minute analysis."""
        return cls(
            mode=OperationalMode.QUICK,
            enable_dynamics=False,
            enable_transfer_detection=True,
            enable_mvc=True,
            enable_calibration=False
        )
    
    @classmethod
    def standard(cls) -> "SimplexityConfig":
        """Standard mode - Full 8-module analysis."""
        return cls(mode=OperationalMode.STANDARD)
    
    @classmethod
    def deep(cls) -> "SimplexityConfig":
        """Deep mode - Extended analysis with sensitivity."""
        return cls(
            mode=OperationalMode.DEEP,
            complexity_ceiling=20.0,
            enable_dynamics=True,
            enable_calibration=True,
            enable_transfer_detection=True,
            enable_mvc=True
        )
    
    @classmethod
    def monitor(cls) -> "SimplexityConfig":
        """Monitor mode - Ongoing complexity tracking."""
        return cls(
            mode=OperationalMode.MONITOR,
            enable_dynamics=True,
            enable_safety_alerts=True
        )
    
    @classmethod
    def crisis(cls) -> "SimplexityConfig":
        """Crisis mode - Minimal viable analysis."""
        return cls(
            mode=OperationalMode.QUICK,
            enable_dynamics=False,
            enable_calibration=True,
            enable_transfer_detection=False,
            enable_mvc=True,
            enable_safety_alerts=True
        )


@dataclass
class AudienceProfile:
    """Profile of the target audience for calibration."""
    expertise: ExpertiseLevel = ExpertiseLevel.INTERMEDIATE
    state: CognitiveState = CognitiveState.FOCUSED
    time_available: TimeAvailable = TimeAvailable.LIMITED
    stakes: DecisionStakes = DecisionStakes.MEDIUM
    
    def recommended_output_level(self) -> OutputLevel:
        """Determine appropriate output level based on profile."""
        if self.state == CognitiveState.CRISIS:
            return OutputLevel.SINGLE_INSIGHT
        
        if self.state == CognitiveState.STRESSED or self.time_available == TimeAvailable.IMMEDIATE:
            return OutputLevel.EXECUTIVE_SUMMARY
        
        if self.stakes == DecisionStakes.CRITICAL and self.expertise == ExpertiseLevel.MASTER:
            return OutputLevel.COMPLETE_COMPLEXITY
        
        if self.stakes in (DecisionStakes.HIGH, DecisionStakes.CRITICAL):
            return OutputLevel.DEEP_ANALYSIS
        
        return OutputLevel.STANDARD_ANALYSIS
    
    def complexity_reduction_factor(self) -> float:
        """How much to reduce complexity based on state."""
        factors = {
            CognitiveState.FOCUSED: 1.0,
            CognitiveState.STRESSED: 0.6,
            CognitiveState.FATIGUED: 0.4,
            CognitiveState.CRISIS: 0.2
        }
        return factors.get(self.state, 1.0)
