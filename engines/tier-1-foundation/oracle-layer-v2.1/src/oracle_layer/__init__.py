"""
Oracle Layer v2.1 - Embedded Intelligence Protocol
===================================================

Platform-agnostic cognitive engine that makes ANY AI self-correct,
self-explain, and self-document during execution.

Author: Sheldon K. Salmon (Mr. AION)
License: Apache 2.0
"""

from .core import OracleLayer
from .providers import AIProvider, AIResponse, OpenAIProvider, AnthropicProvider, GenericProvider
from .verification import (
    VerificationResult,
    VerificationStatus,
    ConfidenceScore,
    ReasoningTrace,
    TrinityVerification
)
from .config import OracleConfig, VerificationLevel

__version__ = "2.1.0"
__author__ = "Sheldon K. Salmon"
__codename__ = "PROMETHEUS"

__all__ = [
    "OracleLayer",
    "AIProvider",
    "AIResponse",
    "OpenAIProvider", 
    "AnthropicProvider",
    "GenericProvider",
    "VerificationResult",
    "VerificationStatus",
    "ConfidenceScore",
    "ReasoningTrace",
    "TrinityVerification",
    "OracleConfig",
    "VerificationLevel",
]
