"""
DECISION ENGINE v1.0 - Test Suite
==================================

Comprehensive tests for the Decision Engine.
"""

import pytest
from decision_engine import (
    DecisionEngine, DecisionConfig, AnalysisMode,
    BiasType, BiasAssessment, DebiasingStrategy,
    AspirationalLevel, SatisficingResult,
    FragilityCategory, OptionalityScore,
    TemporalPhase, TemporalVerdict, TemporalAlignment,
    EthicalVerdict, StakeholderImpact
)
from decision_engine.frameworks.kahneman import KahnemanFramework
from decision_engine.frameworks.simon import SimonFramework
from decision_engine.frameworks.taleb import TalebFramework
from decision_engine.frameworks.bergson import BergsonFramework
from decision_engine.frameworks.rawls_singer import RawlsSingerFramework
from decision_engine.scoring import ConfidenceLevel, TimelineVerdict, MoralCircle


class TestBiasDetection:
    """Test Kahneman bias detection."""
    
    def test_detect_anchoring(self):
        biases = KahnemanFramework.detect_biases("They first offered me $50k")
        assert BiasType.ANCHORING in biases
    
    def test_detect_loss_aversion(self):
        biases = KahnemanFramework.detect_biases("I might lose my current benefits")
        assert BiasType.LOSS_AVERSION in biases
    
    def test_detect_sunk_cost(self):
        biases = KahnemanFramework.detect_biases("I've already invested 5 years here")
        assert BiasType.SUNK_COST in biases
    
    def test_detect_overconfidence(self):
        biases = KahnemanFramework.detect_biases("I'm definitely sure this will work")
        assert BiasType.OVERCONFIDENCE in biases
    
    def test_detect_multiple_biases(self):
        text = "I've spent years here and I'm definitely sure changing is risky"
        biases = KahnemanFramework.detect_biases(text)
        assert len(biases) >= 2
    
    def test_no_biases_detected(self):
        biases = KahnemanFramework.detect_biases("What are my options?")
        assert len(biases) == 0
    
    def test_debiasing_strategy(self):
        strategy = KahnemanFramework.get_debiasing_strategy(BiasType.SUNK_COST)
        assert "If I hadn't invested" in strategy.strategy
    
    def test_premortem_analysis(self):
        causes = KahnemanFramework.run_premortem("Start a business")
        assert len(causes) >= 3
        assert any(c.probability > 0 for c in causes)
    
    def test_full_bias_assessment(self):
        assessment = KahnemanFramework.analyze("I've already invested so much time")
        assert isinstance(assessment, BiasAssessment)
        assert BiasType.SUNK_COST in assessment.detected_biases


class TestSatisficing:
    """Test Simon satisficing framework."""
    
    def test_assess_reversibility_high(self):
        rev = SimonFramework.assess_reversibility("Let me try this for a month")
        assert rev == "high"
    
    def test_assess_reversibility_low(self):
        rev = SimonFramework.assess_reversibility("This marriage decision")
        assert rev == "low"
    
    def test_assess_reversibility_medium(self):
        rev = SimonFramework.assess_reversibility("Should I change jobs?")
        assert rev == "medium"
    
    def test_derive_aspiration_levels(self):
        result = SimonFramework.analyze(
            "Should I start a business?",
            minimum="Cover living expenses",
            target="$150K revenue",
            stretch="$1M revenue"
        )
        assert result.minimum_outcome == "Cover living expenses"
        assert result.target_outcome == "$150K revenue"
    
    def test_stopping_rule_selection(self):
        result = SimonFramework.analyze("Quick experiment to try")
        assert "first" in result.search_stopping_rule.lower() or "good enough" in result.search_stopping_rule.lower()


class TestAntifragility:
    """Test Taleb antifragility framework."""
    
    def test_classify_fragile(self):
        fragility = TalebFramework.classify_fragility("Put all in one stock")
        assert fragility == FragilityCategory.FRAGILE
    
    def test_classify_antifragile(self):
        fragility = TalebFramework.classify_fragility("Learn and grow from challenges")
        assert fragility == FragilityCategory.ANTIFRAGILE
    
    def test_classify_robust(self):
        fragility = TalebFramework.classify_fragility("Maintain current position")
        assert fragility == FragilityCategory.ROBUST
    
    def test_assess_optionality_high(self):
        opt = TalebFramework.assess_optionality("Limited downside with no ceiling on upside")
        assert opt == "HIGH"
    
    def test_generate_black_swans(self):
        swans = TalebFramework.generate_black_swans("Start a business")
        assert len(swans) >= 3
    
    def test_barbell_assessment(self):
        barbell = TalebFramework.assess_barbell("Side experiment while keeping job")
        assert "ALIGNED" in barbell
    
    def test_via_negativa(self):
        suggestions = TalebFramework.suggest_via_negativa("Start a business")
        assert len(suggestions) > 0
    
    def test_full_optionality_score(self):
        score = TalebFramework.analyze("Diversify options and learn")
        assert isinstance(score, OptionalityScore)


class TestTemporalAssessment:
    """Test Bergson temporal framework."""
    
    def test_detect_ripeness(self):
        phase = BergsonFramework.detect_phase("The right time to act now")
        assert phase == TemporalPhase.RIPENESS
    
    def test_detect_decay(self):
        phase = BergsonFramework.detect_phase("Window is closing, last chance")
        assert phase == TemporalPhase.DECAY
    
    def test_detect_gestation(self):
        phase = BergsonFramework.detect_phase("Idea not yet fully formed")
        assert phase == TemporalPhase.GESTATION
    
    def test_assess_external_readiness(self):
        score = BergsonFramework.assess_external_readiness("Market growing with opportunity")
        assert score > 5.0
    
    def test_assess_internal_readiness(self):
        score = BergsonFramework.assess_internal_readiness("I feel ready and prepared")
        assert score > 5.0
    
    def test_determine_verdict_act_now(self):
        verdict = BergsonFramework.determine_verdict(TemporalPhase.RIPENESS, 8.0, 8.0)
        assert verdict == TemporalVerdict.ACT_NOW
    
    def test_determine_verdict_wait(self):
        verdict = BergsonFramework.determine_verdict(TemporalPhase.EMERGENCE, 4.0, 7.0)
        assert verdict == TemporalVerdict.WAIT
    
    def test_full_temporal_analysis(self):
        alignment = BergsonFramework.analyze("Ready to act now in favorable market")
        assert isinstance(alignment, TemporalAlignment)


class TestEthicalValidation:
    """Test Rawls/Singer ethical framework."""
    
    def test_map_stakeholders(self):
        stakeholders = RawlsSingerFramework.map_stakeholders("Change job affecting family")
        names = [s.stakeholder for s in stakeholders]
        assert "Family/Partner" in names or any("family" in s.lower() for s in names)
    
    def test_identify_least_advantaged(self):
        stakeholders = [
            StakeholderImpact("Self", "beneficiary", 50, ""),
            StakeholderImpact("Children", "voiceless", -30, "")
        ]
        least = RawlsSingerFramework.identify_least_advantaged(stakeholders)
        assert least == "Children"
    
    def test_veil_of_ignorance_passes(self):
        stakeholders = [
            StakeholderImpact("Self", "beneficiary", 50, ""),
            StakeholderImpact("Others", "affected", -10, "")
        ]
        passes = RawlsSingerFramework.veil_of_ignorance_test(stakeholders)
        assert passes == True
    
    def test_veil_of_ignorance_fails(self):
        stakeholders = [
            StakeholderImpact("Self", "beneficiary", 100, ""),
            StakeholderImpact("Others", "harmed", -60, "")
        ]
        passes = RawlsSingerFramework.veil_of_ignorance_test(stakeholders)
        assert passes == False
    
    def test_calculate_utility(self):
        stakeholders = [
            StakeholderImpact("A", "beneficiary", 50, ""),
            StakeholderImpact("B", "harmed", -20, "")
        ]
        benefits, harms, net = RawlsSingerFramework.calculate_utility(stakeholders)
        assert benefits == 50
        assert harms == 20
        assert net == 30
    
    def test_moral_circle_expansive(self):
        circle = RawlsSingerFramework.assess_moral_circle("Impact on future generation")
        assert circle == MoralCircle.EXPANSIVE
    
    def test_full_ethical_assessment(self):
        assessment = RawlsSingerFramework.analyze("Business decision affecting family")
        assert assessment.verdict in [EthicalVerdict.JUST, EthicalVerdict.PROBLEMATIC, EthicalVerdict.UNJUST]


class TestDecisionConfig:
    """Test configuration options."""
    
    def test_default_config(self):
        config = DecisionConfig()
        assert config.mode == AnalysisMode.STANDARD
    
    def test_quick_config(self):
        config = DecisionConfig.quick()
        assert config.mode == AnalysisMode.QUICK
        assert config.enable_satisficing == False
    
    def test_deep_config(self):
        config = DecisionConfig.deep()
        assert config.mode == AnalysisMode.DEEP
        assert config.include_premortem == True


class TestDecisionEngine:
    """Test main Decision Engine."""
    
    def test_create_engine(self):
        engine = DecisionEngine()
        assert engine.config.mode == AnalysisMode.STANDARD
    
    def test_generate_prompt(self):
        engine = DecisionEngine()
        prompt = engine.generate_system_prompt()
        assert "DECISION_ENGINE" in prompt or "KAHNEMAN" in prompt
    
    def test_generate_compact_prompt(self):
        engine = DecisionEngine()
        prompt = engine.generate_system_prompt(compact=True)
        assert len(prompt) < 2000
    
    def test_analyze_decision(self):
        engine = DecisionEngine()
        analysis = engine.analyze("Should I quit my job to start a business?")
        assert analysis.decision_statement == "Should I quit my job to start a business?"
        assert analysis.recommendation is not None
    
    def test_analyze_with_stakeholders(self):
        engine = DecisionEngine()
        analysis = engine.analyze(
            "Should I relocate for work?",
            stakeholders=["Spouse", "Children", "Elderly parents"]
        )
        assert analysis.ethical_assessment is not None
    
    def test_quick_check(self):
        engine = DecisionEngine()
        analysis = engine.quick_check("Quick decision test")
        assert analysis.recommendation is not None
    
    def test_analysis_summary(self):
        engine = DecisionEngine()
        analysis = engine.analyze("Test decision")
        summary = analysis.summary()
        assert "DECISION ENGINE" in summary
    
    def test_confidence_levels(self):
        engine = DecisionEngine()
        analysis = engine.analyze("Learn and grow through diversified options")
        assert analysis.recommendation.confidence in [
            ConfidenceLevel.HIGH, ConfidenceLevel.MEDIUM,
            ConfidenceLevel.LOW, ConfidenceLevel.VERY_LOW
        ]
    
    def test_analysis_history(self):
        engine = DecisionEngine()
        engine.analyze("Decision 1")
        engine.analyze("Decision 2")
        history = engine.get_analysis_history()
        assert len(history) == 2
    
    def test_repr(self):
        engine = DecisionEngine()
        assert "standard" in repr(engine).lower()


class TestIntegration:
    """Integration tests."""
    
    def test_full_analysis_pipeline(self):
        engine = DecisionEngine(config=DecisionConfig.standard())
        
        analysis = engine.analyze(
            "Should I quit my stable job to start a risky business?",
            stakeholders=["Family", "Current employer"],
            minimum_outcome="Cover living expenses",
            target_outcome="Match current salary",
            stretch_outcome="Double income"
        )
        
        assert analysis.bias_assessment is not None
        assert analysis.satisficing_result is not None
        assert analysis.optionality_score is not None
        assert analysis.temporal_alignment is not None
        assert analysis.ethical_assessment is not None
        
        assert analysis.recommendation is not None
        assert len(analysis.recommendation.next_steps) > 0
        
        assert BiasType.LOSS_AVERSION in analysis.bias_assessment.detected_biases or \
               BiasType.STATUS_QUO in analysis.bias_assessment.detected_biases
    
    def test_deep_mode(self):
        engine = DecisionEngine(config=DecisionConfig.deep())
        analysis = engine.analyze("Major life decision")
        assert analysis.bias_assessment is not None
        assert len(analysis.bias_assessment.premortem_causes) > 0
    
    def test_framework_alignment_count(self):
        engine = DecisionEngine()
        analysis = engine.analyze("Learn and experiment with options ready to act")
        aligned = analysis.count_aligned_frameworks()
        assert 0 <= aligned <= 5
