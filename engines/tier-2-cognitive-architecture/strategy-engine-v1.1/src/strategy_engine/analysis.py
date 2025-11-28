"""
STRATEGY ENGINE v1.1 - Analysis Results
========================================

Data classes for strategic analysis results.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from .scoring import (
    MoatDurabilityIndex, CompetitorProfile, ResponseProbability,
    PayoffMatrix, EthicsAssessment, EthicsFlag
)
from .config import StrategicPosition


@dataclass
class CompetitiveResponse:
    """Complete competitive response analysis."""
    your_move: str
    competitor_profiles: List[CompetitorProfile]
    response_matrix: List[ResponseProbability]
    second_order_effects: List[str]
    payoff_matrix: Optional[PayoffMatrix] = None
    nash_equilibrium: str = ""
    optimal_strategy: str = ""
    commitment_devices: List[str] = field(default_factory=list)
    
    def to_dict(self) -> dict:
        return {
            "your_move": self.your_move,
            "competitors": [c.to_dict() for c in self.competitor_profiles],
            "responses": [
                {"competitor": r.competitor, "response": r.response_type, "probability": r.probability}
                for r in self.response_matrix
            ],
            "second_order_effects": self.second_order_effects,
            "nash_equilibrium": self.nash_equilibrium,
            "optimal_strategy": self.optimal_strategy,
            "commitment_devices": self.commitment_devices
        }


@dataclass
class StrategicSynthesis:
    """Step 6: Strategic synthesis and roadmap."""
    strategic_position: StrategicPosition
    highest_leverage_interventions: List[str]
    network_strategy: str
    causal_assumptions: List[str]
    sustainability_score: int
    ethics_flag: EthicsFlag
    
    phase_1_actions: List[str]
    phase_2_actions: List[str]
    phase_3_actions: List[str]
    phase_4_actions: List[str]
    
    def to_dict(self) -> dict:
        return {
            "position": self.strategic_position.value,
            "leverage_interventions": self.highest_leverage_interventions,
            "network_strategy": self.network_strategy,
            "assumptions": self.causal_assumptions,
            "sustainability": self.sustainability_score,
            "ethics": self.ethics_flag.value,
            "roadmap": {
                "phase_1_0_90_days": self.phase_1_actions,
                "phase_2_90_180_days": self.phase_2_actions,
                "phase_3_180_365_days": self.phase_3_actions,
                "phase_4_1_3_years": self.phase_4_actions
            }
        }


@dataclass
class StrategicAnalysis:
    """Complete strategic analysis result."""
    organization: str
    industry: str
    strategic_question: str
    
    terrain_analysis: Optional[Dict[str, Any]] = None
    leverage_analysis: Optional[Dict[str, Any]] = None
    network_analysis: Optional[Dict[str, Any]] = None
    causal_model: Optional[Dict[str, Any]] = None
    governance_analysis: Optional[Dict[str, Any]] = None
    
    competitive_response: Optional[CompetitiveResponse] = None
    moat_durability: Optional[MoatDurabilityIndex] = None
    
    synthesis: Optional[StrategicSynthesis] = None
    ethics_assessment: Optional[EthicsAssessment] = None
    
    warnings: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    
    processing_time_ms: float = 0.0
    
    def summary(self) -> str:
        """Generate human-readable summary."""
        lines = [
            "=" * 70,
            "STRATEGY ENGINE v1.1 — THE STRATEGIST'S EDGE",
            "=" * 70,
            f"Organization: {self.organization}",
            f"Industry: {self.industry}",
            f"Question: {self.strategic_question}",
            ""
        ]
        
        if self.synthesis:
            lines.extend([
                f"Strategic Position: {self.synthesis.strategic_position.value.upper()}",
                f"Sustainability Score: {self.synthesis.sustainability_score}/10",
                f"Ethics Flag: [{self.synthesis.ethics_flag.value.upper()}]",
                ""
            ])
        
        if self.moat_durability:
            lines.extend([
                f"Moat Durability Index: {self.moat_durability.score:.2f}",
                f"Moat Strength: {self.moat_durability.strength.value.upper()}",
                f"Estimated Durability: {self.moat_durability.durability_years}",
                ""
            ])
        
        if self.synthesis and self.synthesis.highest_leverage_interventions:
            lines.append("TOP LEVERAGE INTERVENTIONS:")
            for i, intervention in enumerate(self.synthesis.highest_leverage_interventions[:3], 1):
                lines.append(f"  {i}. {intervention}")
            lines.append("")
        
        if self.recommendations:
            lines.append("RECOMMENDATIONS:")
            for rec in self.recommendations[:5]:
                lines.append(f"  → {rec}")
        
        lines.extend(["", "=" * 70])
        
        return "\n".join(lines)
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "organization": self.organization,
            "industry": self.industry,
            "question": self.strategic_question,
            "terrain": self.terrain_analysis,
            "leverage": self.leverage_analysis,
            "network": self.network_analysis,
            "causal": self.causal_model,
            "governance": self.governance_analysis,
            "moat": self.moat_durability.to_dict() if self.moat_durability else None,
            "synthesis": self.synthesis.to_dict() if self.synthesis else None,
            "recommendations": self.recommendations
        }
