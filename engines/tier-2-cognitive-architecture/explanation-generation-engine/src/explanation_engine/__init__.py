"""
EXPLANATION ENGINE v1.0
========================

Multi-Level Explanation Generation for AI Outputs.

Translates complex AI analyses into stakeholder-ready narratives
with audience adaptation, counterfactual explanations, and verification.

Author: Sheldon K. Salmon
License: Apache 2.0
"""

from .core import ExplanationEngine
from .config import ExplanationConfig, AudienceLevel, ExplanationStyle
from .types import (
    Explanation, ExplanationLayer, CounterfactualExplanation,
    AudienceProfile, VerificationResult, ExplanationQuality
)
from .generators import (
    MultiLevelGenerator,
    CounterfactualGenerator,
    AudienceAdapter,
    ExplanationVerifier
)

__version__ = "1.0.0"
__author__ = "Sheldon K. Salmon"
__codename__ = "CLARITAS"

__all__ = [
    "ExplanationEngine",
    "ExplanationConfig",
    "AudienceLevel",
    "ExplanationStyle",
    "Explanation",
    "ExplanationLayer",
    "CounterfactualExplanation",
    "AudienceProfile",
    "VerificationResult",
    "ExplanationQuality",
    "MultiLevelGenerator",
    "CounterfactualGenerator",
    "AudienceAdapter",
    "ExplanationVerifier",
]
