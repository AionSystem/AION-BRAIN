"""
SIMPLEXITY v2.0 - Complexity Scoring System
============================================

The quantitative framework for measuring and tracking complexity.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Dict
import math


class ComplexityDimension(Enum):
    """The five core dimensions of complexity."""
    SCALE = "scale"
    COUPLING = "coupling"
    DYNAMICS = "dynamics"
    UNCERTAINTY = "uncertainty"
    EMERGENCE = "emergence"


class ComplexityTrajectory(Enum):
    """Direction of complexity change over time."""
    GROWING = "growing"
    STABLE = "stable"
    DECAYING = "decaying"
    OSCILLATING = "oscillating"
    EXPLOSIVE = "explosive"


class ReversibilityLevel(Enum):
    """How easily a change can be undone."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    IRREVERSIBLE = "irreversible"


@dataclass
class DimensionScore:
    """Score for a single complexity dimension."""
    dimension: ComplexityDimension
    value: float
    rationale: str = ""
    
    def __post_init__(self):
        if not 1.0 <= self.value <= 10.0:
            raise ValueError(f"Dimension score must be 1-10, got {self.value}")


@dataclass
class ComplexityScore:
    """
    Complete complexity assessment with all dimensions.
    
    Composite = sqrt(Scale² + Coupling² + Dynamics² + Uncertainty² + Emergence²)
    
    Interpretation:
    - 1-5: LOW - Direct analysis feasible
    - 6-10: MODERATE - Decomposition recommended
    - 11-15: HIGH - Significant simplification needed
    - 16+: EXTREME - Multiple reduction strategies needed
    """
    scale: float = 5.0
    coupling: float = 5.0
    dynamics: float = 5.0
    uncertainty: float = 5.0
    emergence: float = 5.0
    trajectory: ComplexityTrajectory = ComplexityTrajectory.STABLE
    rationale: Dict[str, str] = field(default_factory=dict)
    
    def __post_init__(self):
        for dim, val in [
            ("scale", self.scale),
            ("coupling", self.coupling),
            ("dynamics", self.dynamics),
            ("uncertainty", self.uncertainty),
            ("emergence", self.emergence)
        ]:
            if not 1.0 <= val <= 10.0:
                raise ValueError(f"{dim} must be 1-10, got {val}")
    
    @property
    def composite(self) -> float:
        """Calculate composite complexity score."""
        return math.sqrt(
            self.scale**2 + 
            self.coupling**2 + 
            self.dynamics**2 + 
            self.uncertainty**2 + 
            self.emergence**2
        )
    
    @property
    def level(self) -> str:
        """Human-readable complexity level."""
        c = self.composite
        if c <= 5:
            return "LOW"
        elif c <= 10:
            return "MODERATE"
        elif c <= 15:
            return "HIGH"
        else:
            return "EXTREME"
    
    @property
    def recommendation(self) -> str:
        """Action recommendation based on score."""
        level = self.level
        recommendations = {
            "LOW": "Direct analysis feasible",
            "MODERATE": "Decomposition recommended",
            "HIGH": "Significant simplification needed",
            "EXTREME": "Multiple reduction strategies + immediate attention"
        }
        return recommendations[level]
    
    def exceeds_ceiling(self, ceiling: float = 15.0) -> bool:
        """Check if composite exceeds threshold."""
        return self.composite > ceiling
    
    def to_dict(self) -> dict:
        """Convert to dictionary for serialization."""
        return {
            "scale": self.scale,
            "coupling": self.coupling,
            "dynamics": self.dynamics,
            "uncertainty": self.uncertainty,
            "emergence": self.emergence,
            "composite": round(self.composite, 2),
            "level": self.level,
            "trajectory": self.trajectory.value,
            "recommendation": self.recommendation
        }
    
    def __str__(self) -> str:
        return (
            f"ComplexityScore(composite={self.composite:.1f}, level={self.level}, "
            f"trajectory={self.trajectory.value})"
        )


@dataclass
class TransferScore:
    """
    Measures whether complexity was truly eliminated vs moved elsewhere.
    
    Score 0-10:
    - 0: True elimination (complexity removed from system)
    - 5: Partial transfer (some moved, some eliminated)
    - 10: Total transfer (complexity just relocated)
    """
    score: float
    source_area: str = ""
    destination_areas: List[str] = field(default_factory=list)
    hidden_costs: List[str] = field(default_factory=list)
    rationale: str = ""
    
    def __post_init__(self):
        if not 0 <= self.score <= 10:
            raise ValueError(f"Transfer score must be 0-10, got {self.score}")
    
    @property
    def is_acceptable(self) -> bool:
        """Check if transfer is acceptable (< 6)."""
        return self.score < 6.0
    
    @property
    def assessment(self) -> str:
        """Human-readable assessment."""
        if self.score <= 2:
            return "True simplification - complexity eliminated"
        elif self.score <= 4:
            return "Mostly eliminated with minor transfer"
        elif self.score <= 6:
            return "Partial transfer - monitor destination"
        elif self.score <= 8:
            return "Significant transfer - complexity relocated"
        else:
            return "Total transfer - no net reduction"


@dataclass
class FragilityScore:
    """
    Measures protective complexity being removed.
    
    Score 0-10:
    - 0: Safe to remove (no protective function)
    - 1-3: Minor protective function (proceed with caution)
    - 4-6: Significant protective function (preserve if possible)
    - 7-10: Critical protective function (DO NOT REMOVE)
    """
    score: float
    redundancy_impact: float = 0.0
    optionality_impact: float = 0.0
    stress_response_impact: float = 0.0
    learning_impact: float = 0.0
    rationale: str = ""
    
    def __post_init__(self):
        if not 0 <= self.score <= 10:
            raise ValueError(f"Fragility score must be 0-10, got {self.score}")
    
    @property
    def is_safe_to_remove(self) -> bool:
        """Check if complexity can be safely removed."""
        return self.score < 4.0
    
    @property
    def exceeds_floor(self, floor: float = 3.0) -> bool:
        """Check if removal would create fragility below floor."""
        return self.score > floor
    
    @property
    def assessment(self) -> str:
        """Human-readable assessment."""
        if self.score <= 3:
            return "Safe to remove"
        elif self.score <= 6:
            return "Proceed with caution - has protective function"
        else:
            return "DO NOT REMOVE - critical protective function"
    
    @classmethod
    def calculate(
        cls,
        redundancy: float,
        optionality: float,
        stress_response: float,
        learning: float,
        rationale: str = ""
    ) -> "FragilityScore":
        """Calculate fragility score from component impacts."""
        score = (redundancy + optionality + stress_response + learning) / 4.0
        return cls(
            score=score,
            redundancy_impact=redundancy,
            optionality_impact=optionality,
            stress_response_impact=stress_response,
            learning_impact=learning,
            rationale=rationale
        )
