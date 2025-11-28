"""
CREDIBILITY ENGINE v2.0 - Configuration
=========================================

Configuration options for the Credibility Engine.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List, Dict


class AnalysisMode(Enum):
    """Analysis modes for Credibility Engine."""
    QUICK = "quick"
    STANDARD = "standard"
    ENTERPRISE = "enterprise"


@dataclass
class DecaySettings:
    """Settings for decay calculations."""
    use_exponential: bool = True
    use_weibull: bool = False
    default_half_life_days: int = 90
    recency_weight: float = 0.30
    social_weight: float = 0.25
    relevance_weight: float = 0.20
    endorsement_weight: float = 0.15
    fraud_weight: float = 0.10


@dataclass
class AlertThresholds:
    """Thresholds for decay alerts."""
    healthy_min: int = 80
    attention_min: int = 60
    warning_min: int = 40
    critical_min: int = 20


@dataclass
class CredibilityConfig:
    """
    Configuration for Credibility Engine.
    
    Attributes:
        mode: Analysis mode
        decay_settings: Decay calculation settings
        alert_thresholds: Alert triggering thresholds
        enable_fraud_detection: Include fraud analysis
        enable_provenance: Track evidence provenance
    """
    mode: AnalysisMode = AnalysisMode.STANDARD
    decay_settings: DecaySettings = field(default_factory=DecaySettings)
    alert_thresholds: AlertThresholds = field(default_factory=AlertThresholds)
    enable_fraud_detection: bool = True
    enable_provenance: bool = True
    enable_action_automation: bool = True
    
    @classmethod
    def quick(cls) -> "CredibilityConfig":
        """Quick credibility check."""
        return cls(
            mode=AnalysisMode.QUICK,
            enable_fraud_detection=False,
            enable_action_automation=False
        )
    
    @classmethod
    def standard(cls) -> "CredibilityConfig":
        """Standard credibility analysis."""
        return cls(mode=AnalysisMode.STANDARD)
    
    @classmethod
    def enterprise(cls) -> "CredibilityConfig":
        """Enterprise-grade credibility analysis."""
        return cls(
            mode=AnalysisMode.ENTERPRISE,
            enable_fraud_detection=True,
            enable_provenance=True,
            enable_action_automation=True
        )
