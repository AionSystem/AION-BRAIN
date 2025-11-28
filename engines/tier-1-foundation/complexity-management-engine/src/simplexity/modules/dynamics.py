"""
SIMPLEXITY v2.0 - Module 5: Complexity Dynamics
================================================

Track how complexity changes over time.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from ..scoring import ComplexityTrajectory


@dataclass
class TippingPoint:
    """A potential complexity tipping point."""
    name: str
    threshold: float
    current_distance: float
    severity: str = "medium"
    intervention_cost_now: float = 1.0
    intervention_cost_later: float = 3.0


@dataclass
class DynamicsResult:
    """Result of complexity dynamics analysis."""
    trajectory: ComplexityTrajectory
    velocity: str
    drivers: List[str]
    projected_state: str
    tipping_points: List[TippingPoint]
    recommended_interventions: List[str]
    warnings: List[str] = field(default_factory=list)


class DynamicsModule:
    """
    Module 5: Complexity Dynamics (NEW in v2.0)
    
    Track how complexity changes over time:
    - GROWING: Accumulating features, debt, dependencies
    - STABLE: Balanced additions/removals
    - DECAYING: Simplification efforts, deprecation
    - OSCILLATING: Build-up then crisis-driven cleanup
    - EXPLOSIVE: Rapid growth, approaching breakdown
    
    Complexity Growth Drivers:
    - Accretion: Features added without removal
    - Coupling: Dependencies multiply
    - Entropy: Natural disorder increase
    - Scope Creep: Boundaries expand
    - Technical Debt: Shortcuts accumulate
    """
    
    TRAJECTORY_DESCRIPTIONS = {
        ComplexityTrajectory.GROWING: "Accumulating features, debt, dependencies",
        ComplexityTrajectory.STABLE: "Balanced additions/removals",
        ComplexityTrajectory.DECAYING: "Simplification efforts, deprecation",
        ComplexityTrajectory.OSCILLATING: "Build-up then crisis-driven cleanup",
        ComplexityTrajectory.EXPLOSIVE: "Rapid growth, approaching breakdown"
    }
    
    TRAJECTORY_ACTIONS = {
        ComplexityTrajectory.GROWING: "Proactive simplification needed",
        ComplexityTrajectory.STABLE: "Maintain equilibrium",
        ComplexityTrajectory.DECAYING: "Monitor for MVC threshold",
        ComplexityTrajectory.OSCILLATING: "Establish steady-state discipline",
        ComplexityTrajectory.EXPLOSIVE: "IMMEDIATE intervention required"
    }
    
    @classmethod
    def assess_trajectory(
        cls,
        historical_scores: List[float],
        current_score: float,
        time_period: str = "last quarter"
    ) -> ComplexityTrajectory:
        """Determine complexity trajectory from historical data."""
        if not historical_scores:
            return ComplexityTrajectory.STABLE
        
        avg_historical = sum(historical_scores) / len(historical_scores)
        delta = current_score - avg_historical
        variance = sum((s - avg_historical)**2 for s in historical_scores) / len(historical_scores)
        
        if delta > 3:
            return ComplexityTrajectory.EXPLOSIVE
        elif delta > 1:
            return ComplexityTrajectory.GROWING
        elif delta < -1:
            return ComplexityTrajectory.DECAYING
        elif variance > 4:
            return ComplexityTrajectory.OSCILLATING
        else:
            return ComplexityTrajectory.STABLE
    
    @classmethod
    def analyze(
        cls,
        current_score: float,
        historical_scores: Optional[List[float]] = None,
        drivers: Optional[List[str]] = None,
        time_period: str = "last quarter"
    ) -> DynamicsResult:
        """Perform full dynamics analysis."""
        if historical_scores is None:
            historical_scores = []
        if drivers is None:
            drivers = []
        
        trajectory = cls.assess_trajectory(historical_scores, current_score, time_period)
        
        velocity = "stable"
        if trajectory == ComplexityTrajectory.EXPLOSIVE:
            velocity = "rapid increase"
        elif trajectory == ComplexityTrajectory.GROWING:
            velocity = "moderate increase"
        elif trajectory == ComplexityTrajectory.DECAYING:
            velocity = "decreasing"
        
        projected_state = cls.TRAJECTORY_DESCRIPTIONS[trajectory]
        
        tipping_points = []
        if current_score > 12:
            tipping_points.append(TippingPoint(
                name="Complexity ceiling",
                threshold=15.0,
                current_distance=15.0 - current_score,
                severity="high"
            ))
        
        interventions = [cls.TRAJECTORY_ACTIONS[trajectory]]
        
        warnings = []
        if trajectory == ComplexityTrajectory.EXPLOSIVE:
            warnings.append("CRITICAL: Explosive complexity growth detected")
        
        return DynamicsResult(
            trajectory=trajectory,
            velocity=velocity,
            drivers=drivers,
            projected_state=projected_state,
            tipping_points=tipping_points,
            recommended_interventions=interventions,
            warnings=warnings
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for dynamics module."""
        return """
MODULE 5: COMPLEXITY DYNAMICS
Track how complexity changes over time:
- GROWING: Accumulating features, debt, dependencies
- STABLE: Balanced additions/removals
- DECAYING: Simplification efforts, deprecation
- OSCILLATING: Build-up then crisis-driven cleanup
- EXPLOSIVE: Rapid growth, approaching breakdown

DYNAMICS ASSESSMENT:
1. HISTORICAL TRAJECTORY - How has complexity changed?
2. CURRENT VELOCITY - Growing, stable, or decaying?
3. PROJECTED TRAJECTORY - Where is this heading?
4. INTERVENTION POINTS - Where can trajectory be altered?
5. TIPPING POINTS - Thresholds where behavior changes dramatically
"""
