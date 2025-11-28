"""
CREDIBILITY ENGINE v2.0 - Modules
==================================

Specialized modules for credibility analysis.
"""

from .decay_math import DecayMathematics
from .signals import SignalInstrumentation
from .explainability import ExplainabilityEngine
from .automation import ActionAutomation
from .fraud import FraudDetection
from .provenance import ProvenanceSystem

__all__ = [
    "DecayMathematics",
    "SignalInstrumentation",
    "ExplainabilityEngine",
    "ActionAutomation",
    "FraudDetection",
    "ProvenanceSystem",
]
