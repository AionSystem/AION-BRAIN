"""
BENCHMARK FRESHNESS - Credibility Engine Integration
=====================================================

Integrates Credibility Engine's decay mathematics for tracking
benchmark result validity over time.

Key Concepts:
- Benchmark results decay in validity as models update and domains shift
- Domain-specific half-lives (medical faster than general)
- Freshness scores trigger re-validation alerts
- Certificates include expiry dates

Author: Sheldon K. Salmon
Integration: Credibility Engine v2.0 (VERITAS)
"""

import math
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta


class DecayModel(Enum):
    """Mathematical decay models for freshness calculation."""
    EXPONENTIAL = "exponential"
    WEIBULL = "weibull"
    LINEAR = "linear"


class ValidityStatus(Enum):
    """Benchmark validity status levels."""
    FRESH = "fresh"
    VALID = "valid"
    AGING = "aging"
    STALE = "stale"
    EXPIRED = "expired"


DOMAIN_HALF_LIVES = {
    "medical": 90,
    "legal": 180,
    "financial": 120,
    "security": 60,
    "regulatory": 150,
    "research": 365,
    "general": 270,
}

VALIDITY_THRESHOLDS = {
    ValidityStatus.FRESH: 90,
    ValidityStatus.VALID: 70,
    ValidityStatus.AGING: 50,
    ValidityStatus.STALE: 30,
    ValidityStatus.EXPIRED: 0,
}


@dataclass
class FreshnessScore:
    """Freshness score for a benchmark result."""
    benchmark_id: str
    domain: str
    original_score: float
    current_freshness: float
    validity_status: ValidityStatus
    benchmark_date: datetime
    calculated_date: datetime
    half_life_days: int
    days_since_benchmark: int
    decay_model: DecayModel
    recommended_revalidation_date: datetime
    confidence_decay: float
    
    @property
    def freshness_percentage(self) -> float:
        """Freshness as percentage (0-100)."""
        return self.current_freshness * 100
    
    @property
    def is_valid(self) -> bool:
        """Check if benchmark is still valid for use."""
        return self.validity_status not in [ValidityStatus.STALE, ValidityStatus.EXPIRED]
    
    @property
    def days_until_stale(self) -> int:
        """Days until benchmark becomes stale."""
        threshold = VALIDITY_THRESHOLDS[ValidityStatus.STALE]
        if self.freshness_percentage <= threshold:
            return 0
        target_freshness = threshold / 100
        t = -self.half_life_days * math.log(target_freshness) / math.log(2)
        return max(0, int(t - self.days_since_benchmark))


@dataclass
class RevalidationAlert:
    """Alert for benchmarks needing re-validation."""
    benchmark_id: str
    domain: str
    current_freshness: float
    validity_status: ValidityStatus
    urgency: str
    message: str
    recommended_action: str
    days_until_expiry: int


class BenchmarkFreshness:
    """
    Benchmark Freshness System - Time-Decay Validity Tracking.
    
    Integrates Credibility Engine's decay mathematics to track
    when benchmark results need re-validation.
    
    Features:
    - Domain-specific decay rates (medical faster than general)
    - Multiple decay models (exponential, Weibull, linear)
    - Automatic revalidation alerts
    - Certificate expiry tracking
    
    Usage:
        freshness = BenchmarkFreshness()
        score = freshness.calculate_freshness(
            benchmark_id="BM-2024-001",
            domain="medical",
            benchmark_date=datetime(2024, 6, 1)
        )
    """
    
    VERSION = "2.0.0"
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize Benchmark Freshness system."""
        self.config = config or {}
        self._cache: Dict[str, FreshnessScore] = {}
        self._alerts: List[RevalidationAlert] = []
    
    def calculate_freshness(
        self,
        benchmark_id: str,
        domain: str,
        benchmark_date: datetime,
        original_score: float = 100.0,
        model: DecayModel = DecayModel.EXPONENTIAL,
        custom_half_life: Optional[int] = None
    ) -> FreshnessScore:
        """
        Calculate current freshness of a benchmark result.
        
        Args:
            benchmark_id: Unique identifier for the benchmark
            domain: Domain of the benchmark (medical, legal, etc.)
            benchmark_date: When the benchmark was conducted
            original_score: Original benchmark score (0-100)
            model: Decay model to use
            custom_half_life: Override domain default half-life
            
        Returns:
            FreshnessScore with validity status and recommendations
        """
        now = datetime.now()
        days_elapsed = (now - benchmark_date).days
        
        half_life = custom_half_life or DOMAIN_HALF_LIVES.get(domain, 270)
        
        if model == DecayModel.EXPONENTIAL:
            freshness = self._exponential_decay(days_elapsed, half_life)
        elif model == DecayModel.WEIBULL:
            freshness = self._weibull_decay(days_elapsed, half_life)
        else:
            freshness = self._linear_decay(days_elapsed, half_life)
        
        status = self._determine_validity_status(freshness * 100)
        
        confidence_decay = 1 - freshness
        
        revalidation_date = self._calculate_revalidation_date(
            benchmark_date, half_life, status
        )
        
        score = FreshnessScore(
            benchmark_id=benchmark_id,
            domain=domain,
            original_score=original_score,
            current_freshness=freshness,
            validity_status=status,
            benchmark_date=benchmark_date,
            calculated_date=now,
            half_life_days=half_life,
            days_since_benchmark=days_elapsed,
            decay_model=model,
            recommended_revalidation_date=revalidation_date,
            confidence_decay=confidence_decay
        )
        
        self._cache[benchmark_id] = score
        
        return score
    
    def calculate_batch_freshness(
        self,
        benchmarks: List[Dict[str, Any]]
    ) -> List[FreshnessScore]:
        """
        Calculate freshness for multiple benchmarks.
        
        Args:
            benchmarks: List of benchmark configs with id, domain, date
            
        Returns:
            List of FreshnessScores
        """
        return [
            self.calculate_freshness(
                benchmark_id=bm["id"],
                domain=bm["domain"],
                benchmark_date=bm["date"],
                original_score=bm.get("score", 100.0)
            )
            for bm in benchmarks
        ]
    
    def generate_alerts(
        self,
        freshness_scores: Optional[List[FreshnessScore]] = None
    ) -> List[RevalidationAlert]:
        """
        Generate revalidation alerts for aging benchmarks.
        
        Args:
            freshness_scores: Optional list (uses cache if not provided)
            
        Returns:
            List of RevalidationAlerts sorted by urgency
        """
        scores = freshness_scores or list(self._cache.values())
        alerts = []
        
        for score in scores:
            if score.validity_status in [ValidityStatus.AGING, ValidityStatus.STALE]:
                urgency, message, action = self._generate_alert_content(score)
                
                alert = RevalidationAlert(
                    benchmark_id=score.benchmark_id,
                    domain=score.domain,
                    current_freshness=score.current_freshness,
                    validity_status=score.validity_status,
                    urgency=urgency,
                    message=message,
                    recommended_action=action,
                    days_until_expiry=score.days_until_stale
                )
                alerts.append(alert)
        
        urgency_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
        return sorted(alerts, key=lambda a: urgency_order.get(a.urgency, 4))
    
    def get_certificate_expiry(
        self,
        benchmark_date: datetime,
        domain: str,
        target_validity: ValidityStatus = ValidityStatus.VALID
    ) -> datetime:
        """
        Calculate when a benchmark certificate expires.
        
        Args:
            benchmark_date: When benchmark was conducted
            domain: Benchmark domain
            target_validity: Minimum validity level for certificate
            
        Returns:
            Expiry datetime
        """
        half_life = DOMAIN_HALF_LIVES.get(domain, 270)
        threshold = VALIDITY_THRESHOLDS[target_validity] / 100
        
        t = -half_life * math.log(threshold) / math.log(2)
        
        return benchmark_date + timedelta(days=int(t))
    
    def _exponential_decay(self, days: int, half_life: int) -> float:
        """Exponential decay model: N(t) = N0 * (1/2)^(t/t_half)."""
        return 0.5 ** (days / half_life)
    
    def _weibull_decay(self, days: int, half_life: int, k: float = 1.5) -> float:
        """Weibull decay model: N(t) = exp(-(t/λ)^k)."""
        lambda_param = half_life / (math.log(2) ** (1/k))
        return math.exp(-((days / lambda_param) ** k))
    
    def _linear_decay(self, days: int, half_life: int) -> float:
        """Linear decay model: N(t) = max(0, 1 - t/(2*t_half))."""
        return max(0.0, 1.0 - days / (2 * half_life))
    
    def _determine_validity_status(self, freshness_pct: float) -> ValidityStatus:
        """Determine validity status from freshness percentage."""
        if freshness_pct >= VALIDITY_THRESHOLDS[ValidityStatus.FRESH]:
            return ValidityStatus.FRESH
        elif freshness_pct >= VALIDITY_THRESHOLDS[ValidityStatus.VALID]:
            return ValidityStatus.VALID
        elif freshness_pct >= VALIDITY_THRESHOLDS[ValidityStatus.AGING]:
            return ValidityStatus.AGING
        elif freshness_pct >= VALIDITY_THRESHOLDS[ValidityStatus.STALE]:
            return ValidityStatus.STALE
        else:
            return ValidityStatus.EXPIRED
    
    def _calculate_revalidation_date(
        self,
        benchmark_date: datetime,
        half_life: int,
        current_status: ValidityStatus
    ) -> datetime:
        """Calculate recommended revalidation date."""
        if current_status == ValidityStatus.EXPIRED:
            return datetime.now()
        elif current_status == ValidityStatus.STALE:
            return datetime.now() + timedelta(days=7)
        elif current_status == ValidityStatus.AGING:
            return datetime.now() + timedelta(days=30)
        else:
            t = -half_life * math.log(0.7) / math.log(2)
            return benchmark_date + timedelta(days=int(t))
    
    def _generate_alert_content(
        self,
        score: FreshnessScore
    ) -> tuple:
        """Generate alert content based on freshness score."""
        if score.validity_status == ValidityStatus.STALE:
            return (
                "CRITICAL",
                f"Benchmark {score.benchmark_id} is STALE ({score.freshness_percentage:.1f}% fresh)",
                "Immediate revalidation required before using results"
            )
        elif score.freshness_percentage < 60:
            return (
                "HIGH",
                f"Benchmark {score.benchmark_id} is AGING ({score.freshness_percentage:.1f}% fresh)",
                f"Schedule revalidation within {score.days_until_stale} days"
            )
        else:
            return (
                "MEDIUM",
                f"Benchmark {score.benchmark_id} approaching aging threshold",
                "Plan for revalidation in next quarter"
            )
    
    def format_freshness_report(self, score: FreshnessScore) -> str:
        """Format a freshness score as a report."""
        status_emoji = {
            ValidityStatus.FRESH: "🟢",
            ValidityStatus.VALID: "🟢",
            ValidityStatus.AGING: "🟡",
            ValidityStatus.STALE: "🟠",
            ValidityStatus.EXPIRED: "🔴",
        }
        
        return f"""
BENCHMARK FRESHNESS REPORT
{'=' * 50}
Benchmark ID: {score.benchmark_id}
Domain: {score.domain.upper()}
Status: {status_emoji.get(score.validity_status, '⚪')} {score.validity_status.value.upper()}

FRESHNESS METRICS
{'─' * 50}
Current Freshness: {score.freshness_percentage:.1f}%
Original Score: {score.original_score:.1f}
Days Since Benchmark: {score.days_since_benchmark}
Half-Life: {score.half_life_days} days
Decay Model: {score.decay_model.value}

VALIDITY
{'─' * 50}
Still Valid: {'Yes' if score.is_valid else 'No'}
Days Until Stale: {score.days_until_stale}
Confidence Decay: {score.confidence_decay * 100:.1f}%

RECOMMENDATIONS
{'─' * 50}
Revalidation Date: {score.recommended_revalidation_date.strftime('%Y-%m-%d')}
"""
