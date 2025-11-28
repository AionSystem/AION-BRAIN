"""
CREDIBILITY ENGINE v2.0
========================

Trust Acceleration System with Mathematical Rigor.

The complete system for:
- Evidence scoring and decay tracking
- Source validation
- Trust metrics across all cognitive outputs

Author: Sheldon K. Salmon
License: Apache 2.0
"""

from .core import CredibilityEngine
from .config import CredibilityConfig
from .scoring import (
    CredibilityScore, AssetType, DecayModel,
    EvidenceAsset, DecayAlert, AlertPriority,
    CredibilityHealth, FraudSignal
)
from .modules import (
    DecayMathematics,
    SignalInstrumentation,
    ExplainabilityEngine,
    ActionAutomation,
    FraudDetection,
    ProvenanceSystem
)
from .analysis import CredibilityAnalysis, CredibilityReport

__version__ = "2.0.0"
__author__ = "Sheldon K. Salmon"
__codename__ = "VERITAS"

__all__ = [
    "CredibilityEngine",
    "CredibilityConfig",
    "CredibilityScore",
    "AssetType",
    "DecayModel",
    "EvidenceAsset",
    "DecayAlert",
    "AlertPriority",
    "CredibilityHealth",
    "FraudSignal",
    "DecayMathematics",
    "SignalInstrumentation",
    "ExplainabilityEngine",
    "ActionAutomation",
    "FraudDetection",
    "ProvenanceSystem",
    "CredibilityAnalysis",
    "CredibilityReport",
]
