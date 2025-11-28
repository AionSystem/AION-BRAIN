"""
Oracle Layer Configuration
==========================

Configuration classes for Oracle Layer behavior and verification levels.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, List


class VerificationLevel(Enum):
    """Verification intensity levels."""
    MINIMAL = "minimal"
    STANDARD = "standard"
    FULL = "full"
    MAXIMUM = "maximum"


@dataclass
class OracleConfig:
    """
    Configuration for Oracle Layer behavior.
    
    Attributes:
        confidence_threshold: Minimum confidence required (0.0-1.0)
        verification_level: How thorough verification should be
        enable_trinity: Enable Advocate/Skeptic/Arbiter cross-validation
        enable_reasoning_traces: Show step-by-step reasoning
        enable_uncertainty_quantification: Show confidence intervals
        enable_chain_of_custody: Create audit trail
        enable_self_monitoring: Enable recursive self-checking
        max_verify_required_tags: Max uncertain claims before fail_response
        attribution_enabled: Include AION-BRAIN footer
        domain: Optional domain specialization (legal, medical, research)
    """
    confidence_threshold: float = 0.80
    verification_level: VerificationLevel = VerificationLevel.STANDARD
    enable_trinity: bool = True
    enable_reasoning_traces: bool = True
    enable_uncertainty_quantification: bool = True
    enable_chain_of_custody: bool = False
    enable_self_monitoring: bool = True
    max_verify_required_tags: int = 3
    attribution_enabled: bool = True
    domain: Optional[str] = None
    custom_fail_response: Optional[str] = None
    
    def __post_init__(self):
        if not 0.0 <= self.confidence_threshold <= 1.0:
            raise ValueError("confidence_threshold must be between 0.0 and 1.0")
    
    @classmethod
    def minimal(cls) -> "OracleConfig":
        """Minimal configuration for efficiency."""
        return cls(
            verification_level=VerificationLevel.MINIMAL,
            enable_trinity=False,
            enable_reasoning_traces=False,
            enable_uncertainty_quantification=False,
            enable_chain_of_custody=False,
            enable_self_monitoring=False,
        )
    
    @classmethod
    def standard(cls) -> "OracleConfig":
        """Standard configuration for general use."""
        return cls(
            verification_level=VerificationLevel.STANDARD,
            enable_trinity=False,
            enable_reasoning_traces=True,
            enable_uncertainty_quantification=True,
            enable_chain_of_custody=False,
            enable_self_monitoring=True,
        )
    
    @classmethod
    def full(cls) -> "OracleConfig":
        """Full configuration for high-stakes content."""
        return cls(
            verification_level=VerificationLevel.FULL,
            enable_trinity=True,
            enable_reasoning_traces=True,
            enable_uncertainty_quantification=True,
            enable_chain_of_custody=True,
            enable_self_monitoring=True,
        )
    
    @classmethod
    def medical(cls) -> "OracleConfig":
        """Pre-configured for medical domain."""
        config = cls.full()
        config.domain = "medical"
        config.confidence_threshold = 0.90
        config.custom_fail_response = (
            "MEDICAL SAFETY FLAG: This query requires verification by a "
            "licensed healthcare professional before any clinical application."
        )
        return config
    
    @classmethod
    def legal(cls) -> "OracleConfig":
        """Pre-configured for legal domain."""
        config = cls.full()
        config.domain = "legal"
        config.confidence_threshold = 0.85
        config.custom_fail_response = (
            "LEGAL DISCLAIMER: This information is for educational purposes only "
            "and does not constitute legal advice. Consult a licensed attorney."
        )
        return config
    
    @classmethod
    def research(cls) -> "OracleConfig":
        """Pre-configured for research domain."""
        config = cls.standard()
        config.domain = "research"
        config.confidence_threshold = 0.75
        return config
