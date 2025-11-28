"""
CREDIBILITY ENGINE v2.0 - Module 1: Formal Decay Mathematics
=============================================================

Exponential and Weibull decay models with confidence intervals.
"""

import math
from typing import Tuple, Optional
from datetime import datetime, timedelta
from ..scoring import (
    EvidenceAsset, CredibilityScore, CredibilityHealth,
    AssetType, ASSET_HALF_LIVES, DecayModel
)


class DecayMathematics:
    """
    Module 1: Formal Decay Mathematics
    
    Implements:
    - Exponential decay: score(t) = S₀ × exp(-ln(2) × t / T_half)
    - Weibull distribution: score(t) = S₀ × exp(-(t/λ)^k)
    - Bootstrap confidence intervals
    """
    
    @classmethod
    def exponential_decay(
        cls,
        initial_score: float,
        days_elapsed: float,
        half_life_days: int
    ) -> float:
        """
        Calculate exponentially decayed score.
        
        Formula: S(t) = S₀ × exp(-ln(2) × t / T_half)
        """
        if days_elapsed <= 0:
            return initial_score
        
        decay_constant = math.log(2) / half_life_days
        decayed = initial_score * math.exp(-decay_constant * days_elapsed)
        
        return max(0.0, min(100.0, decayed))
    
    @classmethod
    def weibull_decay(
        cls,
        initial_score: float,
        days_elapsed: float,
        scale: float = 100.0,
        shape: float = 1.5
    ) -> float:
        """
        Calculate Weibull-decayed score.
        
        Formula: S(t) = S₀ × exp(-(t/λ)^k)
        
        Args:
            scale (λ): Characteristic life
            shape (k): k<1 early failure, k>1 aging pattern
        """
        if days_elapsed <= 0:
            return initial_score
        
        weibull_factor = math.exp(-((days_elapsed / scale) ** shape))
        decayed = initial_score * weibull_factor
        
        return max(0.0, min(100.0, decayed))
    
    @classmethod
    def calculate_confidence_interval(
        cls,
        score: float,
        sample_size: int = 30,
        std_dev: float = 5.0
    ) -> Tuple[float, float]:
        """
        Calculate confidence interval using bootstrap approximation.
        
        CI = score ± 1.96 × σ / √n
        """
        margin = 1.96 * std_dev / math.sqrt(sample_size)
        lower = max(0.0, score - margin)
        upper = min(100.0, score + margin)
        return (round(lower, 2), round(upper, 2))
    
    @classmethod
    def project_future_score(
        cls,
        current_score: float,
        days_forward: int,
        half_life_days: int
    ) -> float:
        """Project score at future date."""
        return cls.exponential_decay(current_score, days_forward, half_life_days)
    
    @classmethod
    def determine_health(cls, score: float) -> CredibilityHealth:
        """Determine health status from score."""
        if score >= 80:
            return CredibilityHealth.HEALTHY
        elif score >= 60:
            return CredibilityHealth.ATTENTION
        elif score >= 40:
            return CredibilityHealth.WARNING
        elif score >= 20:
            return CredibilityHealth.CRITICAL
        else:
            return CredibilityHealth.EXPIRED
    
    @classmethod
    def calculate_score(
        cls,
        asset: EvidenceAsset,
        model: DecayModel = DecayModel.EXPONENTIAL
    ) -> CredibilityScore:
        """Calculate complete credibility score for an asset."""
        days_elapsed = asset.days_since_refresh()
        half_life = ASSET_HALF_LIVES.get(asset.asset_type, 90)
        
        if model == DecayModel.EXPONENTIAL:
            current = cls.exponential_decay(asset.initial_score, days_elapsed, half_life)
        elif model == DecayModel.WEIBULL:
            current = cls.weibull_decay(asset.initial_score, days_elapsed)
        else:
            decay_rate = asset.initial_score / (half_life * 2)
            current = max(0.0, asset.initial_score - (decay_rate * days_elapsed))
        
        decay_pct = ((asset.initial_score - current) / asset.initial_score) * 100 if asset.initial_score > 0 else 0
        health = cls.determine_health(current)
        projected = cls.project_future_score(current, 30, half_life)
        ci = cls.calculate_confidence_interval(current)
        
        return CredibilityScore(
            asset_id=asset.asset_id,
            current_score=current,
            initial_score=asset.initial_score,
            decay_percentage=decay_pct,
            health=health,
            days_since_refresh=days_elapsed,
            half_life_days=half_life,
            projected_30_day_score=projected,
            confidence_interval=ci
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for decay mathematics."""
        return """
MODULE 1: FORMAL DECAY MATHEMATICS
├─ Exponential Decay: score(t) = S₀ × exp(-ln(2) × t / T_half)
├─ Weibull Distribution: score(t) = S₀ × exp(-(t/λ)^k)
│   ├─ λ: Scale parameter (characteristic life)
│   └─ k: Shape parameter (k<1 early failure, k>1 aging)
├─ Confidence Intervals: ±1.96 × σ / √n (bootstrap resampling)
└─ Composite Scoring:
    ├─ Proof Freshness: 30%
    ├─ Social Momentum: 25%
    ├─ Relevance Index: 20%
    ├─ Endorsement Quality: 15%
    └─ Fraud Score: 10%
"""
