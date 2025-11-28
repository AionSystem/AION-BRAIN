"""
BENCHMARK ENGINE v2.0 - Engine Integrations
============================================

Polymath integration modules that connect Benchmark Engine with other AION engines.

Integrations:
1. Trinity Scoring (Oracle Layer) - 3-judge consensus evaluation
2. Benchmark Freshness (Credibility Engine) - Time-decay validity
3. Audience Reports (Explanation Engine) - Multi-format reports

Author: Sheldon K. Salmon
"""

from .trinity_scoring import TrinityScoring, TrinityJudge, TrinityVerdict, JudgeRole
from .benchmark_freshness import BenchmarkFreshness, FreshnessScore, DecayModel, ValidityStatus
from .audience_reports import AudienceReports, ReportFormat, AudienceLevel, FormattedReport

__all__ = [
    "TrinityScoring", "TrinityJudge", "TrinityVerdict", "JudgeRole",
    "BenchmarkFreshness", "FreshnessScore", "DecayModel", "ValidityStatus",
    "AudienceReports", "ReportFormat", "AudienceLevel", "FormattedReport",
]
