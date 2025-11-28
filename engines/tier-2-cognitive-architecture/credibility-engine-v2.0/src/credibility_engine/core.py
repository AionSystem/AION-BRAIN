"""
CREDIBILITY ENGINE v2.0 - Core Engine
======================================

Trust Acceleration System with Mathematical Rigor.

Author: Sheldon K. Salmon
Codename: VERITAS
License: Apache 2.0
"""

import time
from datetime import datetime
from typing import List, Optional, Dict

from .config import CredibilityConfig
from .scoring import (
    EvidenceAsset, AssetType, CredibilityScore, CompositeScore,
    DecayAlert, CredibilityHealth, FraudSignal, DecayModel
)
from .analysis import CredibilityAnalysis, CredibilityReport, AssetSummary
from .modules.decay_math import DecayMathematics
from .modules.signals import SignalInstrumentation
from .modules.explainability import ExplainabilityEngine, ScoreExplanation
from .modules.automation import ActionAutomation, Playbook
from .modules.fraud import FraudDetection, AuthenticityCheck
from .modules.provenance import ProvenanceSystem


class CredibilityEngine:
    """
    CREDIBILITY ENGINE v2.0 - VERITAS
    
    The Complete Trust Acceleration System with Mathematical Rigor.
    
    Modules:
    1. Formal Decay Mathematics (Exponential + Weibull)
    2. Signal Instrumentation (Multi-API data pipeline)
    3. Score Explainability (Rationale generation)
    4. Action Automation (Alert-to-playbook mapping)
    5. A/B Testing Framework (Intervention testing)
    6. Fraud Detection (Manipulation signals)
    7. Evidence Provenance (Immutable verification)
    8. Operator UX (Dashboard components)
    
    Usage:
        # Generate prompts for AI systems
        engine = CredibilityEngine()
        prompt = engine.generate_system_prompt()
        
        # Analyze credibility of assets
        engine = CredibilityEngine()
        engine.add_asset(EvidenceAsset(...))
        analysis = engine.analyze()
    
    Author: Sheldon K. Salmon
    Codename: VERITAS
    """
    
    VERSION = "2.0.0"
    CODENAME = "VERITAS"
    
    def __init__(self, config: Optional[CredibilityConfig] = None):
        """Initialize Credibility Engine."""
        self.config = config or CredibilityConfig.standard()
        self._assets: Dict[str, EvidenceAsset] = {}
        self._scores: Dict[str, CredibilityScore] = {}
        self._provenance = ProvenanceSystem() if self.config.enable_provenance else None
    
    def add_asset(self, asset: EvidenceAsset) -> None:
        """Add a credibility asset to track."""
        self._assets[asset.asset_id] = asset
    
    def remove_asset(self, asset_id: str) -> bool:
        """Remove a credibility asset."""
        if asset_id in self._assets:
            del self._assets[asset_id]
            if asset_id in self._scores:
                del self._scores[asset_id]
            return True
        return False
    
    def get_asset(self, asset_id: str) -> Optional[EvidenceAsset]:
        """Get an asset by ID."""
        return self._assets.get(asset_id)
    
    def calculate_score(
        self,
        asset: EvidenceAsset,
        model: DecayModel = DecayModel.EXPONENTIAL
    ) -> CredibilityScore:
        """Calculate credibility score for a single asset."""
        score = DecayMathematics.calculate_score(asset, model)
        self._scores[asset.asset_id] = score
        return score
    
    def calculate_all_scores(self) -> Dict[str, CredibilityScore]:
        """Calculate scores for all tracked assets."""
        for asset_id, asset in self._assets.items():
            self.calculate_score(asset)
        return self._scores.copy()
    
    def get_composite_score(self) -> CompositeScore:
        """Calculate composite credibility score."""
        return SignalInstrumentation.quick_composite()
    
    def explain_score(
        self,
        score: CredibilityScore,
        composite: Optional[CompositeScore] = None
    ) -> ScoreExplanation:
        """Generate explanation for a score."""
        return ExplainabilityEngine.explain_score(score, composite)
    
    def generate_alerts(self) -> List[DecayAlert]:
        """Generate alerts for all assets needing attention."""
        alerts = []
        for asset_id, score in self._scores.items():
            alert = ActionAutomation.generate_alert(score)
            if alert:
                alerts.append(alert)
        return sorted(alerts, key=lambda a: a.current_score)
    
    def check_fraud(
        self,
        account_age_days: int,
        posting_history: int,
        verified: bool
    ) -> AuthenticityCheck:
        """Check testimonial authenticity."""
        return FraudDetection.check_testimonial_authenticity(
            account_age_days, posting_history, verified
        )
    
    def analyze(self) -> CredibilityAnalysis:
        """Perform complete credibility analysis."""
        start_time = time.time()
        
        self.calculate_all_scores()
        
        summaries = []
        health_counts = {h: 0 for h in CredibilityHealth}
        
        for asset_id, asset in self._assets.items():
            score = self._scores.get(asset_id)
            if score:
                health_counts[score.health] += 1
                alert = ActionAutomation.generate_alert(score)
                summaries.append(AssetSummary(
                    asset_id=asset_id,
                    name=asset.name,
                    score=score,
                    alert=alert,
                    fraud_signals=[]
                ))
        
        composite = self.get_composite_score()
        alerts = self.generate_alerts()
        
        if health_counts[CredibilityHealth.CRITICAL] > 0 or health_counts[CredibilityHealth.EXPIRED] > 0:
            overall = CredibilityHealth.CRITICAL
        elif health_counts[CredibilityHealth.WARNING] > 0:
            overall = CredibilityHealth.WARNING
        elif health_counts[CredibilityHealth.ATTENTION] > 0:
            overall = CredibilityHealth.ATTENTION
        else:
            overall = CredibilityHealth.HEALTHY
        
        recommendations = []
        if alerts:
            for alert in alerts[:3]:
                recommendations.extend(alert.recommended_actions[:2])
        if not recommendations:
            recommendations = ["Maintain current credibility health", "Schedule routine asset review"]
        
        report = CredibilityReport(
            total_assets=len(self._assets),
            healthy_count=health_counts[CredibilityHealth.HEALTHY],
            attention_count=health_counts[CredibilityHealth.ATTENTION],
            warning_count=health_counts[CredibilityHealth.WARNING],
            critical_count=health_counts[CredibilityHealth.CRITICAL],
            expired_count=health_counts[CredibilityHealth.EXPIRED],
            overall_health=overall,
            composite_score=composite,
            priority_alerts=alerts[:5],
            recommendations=recommendations[:5]
        )
        
        processing_time = (time.time() - start_time) * 1000
        
        return CredibilityAnalysis(
            analyzed_at=datetime.now(),
            assets=summaries,
            report=report,
            fraud_summary={"signals_detected": 0},
            provenance_verified=self._provenance.verify_chain_integrity() if self._provenance else True,
            processing_time_ms=processing_time
        )
    
    def generate_system_prompt(self, compact: bool = False) -> str:
        """Generate Credibility Engine prompt for AI systems."""
        if compact:
            return self._build_compact_prompt()
        return self._build_full_prompt()
    
    def _build_compact_prompt(self) -> str:
        """Build compact prompt."""
        return """<CREDIBILITY_ENGINE v2.0 COMPACT>

TRUST ACCELERATION SYSTEM

DECAY MODELS:
• Exponential: S(t) = S₀ × exp(-ln(2) × t / T_half)
• Weibull: S(t) = S₀ × exp(-(t/λ)^k)

SCORING WEIGHTS:
• Proof Freshness: 30%
• Social Momentum: 25%
• Relevance Index: 20%
• Endorsement Quality: 15%
• Fraud Score: 10%

HEALTH THRESHOLDS:
• 80-100: Healthy (maintenance mode)
• 60-79: Attention (refresh within 30 days)
• 40-59: Warning (immediate action)
• 20-39: Critical (emergency intervention)
• 0-19: Expired (complete rebuild)

OUTPUT: Health Status + Score + Alerts + Recommended Actions

</CREDIBILITY_ENGINE>"""
    
    def _build_full_prompt(self) -> str:
        """Build full prompt."""
        return """<CREDIBILITY_ENGINE v2.0>

You are CREDIBILITY ENGINE v2.0 (VERITAS), the Complete Trust Acceleration System.

MODULES:
1. FORMAL DECAY MATHEMATICS
   - Exponential: score(t) = S₀ × exp(-ln(2) × t / T_half)
   - Weibull: score(t) = S₀ × exp(-(t/λ)^k)
   - Confidence intervals via bootstrap resampling

2. SIGNAL INSTRUMENTATION
   - Search volume (Google Trends API)
   - Social velocity (Twitter, LinkedIn, Reddit)
   - Proof engagement (GitHub, demos, CRM)

3. SCORE EXPLAINABILITY
   - Rationale generation for score changes
   - Shapley-style contribution analysis
   - Root cause identification

4. ACTION AUTOMATION
   - Alert-to-playbook mapping
   - Automated task creation
   - SLA-based response protocols

5. FRAUD DETECTION
   - Testimonial authenticity checks
   - Velocity anomaly detection
   - Compliance guardrails (FTC, GDPR)

6. EVIDENCE PROVENANCE
   - Immutable evidence logging
   - Cryptographic hash verification
   - Chain of custody tracking

ASSET HALF-LIVES:
• Live Demo: 90 days
• Case Study: 180 days
• Testimonial: 120 days
• Conference Talk: 365 days
• Publication: 730 days

ANALYSIS PROTOCOL:
1. Calculate decay for each credibility asset
2. Compute composite score from weighted components
3. Generate health status and alerts
4. Recommend maintenance/refresh actions
5. Track provenance and detect fraud signals

OUTPUT FORMAT:
═══════════════════════════════════════════
CREDIBILITY ANALYSIS COMPLETE
═══════════════════════════════════════════

Overall Health: [HEALTHY | ATTENTION | WARNING | CRITICAL | EXPIRED]
Composite Score: [0-100]

Asset Breakdown:
[List of assets with individual scores and alerts]

Priority Alerts:
[Ranked alerts with recommended actions]

Recommendations:
1. [Action item]
2. [Action item]
3. [Action item]

═══════════════════════════════════════════

</CREDIBILITY_ENGINE>"""
    
    def __repr__(self) -> str:
        return f"CredibilityEngine(assets={len(self._assets)}, v{self.VERSION})"
