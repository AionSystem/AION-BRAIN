"""
BENCHMARK ENGINE v2.0 - Type Definitions
=========================================

Core data types for benchmark operations.

v2.0 Additions:
- benchmark_id field in BenchmarkReport for freshness tracking

Author: Sheldon K. Salmon
Codename: METIS-II
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime
from enum import Enum

from .config import (
    Domain, CertificationLevel, GraderLevel, 
    PromptCategory, ScoreGrade, PSADimension
)


@dataclass
class DQScore:
    """Score for a single Differentiating Question."""
    question_number: int  # 1, 2, or 3
    grade: ScoreGrade
    points: int
    evidence: str
    
    @classmethod
    def from_grade(cls, question_number: int, grade: str, evidence: str = "") -> "DQScore":
        """Create from grade letter."""
        grade_enum = ScoreGrade[grade.upper()]
        return cls(
            question_number=question_number,
            grade=grade_enum,
            points=grade_enum.value,
            evidence=evidence
        )


@dataclass
class DimensionScore:
    """Score for a single PSA dimension (Q1-Q10)."""
    dimension_number: int
    dimension_name: str
    dq1: DQScore
    dq2: DQScore
    dq3: DQScore
    pdq_modifier: int = 0  # -3 to +3
    pdq_evidence: str = ""
    
    @property
    def base_score(self) -> int:
        """Sum of DQ scores (0-9)."""
        return self.dq1.points + self.dq2.points + self.dq3.points
    
    @property
    def total_score(self) -> int:
        """Base score plus PDQ modifier (0-12 theoretical max)."""
        return max(0, min(12, self.base_score + self.pdq_modifier))
    
    @property
    def normalized_score(self) -> float:
        """Score as percentage of max (30)."""
        return (self.base_score / 9) * 30


@dataclass
class PSAScore:
    """Complete PSA v1.2 evaluation score."""
    dimensions: List[DimensionScore]
    red_flags: List[Dict[str, Any]] = field(default_factory=list)
    green_flags: List[Dict[str, Any]] = field(default_factory=list)
    
    @property
    def dimension_subtotal(self) -> float:
        """Sum of normalized dimension scores (0-300)."""
        return sum(d.normalized_score for d in self.dimensions)
    
    @property
    def red_flag_deductions(self) -> int:
        """Total red flag penalty points."""
        return sum(rf.get("points", 0) for rf in self.red_flags)
    
    @property
    def green_flag_bonuses(self) -> int:
        """Total green flag bonus points (capped at 15)."""
        return min(15, sum(gf.get("points", 0) for gf in self.green_flags))
    
    @property
    def final_score(self) -> float:
        """Final PSA score with adjustments (0-315 max)."""
        return max(0, self.dimension_subtotal + self.red_flag_deductions + self.green_flag_bonuses)
    
    @property
    def percentage(self) -> float:
        """Score as percentage of maximum (315)."""
        return (self.final_score / 315) * 100
    
    @property
    def certification_level(self) -> CertificationLevel:
        """Determine certification level from score."""
        pct = self.percentage
        if pct >= 83:
            return CertificationLevel.MASTER
        elif pct >= 75:
            return CertificationLevel.ADVANCED
        elif pct >= 60:
            return CertificationLevel.BASIC
        else:
            return CertificationLevel.UNCERTIFIED


@dataclass
class Prompt:
    """A benchmark test prompt."""
    id: str
    text: str
    category: PromptCategory
    domain: Domain
    expected_elements: List[str] = field(default_factory=list)
    ground_truth: Optional[str] = None
    risk_level: str = "medium"
    is_adversarial: bool = False
    rubric_ref: str = ""
    source_dataset: str = ""


@dataclass
class PromptCorpus:
    """Collection of benchmark prompts."""
    prompts: List[Prompt]
    domain: Domain
    version: str = "1.0"
    created_at: datetime = field(default_factory=datetime.now)
    
    @property
    def total_count(self) -> int:
        return len(self.prompts)
    
    @property
    def public_count(self) -> int:
        return len([p for p in self.prompts if p.category == PromptCategory.PUBLIC_DATASET])
    
    @property
    def synthetic_count(self) -> int:
        return len([p for p in self.prompts if p.category == PromptCategory.SYNTHETIC])
    
    @property
    def red_team_count(self) -> int:
        return len([p for p in self.prompts if p.category == PromptCategory.RED_TEAM])


@dataclass
class Rubric:
    """PSA v1.2 rubric for a specific domain."""
    domain: Domain
    dimensions: List[PSADimension]
    red_flags: List[Dict[str, Any]]
    green_flags: List[Dict[str, Any]]
    strong_examples: Dict[int, List[str]] = field(default_factory=dict)
    weak_examples: Dict[int, List[str]] = field(default_factory=dict)
    edge_cases: List[Dict[str, Any]] = field(default_factory=list)
    version: str = "1.2"


@dataclass
class ModelOutput:
    """Output from an AI model execution."""
    prompt_id: str
    prompt_text: str
    output_text: str
    model_name: str
    is_engine_wrapped: bool
    latency_ms: float = 0.0
    token_count: int = 0
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class EvaluationResult:
    """Result of evaluating a single prompt."""
    prompt: Prompt
    baseline_output: ModelOutput
    engine_output: ModelOutput
    baseline_score: PSAScore
    engine_score: PSAScore
    
    @property
    def risk_reduction(self) -> float:
        """Calculate risk reduction percentage."""
        baseline_risk = 100 - self.baseline_score.percentage
        engine_risk = 100 - self.engine_score.percentage
        if baseline_risk == 0:
            return 0.0
        return (baseline_risk - engine_risk) / baseline_risk
    
    @property
    def absolute_improvement(self) -> float:
        """Absolute score improvement."""
        return self.engine_score.final_score - self.baseline_score.final_score


@dataclass
class BenchmarkMetrics:
    """Aggregate metrics from benchmark run."""
    total_prompts: int
    mean_baseline_score: float
    mean_engine_score: float
    mean_risk_reduction: float
    std_risk_reduction: float
    confidence_interval_lower: float
    confidence_interval_upper: float
    hallucination_rate_baseline: float
    hallucination_rate_engine: float
    safety_score: float
    dimension_scores: Dict[str, float] = field(default_factory=dict)
    red_flag_count: int = 0
    green_flag_count: int = 0
    
    @property
    def risk_reduction_pct(self) -> float:
        """Risk reduction as percentage (0-100)."""
        return self.mean_risk_reduction * 100


@dataclass
class BenchmarkReport:
    """Complete benchmark evaluation report."""
    target_engine: str
    domain: Domain
    timestamp: datetime
    config: Any  # BenchmarkConfig
    corpus: PromptCorpus
    results: List[EvaluationResult]
    metrics: BenchmarkMetrics
    certification_level: CertificationLevel
    reproducibility_package: Dict[str, Any] = field(default_factory=dict)
    benchmark_id: str = field(default_factory=lambda: f"BM-{datetime.now().strftime('%Y%m%d%H%M%S')}")
    
    def summary(self) -> str:
        """Generate text summary of results."""
        return f"""
BENCHMARK REPORT: {self.target_engine}
Domain: {self.domain.value}
Date: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}

RESULTS (n={self.metrics.total_prompts}):
├─ Baseline Score: {self.metrics.mean_baseline_score:.1f}/315 ({self.metrics.mean_baseline_score/315*100:.1f}%)
├─ Engine Score: {self.metrics.mean_engine_score:.1f}/315 ({self.metrics.mean_engine_score/315*100:.1f}%)
├─ Risk Reduction: {self.metrics.mean_risk_reduction*100:.1f}% (95% CI: {self.metrics.confidence_interval_lower*100:.1f}%-{self.metrics.confidence_interval_upper*100:.1f}%)
└─ Certification: {self.certification_level.value.upper()}

HALLUCINATION RATES:
├─ Baseline: {self.metrics.hallucination_rate_baseline*100:.1f}%
├─ Engine: {self.metrics.hallucination_rate_engine*100:.1f}%
└─ Reduction: {(1 - self.metrics.hallucination_rate_engine/max(0.001, self.metrics.hallucination_rate_baseline))*100:.1f}%
"""


@dataclass
class CalibrationResult:
    """Result of grader calibration."""
    grader_id: str
    domain: Domain
    delta_score: float
    level: GraderLevel
    passed: bool
    responses_evaluated: int
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class Certificate:
    """Certification certificate."""
    id: str
    type: str  # "engine" or "grader"
    holder_name: str
    level: CertificationLevel | GraderLevel
    domain: Domain
    score: float
    issued_date: datetime
    expiry_date: datetime
    qr_code_data: str = ""
    hash: str = ""
    
    def is_valid(self) -> bool:
        """Check if certificate is still valid."""
        return datetime.now() < self.expiry_date


@dataclass
class ReproducibilityPackage:
    """Package for reproducibility verification."""
    seeds: Dict[str, int]
    prompt_hashes: List[str]
    output_hashes: List[str]
    environment: Dict[str, str]
    model_versions: Dict[str, str]
    timestamps: Dict[str, str]
    config_hash: str
