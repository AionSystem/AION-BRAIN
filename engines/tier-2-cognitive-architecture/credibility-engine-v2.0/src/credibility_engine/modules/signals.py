"""
CREDIBILITY ENGINE v2.0 - Module 2: Signal Instrumentation
===========================================================

Data source integration and signal processing.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime
from ..scoring import CompositeScore


@dataclass
class DataSignal:
    """A single data signal."""
    source: str
    metric: str
    value: float
    timestamp: datetime
    reliability: float = 0.85
    normalized: bool = False


@dataclass
class SignalBundle:
    """Bundle of related signals."""
    category: str
    signals: List[DataSignal]
    composite_value: float
    last_updated: datetime


class SignalInstrumentation:
    """
    Module 2: Signal Instrumentation & Data Sources
    
    Aggregates signals from multiple sources:
    - Search volume (Google Trends)
    - Social velocity (Twitter, LinkedIn, Reddit)
    - Proof engagement (GitHub, demos, CRM)
    """
    
    WEIGHTS = {
        "proof_freshness": 0.30,
        "social_momentum": 0.25,
        "relevance_index": 0.20,
        "endorsement_quality": 0.15,
        "fraud_score": 0.10
    }
    
    @classmethod
    def normalize_signal(cls, value: float, baseline: float = 50.0) -> float:
        """Normalize signal using z-score relative to baseline."""
        if baseline == 0:
            return value
        return ((value - baseline) / baseline) * 100 + 50
    
    @classmethod
    def calculate_proof_freshness(
        cls,
        days_since_demo: int = 30,
        days_since_case_study: int = 60,
        days_since_testimonial: int = 45
    ) -> float:
        """Calculate proof freshness score."""
        demo_score = max(0, 100 - (days_since_demo * 1.1))
        case_score = max(0, 100 - (days_since_case_study * 0.55))
        testimonial_score = max(0, 100 - (days_since_testimonial * 0.83))
        
        return (demo_score * 0.5 + case_score * 0.3 + testimonial_score * 0.2)
    
    @classmethod
    def calculate_social_momentum(
        cls,
        mention_velocity: float = 10.0,
        sentiment_trend: float = 0.6,
        amplification_rate: float = 2.0
    ) -> float:
        """Calculate social momentum score."""
        velocity_score = min(100, mention_velocity * 5)
        sentiment_score = sentiment_trend * 100
        amp_score = min(100, amplification_rate * 25)
        
        return (velocity_score * 0.4 + sentiment_score * 0.35 + amp_score * 0.25)
    
    @classmethod
    def calculate_relevance_index(
        cls,
        search_volume_trend: float = 0.0,
        market_alignment: float = 0.7,
        competitor_comparison: float = 0.5
    ) -> float:
        """Calculate relevance index."""
        trend_score = 50 + (search_volume_trend * 50)
        alignment_score = market_alignment * 100
        comp_score = competitor_comparison * 100
        
        return (trend_score * 0.3 + alignment_score * 0.4 + comp_score * 0.3)
    
    @classmethod
    def calculate_endorsement_quality(
        cls,
        endorser_authority: float = 0.7,
        endorsement_recency_days: int = 30,
        endorsement_specificity: float = 0.8
    ) -> float:
        """Calculate endorsement quality score."""
        authority_score = endorser_authority * 100
        recency_score = max(0, 100 - (endorsement_recency_days * 1.0))
        specificity_score = endorsement_specificity * 100
        
        return (authority_score * 0.4 + recency_score * 0.3 + specificity_score * 0.3)
    
    @classmethod
    def calculate_fraud_penalty(
        cls,
        bot_signals: int = 0,
        velocity_anomalies: int = 0,
        fake_indicators: int = 0
    ) -> float:
        """Calculate fraud penalty (higher = less fraud = better)."""
        total_signals = bot_signals + velocity_anomalies + fake_indicators
        
        if total_signals == 0:
            return 100.0
        elif total_signals <= 2:
            return 80.0
        elif total_signals <= 5:
            return 50.0
        else:
            return max(0, 100 - (total_signals * 10))
    
    @classmethod
    def calculate_composite(
        cls,
        proof_freshness: float,
        social_momentum: float,
        relevance_index: float,
        endorsement_quality: float,
        fraud_score: float
    ) -> CompositeScore:
        """Calculate weighted composite credibility score."""
        composite = (
            proof_freshness * cls.WEIGHTS["proof_freshness"] +
            social_momentum * cls.WEIGHTS["social_momentum"] +
            relevance_index * cls.WEIGHTS["relevance_index"] +
            endorsement_quality * cls.WEIGHTS["endorsement_quality"] +
            fraud_score * cls.WEIGHTS["fraud_score"]
        )
        
        return CompositeScore(
            proof_freshness=proof_freshness,
            social_momentum=social_momentum,
            relevance_index=relevance_index,
            endorsement_quality=endorsement_quality,
            fraud_score=fraud_score,
            composite=composite,
            weights=cls.WEIGHTS
        )
    
    @classmethod
    def quick_composite(cls) -> CompositeScore:
        """Calculate quick composite with default values."""
        return cls.calculate_composite(
            proof_freshness=cls.calculate_proof_freshness(),
            social_momentum=cls.calculate_social_momentum(),
            relevance_index=cls.calculate_relevance_index(),
            endorsement_quality=cls.calculate_endorsement_quality(),
            fraud_score=cls.calculate_fraud_penalty()
        )
