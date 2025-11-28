"""
SIMPLEXITY v2.0 - Analysis Results
===================================

Data classes for analysis results.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from .scoring import ComplexityScore, TransferScore, FragilityScore, ReversibilityLevel
from .config import OutputLevel


@dataclass
class ComplexityAnalysis:
    """Complete complexity analysis result."""
    score: ComplexityScore
    abstraction_level: str
    emergence_detected: List[str]
    decomposition_strategy: str
    simplification_level: str
    warnings: List[str] = field(default_factory=list)
    
    def to_dict(self) -> dict:
        return {
            "score": self.score.to_dict(),
            "abstraction_level": self.abstraction_level,
            "emergence_detected": self.emergence_detected,
            "decomposition_strategy": self.decomposition_strategy,
            "simplification_level": self.simplification_level,
            "warnings": self.warnings
        }


@dataclass
class DecompositionResult:
    """Result of problem decomposition."""
    original_problem: str
    strategy: str
    sub_problems: List[str]
    reversibility: ReversibilityLevel
    is_mece: bool
    rationale: str


@dataclass
class SimplificationResult:
    """Result of simplification."""
    level: int
    preservation_rate: float
    elements_simplified: List[str]
    elements_preserved: List[str]
    fragility_check: FragilityScore
    warnings: List[str] = field(default_factory=list)


@dataclass
class CalibrationResult:
    """Result of cognitive calibration."""
    output_level: OutputLevel
    complexity_factor: float
    adjustments: List[str]
    format_recommendations: List[str]


@dataclass
class TransferAnalysis:
    """Analysis of complexity transfer."""
    source: str
    destinations: List[str]
    transfer_score: TransferScore
    net_change: float
    is_true_simplification: bool


@dataclass
class MVCResult:
    """Minimum viable complexity result."""
    goal: str
    essential_elements: List[str]
    removed_elements: List[str]
    mvc_score: float
    reduction_achieved: float


@dataclass
class SimplexityAnalysis:
    """Complete SIMPLEXITY v2.0 analysis result."""
    problem: str
    goal: str
    audience: Optional[str]
    
    complexity_score: ComplexityScore
    calibration: Optional[CalibrationResult]
    
    abstraction_result: Optional[Dict[str, Any]]
    emergence_result: Optional[Dict[str, Any]]
    decomposition_result: Optional[Dict[str, Any]]
    simplification_result: Optional[Dict[str, Any]]
    
    dynamics_result: Optional[Dict[str, Any]]
    transfer_result: Optional[Dict[str, Any]]
    mvc_result: Optional[Dict[str, Any]]
    
    safety_alerts: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    
    processing_time_ms: float = 0.0
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "problem": self.problem,
            "goal": self.goal,
            "audience": self.audience,
            "complexity_score": self.complexity_score.to_dict(),
            "safety_alerts": self.safety_alerts,
            "recommendations": self.recommendations
        }
    
    def summary(self) -> str:
        """Generate human-readable summary."""
        lines = [
            "=" * 60,
            "SIMPLEXITY v2.0 ANALYSIS SUMMARY",
            "=" * 60,
            f"Problem: {self.problem[:50]}..." if len(self.problem) > 50 else f"Problem: {self.problem}",
            f"Goal: {self.goal}",
            "",
            f"Complexity Score: {self.complexity_score.composite:.1f} ({self.complexity_score.level})",
            f"Trajectory: {self.complexity_score.trajectory.value}",
            f"Recommendation: {self.complexity_score.recommendation}",
        ]
        
        if self.safety_alerts:
            lines.append("")
            lines.append("SAFETY ALERTS:")
            for alert in self.safety_alerts:
                lines.append(f"  ⚠ {alert}")
        
        if self.recommendations:
            lines.append("")
            lines.append("RECOMMENDATIONS:")
            for rec in self.recommendations:
                lines.append(f"  → {rec}")
        
        lines.append("")
        lines.append("=" * 60)
        
        return "\n".join(lines)
