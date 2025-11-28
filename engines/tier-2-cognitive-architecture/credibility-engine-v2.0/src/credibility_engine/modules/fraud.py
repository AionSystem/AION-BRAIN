"""
CREDIBILITY ENGINE v2.0 - Module 6: Fraud Detection
====================================================

Manipulation detection and compliance guardrails.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from ..scoring import FraudSignal, FraudSignalType


@dataclass
class AuthenticityCheck:
    """Result of testimonial authenticity check."""
    is_authentic: bool
    confidence: float
    flags: List[str]
    recommendation: str


@dataclass
class VelocityAnomaly:
    """Detected velocity anomaly."""
    metric: str
    expected_range: tuple
    observed_value: float
    deviation_sigma: float
    is_suspicious: bool


@dataclass
class ComplianceStatus:
    """Compliance status for credibility assets."""
    ftc_compliant: bool
    gdpr_compliant: bool
    platform_tos_compliant: bool
    issues: List[str]


class FraudDetection:
    """
    Module 6: Fraud & Security
    
    Detects:
    - Testimonial authenticity issues
    - Velocity anomalies (bot patterns)
    - Source trust scoring
    - Compliance violations
    """
    
    BOT_PATTERNS = [
        "burst_posting",
        "identical_phrasing",
        "new_account_high_activity",
        "suspicious_timing",
        "generic_language"
    ]
    
    @classmethod
    def check_testimonial_authenticity(
        cls,
        account_age_days: int,
        posting_history_count: int,
        has_verification: bool,
        content_uniqueness: float = 0.8
    ) -> AuthenticityCheck:
        """Check if testimonial appears authentic."""
        flags = []
        confidence = 0.9
        
        if account_age_days < 30:
            flags.append("New account")
            confidence -= 0.2
        
        if posting_history_count < 5:
            flags.append("Limited posting history")
            confidence -= 0.15
        
        if not has_verification:
            flags.append("Unverified account")
            confidence -= 0.1
        
        if content_uniqueness < 0.5:
            flags.append("Generic/duplicate content")
            confidence -= 0.25
        
        is_authentic = len(flags) < 2 and confidence > 0.5
        
        if is_authentic:
            recommendation = "Testimonial appears authentic"
        elif confidence > 0.4:
            recommendation = "Additional verification recommended"
        else:
            recommendation = "High fraud risk - manual review required"
        
        return AuthenticityCheck(
            is_authentic=is_authentic,
            confidence=max(0.0, confidence),
            flags=flags,
            recommendation=recommendation
        )
    
    @classmethod
    def detect_velocity_anomaly(
        cls,
        metric_name: str,
        observed_value: float,
        historical_mean: float,
        historical_std: float
    ) -> VelocityAnomaly:
        """Detect velocity anomalies in metrics."""
        if historical_std == 0:
            deviation = 0.0
        else:
            deviation = abs(observed_value - historical_mean) / historical_std
        
        is_suspicious = deviation > 2.5
        
        expected_low = historical_mean - (2 * historical_std)
        expected_high = historical_mean + (2 * historical_std)
        
        return VelocityAnomaly(
            metric=metric_name,
            expected_range=(max(0, expected_low), expected_high),
            observed_value=observed_value,
            deviation_sigma=deviation,
            is_suspicious=is_suspicious
        )
    
    @classmethod
    def calculate_source_trust(
        cls,
        domain_authority: float,
        historical_reliability: float,
        verification_status: bool
    ) -> float:
        """Calculate trust score for a source."""
        base_score = (domain_authority * 0.4 + historical_reliability * 0.4)
        
        if verification_status:
            base_score += 0.2
        
        return min(1.0, max(0.0, base_score))
    
    @classmethod
    def check_compliance(
        cls,
        has_disclosure: bool,
        data_handling: str,
        platform: str
    ) -> ComplianceStatus:
        """Check compliance with regulations and platform ToS."""
        issues = []
        ftc = True
        gdpr = True
        tos = True
        
        if not has_disclosure:
            ftc = False
            issues.append("Missing FTC-required disclosure for endorsement")
        
        if data_handling not in ["encrypted", "anonymized", "consented"]:
            gdpr = False
            issues.append("Data handling may not be GDPR compliant")
        
        if platform in ["unknown", "unverified"]:
            tos = False
            issues.append("Platform terms of service compliance unknown")
        
        return ComplianceStatus(
            ftc_compliant=ftc,
            gdpr_compliant=gdpr,
            platform_tos_compliant=tos,
            issues=issues
        )
    
    @classmethod
    def generate_fraud_signals(
        cls,
        authenticity: AuthenticityCheck,
        anomalies: List[VelocityAnomaly],
        compliance: ComplianceStatus
    ) -> List[FraudSignal]:
        """Generate fraud signals from all checks."""
        signals = []
        
        if not authenticity.is_authentic:
            signals.append(FraudSignal(
                signal_type=FraudSignalType.FAKE_TESTIMONIAL,
                severity="high" if authenticity.confidence < 0.3 else "medium",
                confidence=1.0 - authenticity.confidence,
                description="Testimonial authenticity concerns",
                evidence=authenticity.flags
            ))
        
        for anomaly in anomalies:
            if anomaly.is_suspicious:
                signals.append(FraudSignal(
                    signal_type=FraudSignalType.VELOCITY_ANOMALY,
                    severity="medium",
                    confidence=min(1.0, anomaly.deviation_sigma / 5.0),
                    description=f"Unusual velocity in {anomaly.metric}",
                    evidence=[f"{anomaly.deviation_sigma:.1f}σ deviation from expected"]
                ))
        
        if not compliance.ftc_compliant:
            signals.append(FraudSignal(
                signal_type=FraudSignalType.PURCHASED_ENDORSEMENT,
                severity="high",
                confidence=0.7,
                description="Missing endorsement disclosure",
                evidence=compliance.issues
            ))
        
        return signals
