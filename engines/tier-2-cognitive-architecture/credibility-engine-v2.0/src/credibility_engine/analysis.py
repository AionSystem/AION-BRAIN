"""
CREDIBILITY ENGINE v2.0 - Analysis Results
============================================

Data classes for credibility analysis results.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime
from .scoring import (
    EvidenceAsset, CredibilityScore, CompositeScore,
    DecayAlert, FraudSignal, CredibilityHealth
)


@dataclass
class AssetSummary:
    """Summary of a single credibility asset."""
    asset_id: str
    name: str
    score: CredibilityScore
    alert: Optional[DecayAlert]
    fraud_signals: List[FraudSignal]


@dataclass
class CredibilityReport:
    """Complete credibility health report."""
    total_assets: int
    healthy_count: int
    attention_count: int
    warning_count: int
    critical_count: int
    expired_count: int
    overall_health: CredibilityHealth
    composite_score: CompositeScore
    priority_alerts: List[DecayAlert]
    recommendations: List[str]
    
    def to_dict(self) -> dict:
        return {
            "total_assets": self.total_assets,
            "health_breakdown": {
                "healthy": self.healthy_count,
                "attention": self.attention_count,
                "warning": self.warning_count,
                "critical": self.critical_count,
                "expired": self.expired_count
            },
            "overall_health": self.overall_health.value,
            "composite": self.composite_score.to_dict(),
            "alerts": [a.to_dict() for a in self.priority_alerts],
            "recommendations": self.recommendations
        }


@dataclass
class CredibilityAnalysis:
    """Complete credibility analysis result."""
    analyzed_at: datetime
    assets: List[AssetSummary]
    report: CredibilityReport
    fraud_summary: Dict
    provenance_verified: bool
    processing_time_ms: float = 0.0
    
    def summary(self) -> str:
        """Generate human-readable summary."""
        lines = [
            "=" * 70,
            "CREDIBILITY ENGINE v2.0 — VERITAS",
            "=" * 70,
            f"Analyzed: {self.analyzed_at.strftime('%Y-%m-%d %H:%M')}",
            f"Total Assets: {self.report.total_assets}",
            f"Overall Health: {self.report.overall_health.value.upper()}",
            f"Composite Score: {self.report.composite_score.composite:.1f}",
            "",
            "Health Breakdown:",
            f"  Healthy: {self.report.healthy_count}",
            f"  Attention: {self.report.attention_count}",
            f"  Warning: {self.report.warning_count}",
            f"  Critical: {self.report.critical_count}",
            f"  Expired: {self.report.expired_count}",
            ""
        ]
        
        if self.report.priority_alerts:
            lines.append("Priority Alerts:")
            for alert in self.report.priority_alerts[:3]:
                lines.append(f"  - [{alert.priority.value}] {alert.message}")
        
        lines.extend([
            "",
            "Recommendations:",
        ])
        for i, rec in enumerate(self.report.recommendations[:5], 1):
            lines.append(f"  {i}. {rec}")
        
        lines.extend(["", "=" * 70])
        
        return "\n".join(lines)
    
    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "analyzed_at": self.analyzed_at.isoformat(),
            "assets": [
                {
                    "id": a.asset_id,
                    "name": a.name,
                    "score": a.score.to_dict()
                }
                for a in self.assets
            ],
            "report": self.report.to_dict(),
            "fraud_summary": self.fraud_summary,
            "provenance_verified": self.provenance_verified
        }
