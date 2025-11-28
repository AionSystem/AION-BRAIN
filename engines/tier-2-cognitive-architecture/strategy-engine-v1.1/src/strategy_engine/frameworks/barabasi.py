"""
STRATEGY ENGINE v1.1 - Framework 3: Barabási
=============================================

Network dynamics and preferential attachment.
"How do networks amplify advantage?"
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class NetworkTopology(Enum):
    """Types of network topology."""
    HUB_AND_SPOKE = "hub_and_spoke"
    MESH = "mesh"
    HIERARCHICAL = "hierarchical"
    SCALE_FREE = "scale_free"


@dataclass
class NetworkHub:
    """A hub node in the network."""
    name: str
    connection_count: int = 0
    influence_score: float = 0.0
    is_target: bool = False


@dataclass
class TippingPoint:
    """A network tipping point analysis."""
    trigger_adoption_percent: float
    current_adoption_percent: float
    distance_to_tipping: float
    cascade_likelihood: str = "medium"
    
    @property
    def is_near_tipping(self) -> bool:
        return self.distance_to_tipping < 10.0


@dataclass
class NetworkDynamics:
    """Complete network dynamics analysis."""
    topology: NetworkTopology
    key_hubs: List[str]
    bridges: List[str]
    periphery_opportunities: List[str]
    tipping_point: Optional[TippingPoint] = None
    preferential_attachment: bool = False
    clustering_coefficient: str = "medium"
    network_resilience: str = "medium"
    hub_strategy: str = ""
    
    def to_dict(self) -> dict:
        return {
            "topology": self.topology.value,
            "key_hubs": self.key_hubs,
            "bridges": self.bridges,
            "periphery": self.periphery_opportunities,
            "tipping_point": {
                "trigger": self.tipping_point.trigger_adoption_percent,
                "current": self.tipping_point.current_adoption_percent,
                "near": self.tipping_point.is_near_tipping
            } if self.tipping_point else None,
            "preferential_attachment": self.preferential_attachment,
            "hub_strategy": self.hub_strategy
        }


class BarabasiFramework:
    """
    Framework 3: Barabási (Network Science)
    
    Focus: Network dynamics
    Contribution: Hubs, tipping points, preferential attachment
    Strategic Question: "How do networks amplify advantage?"
    """
    
    @classmethod
    def analyze_network(
        cls,
        market_description: str,
        current_adoption: float = 5.0,
        key_players: Optional[List[str]] = None
    ) -> NetworkDynamics:
        """Analyze network dynamics."""
        if key_players is None:
            key_players = []
        
        topology = NetworkTopology.SCALE_FREE
        if "platform" in market_description.lower():
            topology = NetworkTopology.HUB_AND_SPOKE
        elif "enterprise" in market_description.lower():
            topology = NetworkTopology.HIERARCHICAL
        
        trigger = 15.0
        if "b2b" in market_description.lower():
            trigger = 20.0
        elif "consumer" in market_description.lower():
            trigger = 10.0
        
        tipping = TippingPoint(
            trigger_adoption_percent=trigger,
            current_adoption_percent=current_adoption,
            distance_to_tipping=trigger - current_adoption,
            cascade_likelihood="high" if current_adoption > trigger * 0.7 else "medium"
        )
        
        has_preferential = "network" in market_description.lower() or "platform" in market_description.lower()
        
        hub_strategy = "Cultivate key hubs through partnerships"
        if has_preferential:
            hub_strategy = "Accelerate preferential attachment through early hub wins"
        
        return NetworkDynamics(
            topology=topology,
            key_hubs=key_players[:3] if key_players else [],
            bridges=[],
            periphery_opportunities=[],
            tipping_point=tipping,
            preferential_attachment=has_preferential,
            clustering_coefficient="medium",
            network_resilience="medium",
            hub_strategy=hub_strategy
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for Barabási framework."""
        return """
STEP 3: NETWORK DYNAMICS (Barabási)
Map network effects, hubs, and tipping points:

NETWORK TOPOLOGY ANALYSIS:
├─ Network Type: [Hub-and-spoke | Mesh | Hierarchical | Scale-free]
├─ Key Hubs: [High-connection nodes to target]
├─ Bridges: [Nodes connecting different clusters]
└─ Periphery: [Low-connection nodes with potential]

NETWORK DYNAMICS:
├─ Preferential Attachment: [Do popular nodes get more popular?]
├─ Tipping Point Analysis: [What adoption % triggers cascade?]
├─ Clustering Coefficient: [How connected are neighbors?]
└─ Network Resilience: [How fragile is the network?]

STRATEGIC NETWORK QUESTIONS:
├─ "Who are the hubs we must win?"
├─ "What's our path to tipping point?"
├─ "Can we create preferential attachment?"
└─ "How do we become the hub?"
"""
