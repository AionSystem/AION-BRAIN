"""
CREDIBILITY ENGINE v2.0 - Scoring Systems
===========================================

Credibility scoring, decay models, and evidence tracking.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import math


class AssetType(Enum):
    """Types of credibility assets."""
    LIVE_DEMO = "live_demo"
    CASE_STUDY = "case_study"
    TESTIMONIAL = "testimonial"
    CONFERENCE_TALK = "conference_talk"
    PUBLICATION = "publication"
    OPEN_SOURCE = "open_source"
    CERTIFICATION = "certification"
    PARTNERSHIP = "partnership"


ASSET_HALF_LIVES = {
    AssetType.LIVE_DEMO: 90,
    AssetType.CASE_STUDY: 180,
    AssetType.TESTIMONIAL: 120,
    AssetType.CONFERENCE_TALK: 365,
    AssetType.PUBLICATION: 730,
    AssetType.OPEN_SOURCE: 365,
    AssetType.CERTIFICATION: 365,
    AssetType.PARTNERSHIP: 180,
}


class DecayModel(Enum):
    """Mathematical decay models."""
    EXPONENTIAL = "exponential"
    WEIBULL = "weibull"
    LINEAR = "linear"


class AlertPriority(Enum):
    """Priority levels for decay alerts."""
    MAINTENANCE = "maintenance"
    SCHEDULE_REFRESH = "schedule_refresh"
    IMMEDIATE_ACTION = "immediate_action"
    EMERGENCY = "emergency"
    REBUILD_REQUIRED = "rebuild_required"


class CredibilityHealth(Enum):
    """Health status of credibility."""
    HEALTHY = "healthy"
    ATTENTION = "attention"
    WARNING = "warning"
    CRITICAL = "critical"
    EXPIRED = "expired"


@dataclass
class EvidenceAsset:
    """A credibility evidence asset."""
    asset_id: str
    asset_type: AssetType
    name: str
    created_date: datetime
    last_refresh: datetime
    initial_score: float = 100.0
    verifier_identity: str = ""
    verification_method: str = ""
    source_url: str = ""
    metadata: Dict = field(default_factory=dict)
    
    def days_since_refresh(self) -> float:
        """Calculate days since last refresh."""
        delta = datetime.now() - self.last_refresh
        return delta.total_seconds() / 86400


@dataclass
class CredibilityScore:
    """Complete credibility score for an asset."""
    asset_id: str
    current_score: float
    initial_score: float
    decay_percentage: float
    health: CredibilityHealth
    days_since_refresh: float
    half_life_days: int
    projected_30_day_score: float
    confidence_interval: tuple
    
    def to_dict(self) -> dict:
        return {
            "asset_id": self.asset_id,
            "current_score": round(self.current_score, 2),
            "decay": f"{self.decay_percentage:.1f}%",
            "health": self.health.value,
            "days_since_refresh": round(self.days_since_refresh, 1),
            "projected_30_day": round(self.projected_30_day_score, 2),
            "confidence": f"[{self.confidence_interval[0]:.1f}, {self.confidence_interval[1]:.1f}]"
        }


@dataclass
class DecayAlert:
    """Alert for credibility decay."""
    asset_id: str
    asset_name: str
    current_score: float
    priority: AlertPriority
    message: str
    recommended_actions: List[str]
    sla_days: int = 7
    
    def to_dict(self) -> dict:
        return {
            "asset": self.asset_name,
            "score": round(self.current_score, 2),
            "priority": self.priority.value,
            "message": self.message,
            "actions": self.recommended_actions,
            "sla": f"{self.sla_days} days"
        }


@dataclass
class CompositeScore:
    """Composite credibility score with weighted components."""
    proof_freshness: float
    social_momentum: float
    relevance_index: float
    endorsement_quality: float
    fraud_score: float
    composite: float
    weights: Dict[str, float]
    
    def to_dict(self) -> dict:
        return {
            "proof_freshness": round(self.proof_freshness, 2),
            "social_momentum": round(self.social_momentum, 2),
            "relevance_index": round(self.relevance_index, 2),
            "endorsement_quality": round(self.endorsement_quality, 2),
            "fraud_score": round(self.fraud_score, 2),
            "composite": round(self.composite, 2)
        }


class FraudSignalType(Enum):
    """Types of fraud signals."""
    VELOCITY_ANOMALY = "velocity_anomaly"
    BOT_PATTERN = "bot_pattern"
    FAKE_TESTIMONIAL = "fake_testimonial"
    PURCHASED_ENDORSEMENT = "purchased_endorsement"
    DOMAIN_SPOOFING = "domain_spoofing"


@dataclass
class FraudSignal:
    """A detected fraud signal."""
    signal_type: FraudSignalType
    severity: str
    confidence: float
    description: str
    evidence: List[str]
    
    def to_dict(self) -> dict:
        return {
            "type": self.signal_type.value,
            "severity": self.severity,
            "confidence": f"{self.confidence:.0%}",
            "description": self.description
        }


@dataclass
class ProvenanceRecord:
    """Immutable provenance record for evidence."""
    record_id: str
    asset_id: str
    timestamp: datetime
    source_url: str
    verification_hash: str
    verifier: str
    method: str
    metadata: Dict = field(default_factory=dict)
