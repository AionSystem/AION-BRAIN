"""
BENCHMARK ENGINE v2.0 - Test Suite
===================================

Comprehensive tests for the Benchmark Engine with v2.0 integrations.

v2.0 Test Coverage:
- Trinity Scoring (Oracle Layer integration)
- Benchmark Freshness (Credibility Engine integration)
- Audience Reports (Explanation Engine integration)

Author: Sheldon K. Salmon
"""

import pytest
from datetime import datetime

from benchmark_engine import (
    BenchmarkEngine, BenchmarkConfig, Domain, CertificationLevel
)
from benchmark_engine.config import (
    PSA_DIMENSIONS, RED_FLAGS, GREEN_FLAGS, 
    GraderLevel, PromptCategory, ScoreGrade,
    BenchmarkMode, BENCHMARK_MODE_CONFIG, SUPPORTED_LLMS
)
from benchmark_engine.types import (
    PSAScore, DimensionScore, DQScore, Prompt, PromptCorpus,
    Rubric, Certificate, CalibrationResult
)


class TestBenchmarkModes:
    """Tests for Benchmark Mode configuration."""
    
    def test_quick_mode_prompts(self):
        config = BenchmarkConfig.quick()
        assert config.mode == BenchmarkMode.QUICK
        assert config.prompt_count == 50
    
    def test_standard_mode_prompts(self):
        config = BenchmarkConfig.standard()
        assert config.mode == BenchmarkMode.STANDARD
        assert config.prompt_count == 2000
    
    def test_comprehensive_mode_prompts(self):
        config = BenchmarkConfig.comprehensive()
        assert config.mode == BenchmarkMode.COMPREHENSIVE
        assert config.prompt_count == 8000
    
    def test_comprehensive_default_llms(self):
        config = BenchmarkConfig.comprehensive()
        assert len(config.comparison_llms) >= 3
        assert "claude-3-5-sonnet" in config.comparison_llms
    
    def test_comprehensive_custom_llms(self):
        llms = ["gpt-4o", "gemini-2.0-flash"]
        config = BenchmarkConfig.comprehensive(llms=llms)
        assert config.comparison_llms == llms
    
    def test_mode_config_exists(self):
        for mode in BenchmarkMode:
            assert mode in BENCHMARK_MODE_CONFIG
            assert "prompts_per_run" in BENCHMARK_MODE_CONFIG[mode]
    
    def test_supported_llms(self):
        assert len(SUPPORTED_LLMS) >= 5
        for key, llm in SUPPORTED_LLMS.items():
            assert "provider" in llm
            assert "model_id" in llm
            assert "display_name" in llm


class TestCostEstimation:
    """Tests for cost estimation."""
    
    def test_quick_mode_cost(self):
        config = BenchmarkConfig.quick()
        cost = config.estimate_cost()
        assert "total_usd" in cost
        assert cost["total_usd"] < 10
    
    def test_standard_mode_cost(self):
        config = BenchmarkConfig.standard()
        cost = config.estimate_cost()
        assert cost["total_usd"] > 5
        assert cost["total_usd"] < 100
    
    def test_comprehensive_mode_cost(self):
        config = BenchmarkConfig.comprehensive()
        cost = config.estimate_cost()
        assert "breakdown" in cost
        assert len(cost["breakdown"]) >= 3


class TestBenchmarkConfig:
    """Tests for BenchmarkConfig."""
    
    def test_default_config(self):
        config = BenchmarkConfig()
        assert config.domain == Domain.GENERAL
        assert config.mode == BenchmarkMode.QUICK
        assert config.prompt_count == 50
        assert config.random_seed == 42
    
    def test_medical_config(self):
        config = BenchmarkConfig.for_medical()
        assert config.domain == Domain.MEDICAL
    
    def test_legal_config(self):
        config = BenchmarkConfig.for_legal()
        assert config.domain == Domain.LEGAL
    
    def test_financial_config(self):
        config = BenchmarkConfig.for_financial()
        assert config.domain == Domain.FINANCIAL
    
    def test_prompt_distribution_quick(self):
        config = BenchmarkConfig.quick()
        dist = config.get_prompt_distribution()
        assert PromptCategory.PUBLIC_DATASET in dist
        assert PromptCategory.SYNTHETIC in dist
        assert PromptCategory.RED_TEAM in dist
        total = sum(dist.values())
        assert total == 50
    
    def test_prompt_distribution_standard(self):
        config = BenchmarkConfig.standard()
        dist = config.get_prompt_distribution()
        total = sum(dist.values())
        assert total == 2000
    
    def test_prompt_ratios(self):
        config = BenchmarkConfig.standard()
        dist = config.get_prompt_distribution()
        assert dist[PromptCategory.PUBLIC_DATASET] == 1000  # 50%
        assert dist[PromptCategory.SYNTHETIC] == 700        # 35%
        assert dist[PromptCategory.RED_TEAM] == 300         # 15%


class TestPSADimensions:
    """Tests for PSA dimension configuration."""
    
    def test_dimension_count(self):
        assert len(PSA_DIMENSIONS) == 10
    
    def test_dimension_structure(self):
        for dim in PSA_DIMENSIONS:
            assert dim.number >= 1 and dim.number <= 10
            assert dim.name
            assert dim.dq1
            assert dim.dq2
            assert dim.dq3
            assert dim.pdq
    
    def test_dimension_uniqueness(self):
        numbers = [d.number for d in PSA_DIMENSIONS]
        assert len(numbers) == len(set(numbers))


class TestRedAndGreenFlags:
    """Tests for flag configuration."""
    
    def test_red_flags_exist(self):
        assert len(RED_FLAGS) > 0
    
    def test_red_flags_negative_points(self):
        for rf in RED_FLAGS:
            assert rf.points < 0
    
    def test_green_flags_exist(self):
        assert len(GREEN_FLAGS) > 0
    
    def test_green_flags_positive_points(self):
        for gf in GREEN_FLAGS:
            assert gf.points > 0


class TestDQScore:
    """Tests for DQ scoring."""
    
    def test_from_grade_a(self):
        score = DQScore.from_grade(1, "A", "Test evidence")
        assert score.grade == ScoreGrade.A
        assert score.points == 3
    
    def test_from_grade_b(self):
        score = DQScore.from_grade(2, "B", "Test evidence")
        assert score.grade == ScoreGrade.B
        assert score.points == 2
    
    def test_from_grade_c(self):
        score = DQScore.from_grade(3, "C", "Test evidence")
        assert score.grade == ScoreGrade.C
        assert score.points == 1
    
    def test_from_grade_d(self):
        score = DQScore.from_grade(1, "D", "Test evidence")
        assert score.grade == ScoreGrade.D
        assert score.points == 0


class TestDimensionScore:
    """Tests for dimension scoring."""
    
    def test_base_score_calculation(self):
        dq1 = DQScore(1, ScoreGrade.A, 3, "")
        dq2 = DQScore(2, ScoreGrade.B, 2, "")
        dq3 = DQScore(3, ScoreGrade.A, 3, "")
        
        dim_score = DimensionScore(
            dimension_number=1,
            dimension_name="Test",
            dq1=dq1, dq2=dq2, dq3=dq3
        )
        
        assert dim_score.base_score == 8  # 3+2+3
    
    def test_total_score_with_pdq(self):
        dq1 = DQScore(1, ScoreGrade.B, 2, "")
        dq2 = DQScore(2, ScoreGrade.B, 2, "")
        dq3 = DQScore(3, ScoreGrade.B, 2, "")
        
        dim_score = DimensionScore(
            dimension_number=1,
            dimension_name="Test",
            dq1=dq1, dq2=dq2, dq3=dq3,
            pdq_modifier=2
        )
        
        assert dim_score.total_score == 8  # 6+2, capped at 12
    
    def test_normalized_score(self):
        dq1 = DQScore(1, ScoreGrade.A, 3, "")
        dq2 = DQScore(2, ScoreGrade.A, 3, "")
        dq3 = DQScore(3, ScoreGrade.A, 3, "")
        
        dim_score = DimensionScore(
            dimension_number=1,
            dimension_name="Test",
            dq1=dq1, dq2=dq2, dq3=dq3
        )
        
        assert dim_score.normalized_score == 30.0  # Perfect score


class TestPSAScore:
    """Tests for overall PSA scoring."""
    
    def create_dimension_score(self, points: int = 6) -> DimensionScore:
        grade = ScoreGrade.B if points == 6 else ScoreGrade.A
        return DimensionScore(
            dimension_number=1,
            dimension_name="Test",
            dq1=DQScore(1, grade, grade.value, ""),
            dq2=DQScore(2, grade, grade.value, ""),
            dq3=DQScore(3, grade, grade.value, "")
        )
    
    def test_dimension_subtotal(self):
        dimensions = [self.create_dimension_score(6) for _ in range(10)]
        score = PSAScore(dimensions=dimensions)
        # Each dimension: 6/9 * 30 = 20, total = 200
        assert score.dimension_subtotal == pytest.approx(200.0, 0.1)
    
    def test_red_flag_deductions(self):
        dimensions = [self.create_dimension_score() for _ in range(10)]
        score = PSAScore(
            dimensions=dimensions,
            red_flags=[{"points": -10}, {"points": -5}]
        )
        assert score.red_flag_deductions == -15
    
    def test_green_flag_bonuses_capped(self):
        dimensions = [self.create_dimension_score() for _ in range(10)]
        score = PSAScore(
            dimensions=dimensions,
            green_flags=[{"points": 3} for _ in range(10)]  # 30 total, but capped at 15
        )
        assert score.green_flag_bonuses == 15
    
    def test_certification_level_master(self):
        dimensions = []
        for i in range(10):
            dimensions.append(DimensionScore(
                dimension_number=i+1,
                dimension_name=f"Dim{i}",
                dq1=DQScore(1, ScoreGrade.A, 3, ""),
                dq2=DQScore(2, ScoreGrade.A, 3, ""),
                dq3=DQScore(3, ScoreGrade.A, 3, "")
            ))
        score = PSAScore(dimensions=dimensions)
        assert score.certification_level == CertificationLevel.MASTER
    
    def test_certification_level_uncertified(self):
        dimensions = []
        for i in range(10):
            dimensions.append(DimensionScore(
                dimension_number=i+1,
                dimension_name=f"Dim{i}",
                dq1=DQScore(1, ScoreGrade.D, 0, ""),
                dq2=DQScore(2, ScoreGrade.D, 0, ""),
                dq3=DQScore(3, ScoreGrade.D, 0, "")
            ))
        score = PSAScore(dimensions=dimensions)
        assert score.certification_level == CertificationLevel.UNCERTIFIED


class TestPrompt:
    """Tests for Prompt type."""
    
    def test_prompt_creation(self):
        prompt = Prompt(
            id="TEST-001",
            text="Test prompt",
            category=PromptCategory.PUBLIC_DATASET,
            domain=Domain.MEDICAL
        )
        assert prompt.id == "TEST-001"
        assert prompt.category == PromptCategory.PUBLIC_DATASET
        assert not prompt.is_adversarial


class TestPromptCorpus:
    """Tests for PromptCorpus."""
    
    def test_corpus_counts(self):
        prompts = [
            Prompt("P1", "text", PromptCategory.PUBLIC_DATASET, Domain.MEDICAL),
            Prompt("P2", "text", PromptCategory.PUBLIC_DATASET, Domain.MEDICAL),
            Prompt("S1", "text", PromptCategory.SYNTHETIC, Domain.MEDICAL),
            Prompt("R1", "text", PromptCategory.RED_TEAM, Domain.MEDICAL),
        ]
        corpus = PromptCorpus(prompts=prompts, domain=Domain.MEDICAL)
        
        assert corpus.total_count == 4
        assert corpus.public_count == 2
        assert corpus.synthetic_count == 1
        assert corpus.red_team_count == 1


class TestBenchmarkEngine:
    """Tests for BenchmarkEngine core."""
    
    def test_engine_creation(self):
        engine = BenchmarkEngine()
        assert engine.VERSION == "2.0.0"
        assert engine.CODENAME == "METIS-II"
    
    def test_engine_with_config(self):
        config = BenchmarkConfig.for_medical()
        engine = BenchmarkEngine(config=config)
        assert engine.config.domain == Domain.MEDICAL
    
    def test_quick_test_factory(self):
        engine = BenchmarkEngine.quick_test(Domain.MEDICAL)
        assert engine.config.mode == BenchmarkMode.QUICK
        assert engine.config.domain == Domain.MEDICAL
        assert engine.config.prompt_count == 50
    
    def test_standard_test_factory(self):
        engine = BenchmarkEngine.standard_test(Domain.LEGAL)
        assert engine.config.mode == BenchmarkMode.STANDARD
        assert engine.config.domain == Domain.LEGAL
        assert engine.config.prompt_count == 2000
    
    def test_comprehensive_test_factory(self):
        engine = BenchmarkEngine.comprehensive_test(Domain.FINANCIAL)
        assert engine.config.mode == BenchmarkMode.COMPREHENSIVE
        assert engine.config.domain == Domain.FINANCIAL
        assert engine.config.prompt_count == 8000
        assert len(engine.config.comparison_llms) >= 3
    
    def test_comprehensive_custom_llms(self):
        llms = ["claude-3-5-sonnet", "gpt-4o"]
        engine = BenchmarkEngine.comprehensive_test(llms=llms)
        assert engine.config.comparison_llms == llms
    
    def test_estimate_cost(self):
        engine = BenchmarkEngine.quick_test()
        cost = engine.estimate_cost()
        assert "total_usd" in cost
        assert "breakdown" in cost
    
    def test_get_mode_info(self):
        engine = BenchmarkEngine.standard_test()
        info = engine.get_mode_info()
        assert "prompts_per_run" in info
        assert info["prompts_per_run"] == 2000
    
    def test_generate_rubric_medical(self):
        engine = BenchmarkEngine()
        rubric = engine.generate_rubric(Domain.MEDICAL)
        
        assert rubric.domain == Domain.MEDICAL
        assert len(rubric.dimensions) == 10
        assert len(rubric.red_flags) > 0
        assert len(rubric.green_flags) > 0
    
    def test_generate_rubric_legal(self):
        engine = BenchmarkEngine()
        rubric = engine.generate_rubric(Domain.LEGAL)
        assert rubric.domain == Domain.LEGAL
    
    def test_generate_rubric_caching(self):
        engine = BenchmarkEngine()
        rubric1 = engine.generate_rubric(Domain.MEDICAL)
        rubric2 = engine.generate_rubric(Domain.MEDICAL)
        assert rubric1 is rubric2  # Same object (cached)
    
    def test_generate_prompts_count_quick(self):
        engine = BenchmarkEngine.quick_test()
        corpus = engine.generate_prompts(Domain.MEDICAL)
        assert corpus.total_count == 50
    
    def test_generate_prompts_count_standard(self):
        engine = BenchmarkEngine.standard_test()
        corpus = engine.generate_prompts(Domain.MEDICAL)
        assert corpus.total_count == 2000
    
    def test_generate_prompts_distribution_standard(self):
        engine = BenchmarkEngine.standard_test()
        corpus = engine.generate_prompts(Domain.MEDICAL)
        
        assert corpus.public_count == 1000  # 50%
        assert corpus.synthetic_count == 700  # 35%
        assert corpus.red_team_count == 300   # 15%
    
    def test_generate_prompts_domain(self):
        engine = BenchmarkEngine()
        corpus = engine.generate_prompts(Domain.LEGAL)
        assert corpus.domain == Domain.LEGAL
        assert all(p.domain == Domain.LEGAL for p in corpus.prompts)
    
    def test_score_output_basic(self):
        engine = BenchmarkEngine()
        rubric = engine.generate_rubric(Domain.MEDICAL)
        
        output = "Based on the evidence, I recommend consulting a physician. The confidence interval is approximately 85% (±10%). However, there are limitations to this assessment."
        
        score = engine.score_output(output, rubric)
        
        assert len(score.dimensions) == 10
        assert score.final_score > 0
    
    def test_score_output_with_red_flags(self):
        engine = BenchmarkEngine()
        rubric = engine.generate_rubric(Domain.MEDICAL)
        
        output = "PMID: 12345678 definitely proves this treatment works with no doubt."
        
        score = engine.score_output(output, rubric)
        
        # Should detect hallucination indicators
        assert score.red_flag_deductions <= 0  # Some red flags may be detected
    
    def test_generate_system_prompt_full(self):
        engine = BenchmarkEngine()
        prompt = engine.generate_system_prompt(compact=False)
        
        assert "BENCHMARK_ENGINE v1.0" in prompt
        assert "METIS" in prompt
        assert "10 DIMENSIONS" in prompt
    
    def test_generate_system_prompt_compact(self):
        engine = BenchmarkEngine()
        prompt = engine.generate_system_prompt(compact=True)
        
        assert "COMPACT" in prompt
        assert len(prompt) < 1000  # Should be shorter
    
    def test_repr(self):
        engine = BenchmarkEngine()
        assert "BenchmarkEngine" in repr(engine)
        assert "2.0.0" in repr(engine)


class TestCertificate:
    """Tests for Certificate generation."""
    
    def test_certificate_creation(self):
        engine = BenchmarkEngine()
        cert = engine.generate_certificate(
            holder_name="Test Engine v1.0",
            level=CertificationLevel.ADVANCED,
            domain=Domain.MEDICAL,
            score=240.0
        )
        
        assert cert.holder_name == "Test Engine v1.0"
        assert cert.level == CertificationLevel.ADVANCED
        assert cert.domain == Domain.MEDICAL
        assert cert.score == 240.0
        assert cert.qr_code_data.startswith("https://")
        assert len(cert.hash) == 64  # SHA-256 hex
    
    def test_certificate_validity(self):
        engine = BenchmarkEngine()
        cert = engine.generate_certificate(
            holder_name="Test",
            level=CertificationLevel.BASIC,
            domain=Domain.LEGAL,
            score=190.0
        )
        
        assert cert.is_valid()
        assert cert.expiry_date > cert.issued_date


class TestGraderCalibration:
    """Tests for grader calibration."""
    
    def test_calibration_master(self):
        engine = BenchmarkEngine()
        
        # Create master scores
        master_scores = []
        for _ in range(3):
            dimensions = [
                DimensionScore(
                    dimension_number=i+1,
                    dimension_name=f"Dim{i}",
                    dq1=DQScore(1, ScoreGrade.B, 2, ""),
                    dq2=DQScore(2, ScoreGrade.B, 2, ""),
                    dq3=DQScore(3, ScoreGrade.B, 2, "")
                ) for i in range(10)
            ]
            master_scores.append(PSAScore(dimensions=dimensions))
        
        # Grader responses very close to master
        responses = [
            {"score": master_scores[i].final_score + 2} 
            for i in range(3)
        ]
        
        result = engine.calibrate_grader(
            grader_id="grader-001",
            domain=Domain.MEDICAL,
            responses=responses,
            master_scores=master_scores
        )
        
        assert result.passed
        assert result.delta_score < 0.15


class TestIntegration:
    """Integration tests."""
    
    def test_full_rubric_and_prompt_generation_quick(self):
        engine = BenchmarkEngine.quick_test(Domain.MEDICAL)
        
        rubric = engine.generate_rubric(Domain.MEDICAL)
        corpus = engine.generate_prompts(Domain.MEDICAL)
        
        assert rubric.domain == Domain.MEDICAL
        assert corpus.domain == Domain.MEDICAL
        assert corpus.total_count == 50  # Quick mode
        
        # Score a sample prompt
        sample_output = "Consult a physician for proper diagnosis. Approximately 80% confidence."
        score = engine.score_output(sample_output, rubric)
        
        assert score.final_score >= 0
        assert score.percentage >= 0
    
    def test_full_rubric_and_prompt_generation_standard(self):
        engine = BenchmarkEngine.standard_test(Domain.MEDICAL)
        
        rubric = engine.generate_rubric(Domain.MEDICAL)
        corpus = engine.generate_prompts(Domain.MEDICAL)
        
        assert rubric.domain == Domain.MEDICAL
        assert corpus.domain == Domain.MEDICAL
        assert corpus.total_count == 2000  # Standard mode
    
    def test_cross_domain_rubrics(self):
        engine = BenchmarkEngine()
        
        domains = [Domain.MEDICAL, Domain.LEGAL, Domain.FINANCIAL, Domain.SECURITY]
        
        for domain in domains:
            rubric = engine.generate_rubric(domain)
            assert rubric.domain == domain
            assert len(rubric.dimensions) == 10
    
    def test_format_output(self):
        engine = BenchmarkEngine()
        rubric = engine.generate_rubric(Domain.MEDICAL)
        corpus = engine.generate_prompts(Domain.MEDICAL)
        
        # We can't run full evaluation without API, but we can test format
        from benchmark_engine.types import BenchmarkReport, BenchmarkMetrics
        
        metrics = BenchmarkMetrics(
            total_prompts=1531,
            mean_baseline_score=180.0,
            mean_engine_score=260.0,
            mean_risk_reduction=0.83,
            std_risk_reduction=0.05,
            confidence_interval_lower=0.78,
            confidence_interval_upper=0.88,
            hallucination_rate_baseline=0.25,
            hallucination_rate_engine=0.05,
            safety_score=0.94
        )
        
        report = BenchmarkReport(
            target_engine="medical-engine-v2.5",
            domain=Domain.MEDICAL,
            timestamp=datetime.now(),
            config=engine.config,
            corpus=corpus,
            results=[],
            metrics=metrics,
            certification_level=CertificationLevel.MASTER
        )
        
        formatted = engine.format_output(report)
        assert "BENCHMARK REPORT" in formatted
        assert "MASTER" in formatted
        assert "83" in formatted  # Risk reduction percentage


class TestTrinityScoring:
    """Tests for v2.0 Trinity Scoring integration (Oracle Layer)."""
    
    def test_trinity_scoring_import(self):
        from benchmark_engine.integrations.trinity_scoring import (
            TrinityScoring, TrinityJudge, TrinityVerdict, JudgeRole
        )
        assert TrinityScoring is not None
        assert JudgeRole.ADVOCATE.value == "advocate"
        assert JudgeRole.SKEPTIC.value == "skeptic"
        assert JudgeRole.ARBITER.value == "arbiter"
    
    def test_trinity_scoring_initialization(self):
        from benchmark_engine.integrations.trinity_scoring import TrinityScoring
        
        trinity = TrinityScoring()
        assert trinity.VERSION == "2.0.0"
    
    def test_evaluate_dimension(self):
        from benchmark_engine.integrations.trinity_scoring import TrinityScoring
        
        trinity = TrinityScoring()
        verdict = trinity.evaluate_dimension(
            dimension_number=1,
            dimension_name="Falsifiability",
            question="Can the claim be tested?",
            output="The patient should consult a physician for proper diagnosis."
        )
        
        assert verdict.dimension_number == 1
        assert verdict.dimension_name == "Falsifiability"
        assert 0 <= verdict.consensus_score <= 30
        assert 0 <= verdict.advocate_score <= 30
        assert 0 <= verdict.skeptic_score <= 30
        assert 0 <= verdict.arbiter_score <= 30
    
    def test_verdict_is_unanimous(self):
        from benchmark_engine.integrations.trinity_scoring import TrinityScoring
        
        trinity = TrinityScoring()
        verdict = trinity.evaluate_dimension(
            dimension_number=2,
            dimension_name="Explainability",
            question="Is the reasoning transparent?",
            output="Test output"
        )
        
        assert hasattr(verdict, 'is_unanimous')
        assert isinstance(verdict.is_unanimous, bool)
    
    def test_agreement_levels(self):
        from benchmark_engine.integrations.trinity_scoring import TrinityScoring
        
        trinity = TrinityScoring()
        verdict = trinity.evaluate_dimension(
            dimension_number=3,
            dimension_name="Uncertainty",
            question="Are confidence levels stated?",
            output="Test output with 80% confidence"
        )
        
        assert verdict.agreement_level in [
            "UNANIMOUS", "STRONG_CONSENSUS", 
            "MODERATE_CONSENSUS", "SPLIT_DECISION"
        ]
    
    def test_confidence_interval(self):
        from benchmark_engine.integrations.trinity_scoring import TrinityScoring
        
        trinity = TrinityScoring()
        verdict = trinity.evaluate_dimension(
            dimension_number=4,
            dimension_name="Error Recovery",
            question="Does it fail safely?",
            output="Test output"
        )
        
        assert len(verdict.confidence_interval) == 2
        assert verdict.confidence_interval[0] <= verdict.confidence_interval[1]
    
    def test_format_verdict(self):
        from benchmark_engine.integrations.trinity_scoring import TrinityScoring
        
        trinity = TrinityScoring()
        verdict = trinity.evaluate_dimension(
            dimension_number=5,
            dimension_name="Value Alignment",
            question="Does it respect human agency?",
            output="Test output"
        )
        
        formatted = trinity.format_verdict(verdict)
        assert "TRINITY VERDICT" in formatted
        assert "Value Alignment" in formatted
        assert "CONSENSUS" in formatted
    
    def test_engine_trinity_integration(self):
        engine = BenchmarkEngine.quick_test(Domain.MEDICAL)
        
        assert hasattr(engine, '_trinity_scoring')
        assert engine._trinity_scoring is not None


class TestBenchmarkFreshness:
    """Tests for v2.0 Benchmark Freshness integration (Credibility Engine)."""
    
    def test_freshness_import(self):
        from benchmark_engine.integrations.benchmark_freshness import (
            BenchmarkFreshness, FreshnessScore, DecayModel, ValidityStatus
        )
        assert BenchmarkFreshness is not None
        assert DecayModel.EXPONENTIAL.value == "exponential"
        assert ValidityStatus.FRESH.value == "fresh"
    
    def test_freshness_initialization(self):
        from benchmark_engine.integrations.benchmark_freshness import BenchmarkFreshness
        
        freshness = BenchmarkFreshness()
        assert freshness.VERSION == "2.0.0"
    
    def test_calculate_freshness_recent(self):
        from benchmark_engine.integrations.benchmark_freshness import (
            BenchmarkFreshness, ValidityStatus
        )
        
        freshness = BenchmarkFreshness()
        score = freshness.calculate_freshness(
            benchmark_id="BM-2024-001",
            domain="medical",
            benchmark_date=datetime.now()
        )
        
        assert score.benchmark_id == "BM-2024-001"
        assert score.domain == "medical"
        assert score.validity_status == ValidityStatus.FRESH
        assert score.freshness_percentage >= 99
    
    def test_calculate_freshness_old(self):
        from datetime import timedelta
        from benchmark_engine.integrations.benchmark_freshness import (
            BenchmarkFreshness, ValidityStatus
        )
        
        freshness = BenchmarkFreshness()
        old_date = datetime.now() - timedelta(days=365)
        
        score = freshness.calculate_freshness(
            benchmark_id="BM-OLD-001",
            domain="medical",
            benchmark_date=old_date
        )
        
        assert score.freshness_percentage < 50
        assert score.validity_status in [
            ValidityStatus.AGING, ValidityStatus.STALE, ValidityStatus.EXPIRED
        ]
    
    def test_domain_half_lives(self):
        from benchmark_engine.integrations.benchmark_freshness import DOMAIN_HALF_LIVES
        
        assert "medical" in DOMAIN_HALF_LIVES
        assert "legal" in DOMAIN_HALF_LIVES
        assert "financial" in DOMAIN_HALF_LIVES
        
        assert DOMAIN_HALF_LIVES["medical"] == 90
        assert DOMAIN_HALF_LIVES["security"] == 60
    
    def test_decay_models(self):
        from benchmark_engine.integrations.benchmark_freshness import (
            BenchmarkFreshness, DecayModel
        )
        from datetime import timedelta
        
        freshness = BenchmarkFreshness()
        date_90_days_ago = datetime.now() - timedelta(days=90)
        
        exp_score = freshness.calculate_freshness(
            benchmark_id="EXP-001",
            domain="general",
            benchmark_date=date_90_days_ago,
            model=DecayModel.EXPONENTIAL
        )
        
        linear_score = freshness.calculate_freshness(
            benchmark_id="LIN-001",
            domain="general",
            benchmark_date=date_90_days_ago,
            model=DecayModel.LINEAR
        )
        
        assert exp_score.decay_model == DecayModel.EXPONENTIAL
        assert linear_score.decay_model == DecayModel.LINEAR
    
    def test_freshness_score_properties(self):
        from benchmark_engine.integrations.benchmark_freshness import BenchmarkFreshness
        
        freshness = BenchmarkFreshness()
        score = freshness.calculate_freshness(
            benchmark_id="BM-PROP-001",
            domain="medical",
            benchmark_date=datetime.now()
        )
        
        assert hasattr(score, 'freshness_percentage')
        assert hasattr(score, 'is_valid')
        assert hasattr(score, 'days_until_stale')
        
        assert score.is_valid == True
    
    def test_format_freshness_report(self):
        from benchmark_engine.integrations.benchmark_freshness import BenchmarkFreshness
        
        freshness = BenchmarkFreshness()
        score = freshness.calculate_freshness(
            benchmark_id="BM-FMT-001",
            domain="legal",
            benchmark_date=datetime.now()
        )
        
        formatted = freshness.format_freshness_report(score)
        assert "BENCHMARK FRESHNESS REPORT" in formatted
        assert "BM-FMT-001" in formatted
        assert "LEGAL" in formatted
    
    def test_engine_freshness_integration(self):
        engine = BenchmarkEngine.quick_test(Domain.MEDICAL)
        
        assert hasattr(engine, '_benchmark_freshness')
        assert engine._benchmark_freshness is not None


class TestAudienceReports:
    """Tests for v2.0 Audience Reports integration (Explanation Engine)."""
    
    def test_audience_reports_import(self):
        from benchmark_engine.integrations.audience_reports import (
            AudienceReports, AudienceLevel, ReportFormat, FormattedReport
        )
        assert AudienceReports is not None
        assert AudienceLevel.EXECUTIVE.value == "executive"
        assert AudienceLevel.TECHNICAL.value == "technical"
        assert AudienceLevel.COMPLIANCE.value == "compliance"
    
    def test_audience_reports_initialization(self):
        from benchmark_engine.integrations.audience_reports import AudienceReports
        
        reports = AudienceReports()
        assert reports.VERSION == "2.0.0"
    
    def test_executive_report(self):
        from benchmark_engine.integrations.audience_reports import (
            AudienceReports, AudienceLevel
        )
        
        reports = AudienceReports()
        benchmark_data = {
            "target_engine": "medical-engine-v2.5",
            "domain": "medical",
            "certification_level": "master",
            "metrics": {
                "mean_baseline_score": 180.0,
                "mean_engine_score": 260.0,
                "mean_risk_reduction": 0.83,
                "std_risk_reduction": 0.05,
                "confidence_interval_lower": 0.78,
                "confidence_interval_upper": 0.88,
                "total_prompts": 1531,
                "hallucination_rate_baseline": 0.25,
                "hallucination_rate_engine": 0.05,
                "safety_score": 0.85,
            }
        }
        
        report = reports.generate_report(benchmark_data, AudienceLevel.EXECUTIVE)
        
        assert report.audience == AudienceLevel.EXECUTIVE
        assert "medical-engine-v2.5" in report.title
        assert len(report.sections) > 0
        assert "MASTER" in report.key_metrics["Certification Level"]
    
    def test_technical_report(self):
        from benchmark_engine.integrations.audience_reports import (
            AudienceReports, AudienceLevel
        )
        
        reports = AudienceReports()
        benchmark_data = {
            "target_engine": "test-engine",
            "domain": "general",
            "certification_level": "advanced",
            "metrics": {
                "mean_baseline_score": 180.0,
                "mean_engine_score": 250.0,
                "mean_risk_reduction": 0.78,
                "std_risk_reduction": 0.06,
                "confidence_interval_lower": 0.70,
                "confidence_interval_upper": 0.86,
                "total_prompts": 2000,
                "hallucination_rate_baseline": 0.20,
                "hallucination_rate_engine": 0.05,
                "safety_score": 0.80,
            }
        }
        
        report = reports.generate_report(benchmark_data, AudienceLevel.TECHNICAL)
        
        assert report.audience == AudienceLevel.TECHNICAL
        assert any("Methodology" in s.title for s in report.sections)
    
    def test_compliance_report(self):
        from benchmark_engine.integrations.audience_reports import (
            AudienceReports, AudienceLevel
        )
        
        reports = AudienceReports()
        benchmark_data = {
            "target_engine": "compliance-test-engine",
            "domain": "financial",
            "certification_level": "basic",
            "metrics": {
                "mean_baseline_score": 180.0,
                "mean_engine_score": 200.0,
                "mean_risk_reduction": 0.65,
                "std_risk_reduction": 0.08,
                "confidence_interval_lower": 0.55,
                "confidence_interval_upper": 0.75,
                "total_prompts": 1000,
                "hallucination_rate_baseline": 0.30,
                "hallucination_rate_engine": 0.12,
                "safety_score": 0.65,
            }
        }
        
        report = reports.generate_report(benchmark_data, AudienceLevel.COMPLIANCE)
        
        assert report.audience == AudienceLevel.COMPLIANCE
        assert any("Audit" in s.title for s in report.sections)
    
    def test_report_to_markdown(self):
        from benchmark_engine.integrations.audience_reports import (
            AudienceReports, AudienceLevel
        )
        
        reports = AudienceReports()
        benchmark_data = {
            "target_engine": "test-engine",
            "domain": "medical",
            "certification_level": "master",
            "metrics": {
                "mean_baseline_score": 180.0,
                "mean_engine_score": 260.0,
                "mean_risk_reduction": 0.83,
                "std_risk_reduction": 0.05,
                "confidence_interval_lower": 0.78,
                "confidence_interval_upper": 0.88,
                "total_prompts": 1531,
                "hallucination_rate_baseline": 0.25,
                "hallucination_rate_engine": 0.05,
                "safety_score": 0.85,
            }
        }
        
        report = reports.generate_report(benchmark_data, AudienceLevel.EXECUTIVE)
        markdown = report.to_markdown()
        
        assert "# " in markdown  # Has H1 heading
        assert "## " in markdown  # Has H2 headings
        assert "Key Metrics" in markdown
    
    def test_word_count(self):
        from benchmark_engine.integrations.audience_reports import (
            AudienceReports, AudienceLevel
        )
        
        reports = AudienceReports()
        benchmark_data = {
            "target_engine": "test-engine",
            "domain": "medical",
            "certification_level": "master",
            "metrics": {
                "mean_baseline_score": 180.0,
                "mean_engine_score": 260.0,
                "mean_risk_reduction": 0.83,
                "std_risk_reduction": 0.05,
                "confidence_interval_lower": 0.78,
                "confidence_interval_upper": 0.88,
                "total_prompts": 1531,
                "hallucination_rate_baseline": 0.25,
                "hallucination_rate_engine": 0.05,
                "safety_score": 0.85,
            }
        }
        
        report = reports.generate_report(benchmark_data, AudienceLevel.EXECUTIVE)
        
        assert report.word_count > 0
    
    def test_engine_audience_reports_integration(self):
        engine = BenchmarkEngine.quick_test(Domain.MEDICAL)
        
        assert hasattr(engine, '_audience_reports')
        assert engine._audience_reports is not None


class TestV2Integration:
    """Tests for v2.0 full integration in BenchmarkEngine."""
    
    def test_engine_version(self):
        engine = BenchmarkEngine()
        assert engine.VERSION == "2.0.0"
        assert engine.CODENAME == "METIS-II"
    
    def test_all_integrations_initialized(self):
        engine = BenchmarkEngine()
        
        assert hasattr(engine, '_trinity_scoring')
        assert hasattr(engine, '_benchmark_freshness')
        assert hasattr(engine, '_audience_reports')
    
    def test_trinity_summary(self):
        from benchmark_engine.integrations.trinity_scoring import TrinityScoring
        
        engine = BenchmarkEngine.quick_test(Domain.MEDICAL)
        trinity = TrinityScoring()
        
        verdicts = [
            trinity.evaluate_dimension(
                dimension_number=i+1,
                dimension_name=f"Dimension {i+1}",
                question=f"Question {i+1}?",
                output="Test output"
            )
            for i in range(3)
        ]
        
        summary = engine.get_trinity_summary(verdicts)
        
        assert "total_dimensions" in summary
        assert summary["total_dimensions"] == 3
        assert "consensus_total" in summary
        assert "consensus_percentage" in summary
    
    def test_trinity_summary_empty(self):
        engine = BenchmarkEngine.quick_test(Domain.MEDICAL)
        
        summary = engine.get_trinity_summary([])
        
        assert "error" in summary
    
    def test_full_v2_workflow(self):
        from benchmark_engine.types import BenchmarkReport, BenchmarkMetrics
        from benchmark_engine.integrations.audience_reports import AudienceLevel
        
        engine = BenchmarkEngine.quick_test(Domain.MEDICAL)
        rubric = engine.generate_rubric(Domain.MEDICAL)
        corpus = engine.generate_prompts(Domain.MEDICAL)
        
        metrics = BenchmarkMetrics(
            total_prompts=50,
            mean_baseline_score=180.0,
            mean_engine_score=260.0,
            mean_risk_reduction=0.83,
            std_risk_reduction=0.05,
            confidence_interval_lower=0.78,
            confidence_interval_upper=0.88,
            hallucination_rate_baseline=0.25,
            hallucination_rate_engine=0.05,
            safety_score=0.94
        )
        
        report = BenchmarkReport(
            target_engine="medical-engine-v2.5",
            domain=Domain.MEDICAL,
            timestamp=datetime.now(),
            config=engine.config,
            corpus=corpus,
            results=[],
            metrics=metrics,
            certification_level=CertificationLevel.MASTER
        )
        
        freshness = engine.check_freshness(report)
        assert freshness.is_valid
        
        expiry = engine.get_certificate_expiry(report)
        assert expiry > datetime.now()
        
        exec_report = engine.generate_audience_report(report, AudienceLevel.EXECUTIVE)
        assert exec_report is not None
        assert exec_report.audience == AudienceLevel.EXECUTIVE
