"""
STRATEGY ENGINE v1.1 - Scoring Systems
=======================================

Moat Durability Index and Competitive Response scoring.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Tuple


class MoatStrength(Enum):
    """Moat strength levels based on MDI score."""
    FORTRESS = "fortress"
    STRONG = "strong"
    MODERATE = "moderate"
    WEAK = "weak"
    NONE = "none"


class EthicsFlag(Enum):
    """Ethics assessment flags."""
    GREEN = "green"
    YELLOW = "yellow"
    RED = "red"


@dataclass
class MoatDimension:
    """A single dimension of the moat durability assessment."""
    name: str
    score: float
    weight: float
    reasoning: str = ""
    
    def __post_init__(self):
        if not 0 <= self.score <= 10:
            raise ValueError(f"Score must be 0-10, got {self.score}")
    
    @property
    def weighted_score(self) -> float:
        return self.score * self.weight


@dataclass
class MoatDurabilityIndex:
    """
    Moat Durability Index (MDI) calculation.
    
    MDI = (Imitation × 0.25) + (Switching × 0.20) + (Network × 0.20)
        + (Scale × 0.15) + (Brand × 0.10) + (Regulatory × 0.10)
    
    Interpretation:
    - 8.0-10.0: FORTRESS MOAT (10+ year durability)
    - 6.0-7.9: STRONG MOAT (5-10 year durability)
    - 4.0-5.9: MODERATE MOAT (2-5 year durability)
    - 2.0-3.9: WEAK MOAT (1-2 year durability)
    - 0.0-1.9: NO MOAT (< 1 year before commoditization)
    """
    imitation_difficulty: float = 5.0
    switching_costs: float = 5.0
    network_effects: float = 5.0
    scale_advantages: float = 5.0
    brand_trust: float = 5.0
    regulatory_moat: float = 5.0
    reasoning: Dict[str, str] = field(default_factory=dict)
    
    WEIGHTS = {
        "imitation_difficulty": 0.25,
        "switching_costs": 0.20,
        "network_effects": 0.20,
        "scale_advantages": 0.15,
        "brand_trust": 0.10,
        "regulatory_moat": 0.10
    }
    
    def __post_init__(self):
        for name in self.WEIGHTS.keys():
            value = getattr(self, name)
            if not 0 <= value <= 10:
                raise ValueError(f"{name} must be 0-10, got {value}")
    
    @property
    def score(self) -> float:
        """Calculate the weighted MDI score."""
        return (
            self.imitation_difficulty * self.WEIGHTS["imitation_difficulty"] +
            self.switching_costs * self.WEIGHTS["switching_costs"] +
            self.network_effects * self.WEIGHTS["network_effects"] +
            self.scale_advantages * self.WEIGHTS["scale_advantages"] +
            self.brand_trust * self.WEIGHTS["brand_trust"] +
            self.regulatory_moat * self.WEIGHTS["regulatory_moat"]
        )
    
    @property
    def strength(self) -> MoatStrength:
        """Determine moat strength from score."""
        s = self.score
        if s >= 8.0:
            return MoatStrength.FORTRESS
        elif s >= 6.0:
            return MoatStrength.STRONG
        elif s >= 4.0:
            return MoatStrength.MODERATE
        elif s >= 2.0:
            return MoatStrength.WEAK
        else:
            return MoatStrength.NONE
    
    @property
    def durability_years(self) -> str:
        """Estimated durability in years."""
        strength = self.strength
        durations = {
            MoatStrength.FORTRESS: "10+ years",
            MoatStrength.STRONG: "5-10 years",
            MoatStrength.MODERATE: "2-5 years",
            MoatStrength.WEAK: "1-2 years",
            MoatStrength.NONE: "< 1 year"
        }
        return durations[strength]
    
    def get_weakest_dimensions(self, n: int = 3) -> List[Tuple[str, float]]:
        """Get the n weakest dimensions for improvement priority."""
        dimensions = [
            ("imitation_difficulty", self.imitation_difficulty),
            ("switching_costs", self.switching_costs),
            ("network_effects", self.network_effects),
            ("scale_advantages", self.scale_advantages),
            ("brand_trust", self.brand_trust),
            ("regulatory_moat", self.regulatory_moat)
        ]
        return sorted(dimensions, key=lambda x: x[1])[:n]
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "score": round(self.score, 2),
            "strength": self.strength.value,
            "durability": self.durability_years,
            "dimensions": {
                "imitation_difficulty": self.imitation_difficulty,
                "switching_costs": self.switching_costs,
                "network_effects": self.network_effects,
                "scale_advantages": self.scale_advantages,
                "brand_trust": self.brand_trust,
                "regulatory_moat": self.regulatory_moat
            },
            "improvement_priorities": self.get_weakest_dimensions()
        }


@dataclass
class CompetitorProfile:
    """Profile of a competitor for response simulation."""
    name: str
    posture: str = "defensive"
    resources: str = "adequate"
    response_speed: str = "medium"
    pattern: str = "accommodating"
    market_stakes: str = "medium"
    
    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "posture": self.posture,
            "resources": self.resources,
            "response_speed": self.response_speed,
            "pattern": self.pattern,
            "market_stakes": self.market_stakes
        }


@dataclass
class ResponseProbability:
    """A possible competitive response with probability."""
    competitor: str
    response_type: str
    probability: float
    your_counter: str
    
    def __post_init__(self):
        if not 0 <= self.probability <= 100:
            raise ValueError(f"Probability must be 0-100, got {self.probability}")


@dataclass
class PayoffMatrix:
    """
    Simple 2x2 payoff matrix for game theory analysis.
    
    Format: (your_payoff, competitor_payoff)
    """
    aggressive_aggressive: Tuple[int, int] = (-2, -2)
    aggressive_passive: Tuple[int, int] = (3, -1)
    passive_aggressive: Tuple[int, int] = (-1, 3)
    passive_passive: Tuple[int, int] = (1, 1)
    
    def find_nash_equilibrium(self) -> str:
        """Identify the Nash equilibrium."""
        aa_you, aa_comp = self.aggressive_aggressive
        ap_you, ap_comp = self.aggressive_passive
        pa_you, pa_comp = self.passive_aggressive
        pp_you, pp_comp = self.passive_passive
        
        if aa_you >= pa_you and aa_comp >= ap_comp:
            return "Aggressive-Aggressive"
        if pp_you >= ap_you and pp_comp >= pa_comp:
            return "Passive-Passive"
        if ap_you >= pp_you and pa_comp >= aa_comp:
            return "Mixed strategy equilibrium"
        return "Aggressive-Passive (you aggressive, competitor passive)"
    
    def recommend_strategy(self) -> str:
        """Recommend optimal strategy based on payoffs."""
        ap_you = self.aggressive_passive[0]
        pp_you = self.passive_passive[0]
        aa_you = self.aggressive_aggressive[0]
        pa_you = self.passive_aggressive[0]
        
        aggressive_expected = (ap_you + aa_you) / 2
        passive_expected = (pp_you + pa_you) / 2
        
        if aggressive_expected > passive_expected:
            return "Aggressive strategy recommended"
        elif passive_expected > aggressive_expected:
            return "Passive strategy recommended"
        else:
            return "Strategy depends on competitor intelligence"


@dataclass
class EthicsAssessment:
    """Ethics assessment for a strategy."""
    flag: EthicsFlag
    concerns: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    
    PROHIBITED_PRACTICES = [
        "predatory_pricing",
        "regulatory_capture",
        "monopolistic_practices",
        "misleading_marketing",
        "labor_exploitation",
        "environmental_harm"
    ]
    
    @classmethod
    def assess(cls, strategy_elements: List[str]) -> "EthicsAssessment":
        """Assess ethics of strategy elements."""
        concerns = []
        for element in strategy_elements:
            element_lower = element.lower()
            for prohibited in cls.PROHIBITED_PRACTICES:
                if prohibited.replace("_", " ") in element_lower:
                    concerns.append(f"Potential {prohibited.replace('_', ' ')}")
        
        if not concerns:
            return cls(flag=EthicsFlag.GREEN)
        elif len(concerns) <= 2:
            return cls(
                flag=EthicsFlag.YELLOW,
                concerns=concerns,
                recommendations=["Review strategy for potential externalities"]
            )
        else:
            return cls(
                flag=EthicsFlag.RED,
                concerns=concerns,
                recommendations=["Strategy violates ethical boundaries - revise required"]
            )
