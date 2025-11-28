"""
STRATEGY ENGINE v1.1 - Framework 2: Meadows
============================================

Systems leverage through intervention point identification.
"Where is the highest leverage?"
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class LeverageLevel(Enum):
    """Leverage point levels (Meadows' 12 points grouped)."""
    WEAK = "weak"
    MEDIUM = "medium"
    STRONG = "strong"
    PARADIGM = "paradigm"


@dataclass
class LeveragePoint:
    """A leverage point in the system."""
    level: int
    name: str
    description: str
    leverage_category: LeverageLevel
    strategic_application: str = ""
    ease_of_change: str = "medium"
    impact_potential: str = "medium"
    
    def __post_init__(self):
        if not 1 <= self.level <= 12:
            raise ValueError(f"Leverage level must be 1-12, got {self.level}")


@dataclass
class SystemLoop:
    """A feedback loop in the system."""
    name: str
    loop_type: str
    elements: List[str] = field(default_factory=list)
    strategic_implication: str = ""


@dataclass
class LeverageAnalysis:
    """Complete leverage analysis result."""
    highest_leverage_points: List[LeveragePoint]
    reinforcing_loops: List[str]
    balancing_loops: List[str]
    recommended_interventions: List[str]
    
    def to_dict(self) -> dict:
        return {
            "leverage_points": [
                {"level": lp.level, "name": lp.name, "category": lp.leverage_category.value}
                for lp in self.highest_leverage_points
            ],
            "reinforcing_loops": self.reinforcing_loops,
            "balancing_loops": self.balancing_loops,
            "interventions": self.recommended_interventions
        }


class MeadowsFramework:
    """
    Framework 2: Meadows (Thinking in Systems)
    
    Focus: Systems leverage
    Contribution: High-impact intervention points, feedback loops
    Strategic Question: "Where is the highest leverage?"
    """
    
    LEVERAGE_POINTS = {
        12: ("Parameters", LeverageLevel.WEAK, "Prices, sizes, quantities"),
        11: ("Buffers", LeverageLevel.WEAK, "Inventory, reserves, cash"),
        10: ("Stock-Flow Structures", LeverageLevel.WEAK, "Physical infrastructure"),
        9: ("Delays", LeverageLevel.MEDIUM, "Response times, feedback delays"),
        8: ("Balancing Loops", LeverageLevel.MEDIUM, "Regulatory, market equilibrium"),
        7: ("Reinforcing Loops", LeverageLevel.MEDIUM, "Growth engines, network effects"),
        6: ("Information Flows", LeverageLevel.MEDIUM, "Transparency, data access"),
        5: ("Rules", LeverageLevel.STRONG, "Incentives, constraints, policies"),
        4: ("Self-Organization", LeverageLevel.STRONG, "Who makes decisions"),
        3: ("Goals", LeverageLevel.STRONG, "System purpose"),
        2: ("Mindset", LeverageLevel.PARADIGM, "Underlying assumptions"),
        1: ("Transcendence", LeverageLevel.PARADIGM, "Ability to change paradigms")
    }
    
    @classmethod
    def identify_leverage_points(
        cls,
        system_description: str,
        focus_areas: Optional[List[str]] = None
    ) -> LeverageAnalysis:
        """Identify high-leverage intervention points."""
        leverage_points = []
        
        for level, (name, category, desc) in cls.LEVERAGE_POINTS.items():
            if level <= 5:
                lp = LeveragePoint(
                    level=level,
                    name=name,
                    description=desc,
                    leverage_category=category
                )
                leverage_points.append(lp)
        
        reinforcing = []
        balancing = []
        
        if "growth" in system_description.lower() or "network" in system_description.lower():
            reinforcing.append("Network effect growth loop")
        if "market" in system_description.lower():
            balancing.append("Market equilibrium forces")
        
        interventions = []
        if leverage_points:
            interventions.append(f"Target {leverage_points[0].name} for highest impact")
        
        return LeverageAnalysis(
            highest_leverage_points=leverage_points[:3],
            reinforcing_loops=reinforcing,
            balancing_loops=balancing,
            recommended_interventions=interventions
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for Meadows framework."""
        return """
STEP 2: LEVERAGE POINTS (Meadows)
Identify high-impact intervention points in the system:

MEADOWS' 12 LEVERAGE POINTS (Strategic Application):

WEAK LEVERAGE (Easy to change, low impact):
├─ 12. Parameters: Prices, sizes, quantities
├─ 11. Buffers: Inventory, reserves, cash
└─ 10. Stock-Flow Structures: Physical infrastructure

MEDIUM LEVERAGE:
├─ 9. Delays: Response times, feedback delays
├─ 8. Balancing Loops: Regulatory, market equilibrium
├─ 7. Reinforcing Loops: Growth engines, network effects
└─ 6. Information Flows: Transparency, data access

STRONG LEVERAGE:
├─ 5. Rules: Incentives, constraints, policies
├─ 4. Self-Organization: Who makes decisions
└─ 3. Goals: System purpose

PARADIGM LEVERAGE (Hard to change, highest impact):
├─ 2. Mindset: Underlying assumptions
└─ 1. Transcendence: Ability to change paradigms

STRATEGIC QUESTIONS:
├─ "What's the smallest change with the largest effect?"
├─ "Where are the reinforcing loops we can accelerate?"
├─ "What rules or goals can we redefine?"
└─ "What mindset assumptions are competitors stuck in?"
"""
