"""
CREDIBILITY ENGINE v2.0 - Module 4: Action Automation
======================================================

Alert-to-playbook mapping and automated responses.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from ..scoring import (
    CredibilityScore, DecayAlert, AlertPriority, CredibilityHealth
)


@dataclass
class Playbook:
    """An automated response playbook."""
    name: str
    trigger_condition: str
    actions: List[str]
    sla_days: int
    expected_outcome: str


@dataclass
class PlaybookExecution:
    """Record of playbook execution."""
    playbook_name: str
    triggered_by: str
    actions_taken: List[str]
    expected_recovery_days: int


class ActionAutomation:
    """
    Module 4: Action Automation & Lifecycle
    
    Maps alerts to playbooks and automates responses.
    """
    
    PLAYBOOKS = {
        "proof_stagnation": Playbook(
            name="Proof Stagnation Recovery",
            trigger_condition="proof_freshness < 50",
            actions=[
                "Create Jira task: '48-hour demo refresh sprint'",
                "Schedule content calendar: 'case study update'",
                "Trigger outreach: 'previous demo attendees invite'",
                "Log expected outcome: 'freshness score target 75'"
            ],
            sla_days=7,
            expected_outcome="Proof freshness score recovers to 75+"
        ),
        "social_momentum_loss": Playbook(
            name="Social Momentum Recovery",
            trigger_condition="social_velocity < 40",
            actions=[
                "Execute testimonial solicitation sequence",
                "Launch mini case study campaign",
                "Schedule amplifier engagement outreach",
                "Create social content calendar burst"
            ],
            sla_days=14,
            expected_outcome="Social momentum recovers to 60+"
        ),
        "critical_decay": Playbook(
            name="Emergency Credibility Recovery",
            trigger_condition="overall_score < 30",
            actions=[
                "Escalate to leadership review",
                "Deploy emergency content refresh",
                "Activate customer success for testimonials",
                "Schedule investor/partner communications"
            ],
            sla_days=3,
            expected_outcome="Stabilize score above critical threshold"
        ),
        "maintenance": Playbook(
            name="Routine Maintenance",
            trigger_condition="health == 'attention'",
            actions=[
                "Review upcoming asset expirations",
                "Queue content refresh tasks",
                "Check social engagement metrics"
            ],
            sla_days=30,
            expected_outcome="Prevent decay to warning level"
        )
    }
    
    @classmethod
    def generate_alert(cls, score: CredibilityScore) -> Optional[DecayAlert]:
        """Generate decay alert based on score."""
        if score.health == CredibilityHealth.HEALTHY:
            return None
        
        if score.health == CredibilityHealth.ATTENTION:
            priority = AlertPriority.SCHEDULE_REFRESH
            message = f"Asset {score.asset_id} needs refresh within 30 days"
            sla = 30
        elif score.health == CredibilityHealth.WARNING:
            priority = AlertPriority.IMMEDIATE_ACTION
            message = f"Asset {score.asset_id} requires immediate action"
            sla = 7
        elif score.health == CredibilityHealth.CRITICAL:
            priority = AlertPriority.EMERGENCY
            message = f"CRITICAL: Asset {score.asset_id} in emergency state"
            sla = 3
        else:
            priority = AlertPriority.REBUILD_REQUIRED
            message = f"Asset {score.asset_id} has expired - rebuild required"
            sla = 14
        
        playbook = cls.select_playbook(score)
        actions = playbook.actions if playbook else ["Review asset manually"]
        
        return DecayAlert(
            asset_id=score.asset_id,
            asset_name=score.asset_id,
            current_score=score.current_score,
            priority=priority,
            message=message,
            recommended_actions=actions,
            sla_days=sla
        )
    
    @classmethod
    def select_playbook(cls, score: CredibilityScore) -> Optional[Playbook]:
        """Select appropriate playbook based on score."""
        if score.current_score < 30:
            return cls.PLAYBOOKS["critical_decay"]
        elif score.current_score < 50:
            return cls.PLAYBOOKS["proof_stagnation"]
        elif score.health == CredibilityHealth.ATTENTION:
            return cls.PLAYBOOKS["maintenance"]
        
        return None
    
    @classmethod
    def execute_playbook(
        cls,
        playbook: Playbook,
        score: CredibilityScore
    ) -> PlaybookExecution:
        """Simulate playbook execution."""
        return PlaybookExecution(
            playbook_name=playbook.name,
            triggered_by=f"Score: {score.current_score:.1f}, Health: {score.health.value}",
            actions_taken=playbook.actions,
            expected_recovery_days=playbook.sla_days
        )
    
    @classmethod
    def get_all_playbooks(cls) -> Dict[str, Playbook]:
        """Get all available playbooks."""
        return cls.PLAYBOOKS.copy()
