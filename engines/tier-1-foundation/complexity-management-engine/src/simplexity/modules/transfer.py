"""
SIMPLEXITY v2.0 - Module 7: Complexity Transfer Detection
==========================================================

Detect when simplification moves complexity elsewhere.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from ..scoring import TransferScore


@dataclass
class TransferDestination:
    """Where complexity was transferred to."""
    area: str
    description: str
    new_complexity_estimate: float
    hidden_costs: List[str] = field(default_factory=list)


@dataclass
class TransferAnalysis:
    """Complete transfer analysis result."""
    source_area: str
    original_complexity: float
    simplified_complexity: float
    destinations: List[TransferDestination]
    transfer_score: TransferScore
    net_system_change: float
    warnings: List[str] = field(default_factory=list)
    recommendations: List[str] = field(default_factory=list)
    
    @property
    def is_true_simplification(self) -> bool:
        return self.transfer_score.score < 3.0


class TransferModule:
    """
    Module 7: Complexity Transfer Detection (NEW in v2.0)
    
    The Balloon Squeeze Effect:
    When you squeeze a balloon in one place, it bulges elsewhere.
    Simplification that moves complexity isn't simplification.
    
    Common Transfer Destinations:
    - Code architecture → Deployment/operations
    - User interface → Backend logic
    - Central system → End user
    - Software → Documentation/training
    - Current team → Future maintainers
    
    Transfer Score 0-10:
    - 0: True elimination
    - 5: Partial transfer
    - 10: Total transfer (complexity just relocated)
    """
    
    COMMON_TRANSFERS = {
        "code_architecture": ["deployment", "operations", "configuration"],
        "user_interface": ["backend_logic", "api", "database"],
        "central_system": ["end_user", "client", "edge"],
        "software": ["documentation", "training", "support"],
        "current_team": ["future_maintainers", "operations", "support"]
    }
    
    @classmethod
    def detect_transfer(
        cls,
        source_area: str,
        original_complexity: float,
        simplified_complexity: float,
        destinations: Optional[List[TransferDestination]] = None
    ) -> TransferAnalysis:
        """Detect and analyze complexity transfer."""
        if destinations is None:
            destinations = []
        
        apparent_reduction = original_complexity - simplified_complexity
        
        total_transferred = sum(d.new_complexity_estimate for d in destinations)
        
        if apparent_reduction > 0:
            transfer_ratio = total_transferred / apparent_reduction
        else:
            transfer_ratio = 0.0
        
        transfer_score_value = min(10.0, transfer_ratio * 10)
        
        hidden_costs = []
        for dest in destinations:
            hidden_costs.extend(dest.hidden_costs)
        
        transfer_score = TransferScore(
            score=transfer_score_value,
            source_area=source_area,
            destination_areas=[d.area for d in destinations],
            hidden_costs=hidden_costs,
            rationale=f"Transfer ratio: {transfer_ratio:.2f}"
        )
        
        net_change = simplified_complexity + total_transferred - original_complexity
        
        warnings = []
        if transfer_score_value > 6:
            warnings.append("TRANSFER WARNING: Complexity relocated, not eliminated")
        
        recommendations = []
        if transfer_score_value > 3:
            recommendations.append("Investigate transfer destinations for optimization")
        if hidden_costs:
            recommendations.append(f"Address hidden costs: {', '.join(hidden_costs[:3])}")
        
        return TransferAnalysis(
            source_area=source_area,
            original_complexity=original_complexity,
            simplified_complexity=simplified_complexity,
            destinations=destinations,
            transfer_score=transfer_score,
            net_system_change=net_change,
            warnings=warnings,
            recommendations=recommendations
        )
    
    @classmethod
    def suggest_destinations(cls, source_area: str) -> List[str]:
        """Suggest likely transfer destinations for a source area."""
        for key, destinations in cls.COMMON_TRANSFERS.items():
            if key in source_area.lower():
                return destinations
        return ["downstream_systems", "operations", "end_users"]
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for transfer module."""
        return """
MODULE 7: COMPLEXITY TRANSFER DETECTION
Detect when simplification moves complexity elsewhere (balloon squeeze):
- Scan boundaries of simplified area
- Audit new interfaces created
- Trace responsibility shifts
- Search for hidden costs and workarounds
- Assess downstream impact

COMMON TRANSFER DESTINATIONS:
- Code architecture → Deployment/operations
- User interface → Backend logic
- Central system → End user
- Software → Documentation/training
- Current team → Future maintainers

TRANSFER SCORE: 0 (true elimination) to 10 (total transfer)
├─ 0-2: True simplification
├─ 3-4: Mostly eliminated, minor transfer
├─ 5-6: Partial transfer - monitor
├─ 7-8: Significant transfer - complexity relocated
└─ 9-10: Total transfer - no net reduction
"""
