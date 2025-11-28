"""
STRATEGY ENGINE v1.1 - Framework 1: Sun Tzu
============================================

Competitive positioning through terrain analysis.
"Where and when to fight?"
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class ConcentrationLevel(Enum):
    """Market concentration levels."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class BlueOceanPotential(Enum):
    """Blue ocean opportunity level."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RedOceanIntensity(Enum):
    """Red ocean competition intensity."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class MarketActor:
    """An actor in the competitive landscape."""
    name: str
    actor_type: str
    threat_level: str = "medium"
    notes: str = ""


@dataclass
class StructuralAdvantage:
    """A structural competitive advantage."""
    advantage_type: str
    description: str
    strength: str = "medium"


@dataclass
class TerrainAnalysis:
    """
    Complete terrain analysis result.
    Step 1 of the 6-step protocol.
    """
    market_type: str = "competitive"
    concentration: ConcentrationLevel = ConcentrationLevel.MEDIUM
    barriers_to_entry: str = "moderate"
    
    direct_competitors: List[str] = field(default_factory=list)
    indirect_competitors: List[str] = field(default_factory=list)
    potential_entrants: List[str] = field(default_factory=list)
    suppliers: List[str] = field(default_factory=list)
    customer_segments: List[str] = field(default_factory=list)
    complementors: List[str] = field(default_factory=list)
    
    blue_ocean_potential: BlueOceanPotential = BlueOceanPotential.MEDIUM
    red_ocean_intensity: RedOceanIntensity = RedOceanIntensity.MEDIUM
    terrain_type: str = "hybrid"
    
    position_advantages: List[str] = field(default_factory=list)
    timing_advantages: List[str] = field(default_factory=list)
    information_advantages: List[str] = field(default_factory=list)
    
    force_multipliers: List[str] = field(default_factory=list)
    competitor_weaknesses: List[str] = field(default_factory=list)
    
    def to_dict(self) -> dict:
        return {
            "market_structure": {
                "type": self.market_type,
                "concentration": self.concentration.value,
                "barriers": self.barriers_to_entry
            },
            "actors": {
                "direct_competitors": self.direct_competitors,
                "indirect_competitors": self.indirect_competitors,
                "potential_entrants": self.potential_entrants,
                "suppliers": self.suppliers,
                "customers": self.customer_segments,
                "complementors": self.complementors
            },
            "terrain": {
                "blue_ocean_potential": self.blue_ocean_potential.value,
                "red_ocean_intensity": self.red_ocean_intensity.value,
                "type": self.terrain_type
            },
            "advantages": {
                "position": self.position_advantages,
                "timing": self.timing_advantages,
                "information": self.information_advantages
            },
            "force_multipliers": self.force_multipliers,
            "competitor_weaknesses": self.competitor_weaknesses
        }


class SunTzuFramework:
    """
    Framework 1: Sun Tzu (The Art of War)
    
    Focus: Competitive positioning
    Contribution: Terrain, timing, force multiplication
    Strategic Question: "Where and when to fight?"
    """
    
    @classmethod
    def analyze_terrain(
        cls,
        industry: str,
        competitors: Optional[List[str]] = None,
        market_type: str = "competitive"
    ) -> TerrainAnalysis:
        """Perform terrain analysis."""
        if competitors is None:
            competitors = []
        
        concentration = ConcentrationLevel.MEDIUM
        if len(competitors) <= 3:
            concentration = ConcentrationLevel.HIGH
        elif len(competitors) > 10:
            concentration = ConcentrationLevel.LOW
        
        blue_ocean = BlueOceanPotential.MEDIUM
        red_ocean = RedOceanIntensity.MEDIUM
        
        if len(competitors) > 5:
            red_ocean = RedOceanIntensity.HIGH
            blue_ocean = BlueOceanPotential.LOW
        
        terrain_type = "hybrid"
        if blue_ocean == BlueOceanPotential.HIGH:
            terrain_type = "pure_blue"
        elif red_ocean == RedOceanIntensity.HIGH:
            terrain_type = "pure_red"
        
        return TerrainAnalysis(
            market_type=market_type,
            concentration=concentration,
            barriers_to_entry="moderate",
            direct_competitors=competitors,
            blue_ocean_potential=blue_ocean,
            red_ocean_intensity=red_ocean,
            terrain_type=terrain_type
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for Sun Tzu framework."""
        return """
STEP 1: TERRAIN ANALYSIS (Sun Tzu)
Map the competitive landscape and identify strategic positioning:

COMPETITIVE LANDSCAPE MAPPING:
├─ MARKET STRUCTURE:
│  ├─ Market Type: [Monopoly | Oligopoly | Competitive | Fragmented]
│  ├─ Concentration: [High (top 3 own 70%+) | Medium | Low]
│  └─ Barriers to Entry: [VERY HIGH | HIGH | MODERATE | LOW | MINIMAL]
│
├─ ACTOR IDENTIFICATION:
│  ├─ Direct Competitors: [Top 5 competitors]
│  ├─ Indirect Competitors: [Substitutes, alternatives]
│  ├─ Potential Entrants: [Who could enter?]
│  ├─ Suppliers: [Critical dependencies]
│  ├─ Customers: [Buyer segments]
│  └─ Complementors: [Value enhancers]
│
├─ STRATEGIC TERRAIN:
│  ├─ Blue Ocean Potential: [HIGH | MEDIUM | LOW]
│  ├─ Red Ocean Intensity: [HIGH | MEDIUM | LOW]
│  └─ Terrain Type: [PURE BLUE | HYBRID | PURE RED]
│
└─ STRUCTURAL ADVANTAGES:
   ├─ Position: Market share, geographic, value chain
   ├─ Timing: Market maturity, window of opportunity
   └─ Information: Customer insights, tech understanding
"""
