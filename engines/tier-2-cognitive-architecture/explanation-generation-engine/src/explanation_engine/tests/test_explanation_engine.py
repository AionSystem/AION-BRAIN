"""
EXPLANATION ENGINE v1.0 - Test Suite
======================================

Comprehensive tests for the Explanation Engine.
"""

import pytest
from explanation_engine import (
    ExplanationEngine, ExplanationConfig,
    AudienceLevel, ExplanationStyle,
    Explanation, ExplanationLayer, CounterfactualExplanation,
    AudienceProfile, VerificationResult, ExplanationQuality
)
from explanation_engine.config import ExplanationDepth
from explanation_engine.types import LayerType, QualityLevel
from explanation_engine.generators.multi_level import MultiLevelGenerator
from explanation_engine.generators.counterfactual import CounterfactualGenerator
from explanation_engine.generators.audience import AudienceAdapter
from explanation_engine.generators.verification import ExplanationVerifier


class TestMultiLevelGenerator:
    """Test multi-level explanation generation."""
    
    def test_generate_headline(self):
        layer = MultiLevelGenerator.generate_headline(
            topic="Revenue Analysis",
            conclusion="Revenue exceeded targets",
            confidence=0.85
        )
        assert layer.layer_type == LayerType.HEADLINE
        assert "Revenue" in layer.content
    
    def test_generate_headline_low_confidence(self):
        layer = MultiLevelGenerator.generate_headline(
            topic="Forecast",
            conclusion="Growth expected",
            confidence=0.4
        )
        assert "uncertainty" in layer.content.lower()
    
    def test_generate_summary_executive(self):
        layer = MultiLevelGenerator.generate_summary(
            findings=["Strong sales", "Market expansion"],
            conclusion="Positive quarter",
            audience=AudienceProfile.executive()
        )
        assert "Bottom Line" in layer.content
    
    def test_generate_summary_general(self):
        layer = MultiLevelGenerator.generate_summary(
            findings=["Sales increased", "Costs reduced"],
            conclusion="Healthy business",
            audience=AudienceProfile.general()
        )
        assert "Overview" in layer.content
    
    def test_generate_key_factors(self):
        factors = [
            {"name": "Sales", "impact": "high", "direction": "positive"},
            {"name": "Costs", "impact": "medium", "direction": "negative"}
        ]
        layer = MultiLevelGenerator.generate_key_factors(
            factors=factors,
            audience=AudienceProfile.general()
        )
        assert layer.layer_type == LayerType.KEY_FACTORS
        assert "Sales" in layer.content
    
    def test_generate_evidence(self):
        evidence = [
            {"source": "Q3 Report", "data": "Revenue +15%"},
            {"source": "Market Analysis", "data": "Share +2%"}
        ]
        layer = MultiLevelGenerator.generate_evidence(evidence)
        assert layer.layer_type == LayerType.EVIDENCE
        assert "Q3 Report" in layer.content
    
    def test_generate_methodology(self):
        layer = MultiLevelGenerator.generate_methodology(
            steps=["Data collection", "Analysis", "Validation"],
            frameworks_used=["Statistical Analysis"]
        )
        assert layer.layer_type == LayerType.METHODOLOGY
    
    def test_generate_limitations(self):
        layer = MultiLevelGenerator.generate_limitations(
            limitations=["Limited sample size"],
            uncertainties=["Market volatility"]
        )
        assert layer.layer_type == LayerType.LIMITATIONS
    
    def test_generate_recommendations(self):
        layer = MultiLevelGenerator.generate_recommendations(
            recommendations=["Increase investment", "Monitor trends"],
            timeline="immediate"
        )
        assert layer.layer_type == LayerType.RECOMMENDATIONS
    
    def test_get_layers_for_depth_summary(self):
        layers = MultiLevelGenerator.get_layers_for_depth(ExplanationDepth.SUMMARY)
        assert LayerType.HEADLINE in layers
        assert LayerType.METHODOLOGY not in layers
    
    def test_get_layers_for_depth_comprehensive(self):
        layers = MultiLevelGenerator.get_layers_for_depth(ExplanationDepth.COMPREHENSIVE)
        assert LayerType.METHODOLOGY in layers
        assert LayerType.LIMITATIONS in layers


class TestCounterfactualGenerator:
    """Test counterfactual explanation generation."""
    
    def test_generate_counterfactual(self):
        cf = CounterfactualGenerator.generate_counterfactual(
            original_outcome="Growth achieved",
            factor_name="market conditions",
            factor_change="unfavorable",
            alternative_outcome="Growth would be limited",
            probability_shift=-0.25
        )
        assert isinstance(cf, CounterfactualExplanation)
        assert "market conditions" in cf.changed_factor
    
    def test_high_sensitivity_insight(self):
        cf = CounterfactualGenerator.generate_counterfactual(
            original_outcome="Success",
            factor_name="funding",
            factor_change="reduced by 50%",
            alternative_outcome="Failure likely",
            probability_shift=-0.40
        )
        assert "highly sensitive" in cf.insight.lower()
    
    def test_generate_sensitivity_analysis(self):
        factors = [
            {"name": "Price", "current_value": "$100", "alternative_value": "$80", "impact_if_changed": "Higher volume", "sensitivity": 0.25},
            {"name": "Quality", "current_value": "High", "alternative_value": "Medium", "impact_if_changed": "Lower retention", "sensitivity": 0.15}
        ]
        counterfactuals = CounterfactualGenerator.generate_sensitivity_analysis(
            outcome="Strong sales",
            factors=factors
        )
        assert len(counterfactuals) == 2
        assert counterfactuals[0].probability_shift >= counterfactuals[1].probability_shift
    
    def test_generate_decision_alternatives(self):
        alternatives = [
            {"alternative": "Option B", "expected_outcome": "Lower risk", "probability_shift": 0.15},
            {"alternative": "Option C", "expected_outcome": "Higher reward", "probability_shift": 0.30}
        ]
        counterfactuals = CounterfactualGenerator.generate_decision_alternatives(
            decision="Option A",
            outcome="Moderate success",
            alternatives=alternatives
        )
        assert len(counterfactuals) == 2


class TestAudienceAdapter:
    """Test audience adaptation."""
    
    def test_get_executive_profile(self):
        profile = AudienceAdapter.get_audience_profile(AudienceLevel.EXECUTIVE)
        assert profile.attention_span == "short"
        assert profile.decision_authority == True
    
    def test_get_technical_profile(self):
        profile = AudienceAdapter.get_audience_profile(AudienceLevel.TECHNICAL)
        assert profile.domain_knowledge == "deep"
    
    def test_simplify_text_general(self):
        text = "The multivariate analysis shows correlation"
        simplified = AudienceAdapter.simplify_text(text, AudienceLevel.GENERAL_PUBLIC)
        assert "looking at multiple factors" in simplified or "relationship" in simplified
    
    def test_simplify_text_technical(self):
        text = "The multivariate analysis shows correlation"
        result = AudienceAdapter.simplify_text(text, AudienceLevel.TECHNICAL)
        assert result == text
    
    def test_adjust_length_executive(self):
        long_content = "Para 1\n\nPara 2\n\nPara 3\n\nPara 4\n\nPara 5"
        adjusted = AudienceAdapter.adjust_length(long_content, AudienceLevel.EXECUTIVE)
        assert adjusted.count("\n\n") < long_content.count("\n\n")
    
    def test_add_emphasis_executive(self):
        content = "Key finding here"
        emphasized = AudienceAdapter.add_emphasis(content, AudienceLevel.EXECUTIVE)
        assert "BOTTOM LINE" in emphasized
    
    def test_adapt_layer(self):
        layer = ExplanationLayer(
            layer_type=LayerType.SUMMARY,
            content="Long technical explanation with multivariate analysis details"
        )
        adapted = AudienceAdapter.adapt_layer(layer, AudienceLevel.GENERAL_PUBLIC)
        assert "looking at multiple factors" in adapted.content


class TestExplanationVerifier:
    """Test explanation verification."""
    
    def test_check_logical_consistency(self):
        explanation = Explanation(
            topic="Test",
            audience=AudienceProfile.general(),
            layers=[
                ExplanationLayer(LayerType.HEADLINE, "Short headline", confidence=0.9),
                ExplanationLayer(LayerType.SUMMARY, "Longer summary with more details about the topic", confidence=0.85)
            ],
            counterfactuals=[]
        )
        score = ExplanationVerifier.check_logical_consistency(explanation)
        assert 0 <= score <= 1.0
    
    def test_check_completeness_standard(self):
        explanation = Explanation(
            topic="Test",
            audience=AudienceProfile.general(),
            layers=[
                ExplanationLayer(LayerType.HEADLINE, "Headline"),
                ExplanationLayer(LayerType.SUMMARY, "Summary"),
                ExplanationLayer(LayerType.KEY_FACTORS, "Factors"),
                ExplanationLayer(LayerType.RECOMMENDATIONS, "Recommendations")
            ],
            counterfactuals=[]
        )
        score = ExplanationVerifier.check_completeness(explanation, "standard")
        assert score > 0.5
    
    def test_check_audience_fit_short_attention(self):
        explanation = Explanation(
            topic="Test",
            audience=AudienceProfile.executive(),
            layers=[
                ExplanationLayer(LayerType.SUMMARY, "A" * 1000)
            ],
            counterfactuals=[]
        )
        score = ExplanationVerifier.check_audience_fit(explanation)
        assert score < 1.0
    
    def test_identify_issues_missing_headline(self):
        explanation = Explanation(
            topic="Test",
            audience=AudienceProfile.general(),
            layers=[
                ExplanationLayer(LayerType.SUMMARY, "Summary only")
            ],
            counterfactuals=[]
        )
        issues = ExplanationVerifier.identify_issues(explanation)
        assert any("headline" in issue.lower() for issue in issues)
    
    def test_generate_suggestions(self):
        explanation = Explanation(
            topic="Test",
            audience=AudienceProfile.general(),
            layers=[],
            counterfactuals=[]
        )
        issues = ExplanationVerifier.identify_issues(explanation)
        suggestions = ExplanationVerifier.generate_suggestions(explanation, issues)
        assert len(suggestions) > 0
    
    def test_verify_valid_explanation(self):
        explanation = Explanation(
            topic="Test",
            audience=AudienceProfile.general(),
            layers=[
                ExplanationLayer(LayerType.HEADLINE, "Clear headline", confidence=0.9),
                ExplanationLayer(LayerType.SUMMARY, "Good summary of key points", confidence=0.85),
                ExplanationLayer(LayerType.RECOMMENDATIONS, "1. Action 2. Action", confidence=0.8)
            ],
            counterfactuals=[]
        )
        result = ExplanationVerifier.verify(explanation)
        assert result.is_valid == True
    
    def test_assess_quality(self):
        explanation = Explanation(
            topic="Test",
            audience=AudienceProfile.general(),
            layers=[
                ExplanationLayer(LayerType.HEADLINE, "Headline", confidence=0.9),
                ExplanationLayer(LayerType.SUMMARY, "Summary", confidence=0.85)
            ],
            counterfactuals=[]
        )
        quality = ExplanationVerifier.assess_quality(explanation)
        assert quality.overall_level in list(QualityLevel)


class TestExplanationConfig:
    """Test configuration options."""
    
    def test_default_config(self):
        config = ExplanationConfig()
        assert config.include_counterfactuals == True
    
    def test_executive_config(self):
        config = ExplanationConfig.for_executives()
        assert config.audience_level == AudienceLevel.EXECUTIVE
        assert config.max_layers == 2
    
    def test_technical_config(self):
        config = ExplanationConfig.for_technical()
        assert config.audience_level == AudienceLevel.TECHNICAL
        assert config.depth == ExplanationDepth.COMPREHENSIVE


class TestExplanationEngine:
    """Test main Explanation Engine."""
    
    def test_create_engine(self):
        engine = ExplanationEngine()
        assert engine.VERSION == "1.0.0"
    
    def test_generate_explanation(self):
        engine = ExplanationEngine()
        explanation = engine.explain(
            topic="Q3 Performance",
            conclusion="Exceeded expectations",
            findings=["Revenue up 15%", "Costs down 5%"]
        )
        assert isinstance(explanation, Explanation)
        assert len(explanation.layers) > 0
    
    def test_generate_with_custom_config(self):
        engine = ExplanationEngine(config=ExplanationConfig.for_executives())
        explanation = engine.explain(
            topic="Executive Summary",
            conclusion="Strong quarter",
            findings=["Sales growth"]
        )
        assert explanation.audience.level == "executive"
    
    def test_adapt_for_audience(self):
        engine = ExplanationEngine()
        explanation = engine.explain(
            topic="Technical Report",
            conclusion="System optimized",
            findings=["Performance improved"]
        )
        adapted = engine.adapt_for_audience(explanation, AudienceLevel.GENERAL_PUBLIC)
        assert adapted.audience.level == "general"
    
    def test_add_counterfactuals(self):
        engine = ExplanationEngine(config=ExplanationConfig(include_counterfactuals=False))
        explanation = engine.explain(
            topic="Decision Analysis",
            conclusion="Option A recommended",
            findings=["Lower risk"]
        )
        
        scenarios = [
            {"name": "budget", "current_value": "high", "alternative_value": "low", "impact_if_changed": "scope reduced", "sensitivity": 0.30}
        ]
        updated = engine.add_counterfactuals(explanation, scenarios)
        assert len(updated.counterfactuals) > 0
    
    def test_verify_explanation(self):
        engine = ExplanationEngine()
        explanation = engine.explain(
            topic="Test",
            conclusion="Valid",
            findings=["Finding 1"]
        )
        result = engine.verify_explanation(explanation)
        assert isinstance(result, VerificationResult)
    
    def test_assess_quality(self):
        engine = ExplanationEngine()
        explanation = engine.explain(
            topic="Quality Test",
            conclusion="Good",
            findings=["Evidence 1", "Evidence 2"]
        )
        quality = engine.assess_quality(explanation)
        assert isinstance(quality, ExplanationQuality)
    
    def test_generate_prompt(self):
        engine = ExplanationEngine()
        prompt = engine.generate_system_prompt()
        assert "EXPLANATION" in prompt
    
    def test_compact_prompt(self):
        engine = ExplanationEngine()
        prompt = engine.generate_system_prompt(compact=True)
        assert len(prompt) < 2000
    
    def test_get_history(self):
        engine = ExplanationEngine()
        engine.explain("Topic 1", "Conclusion 1", ["Finding 1"])
        engine.explain("Topic 2", "Conclusion 2", ["Finding 2"])
        history = engine.get_history()
        assert len(history) == 2
    
    def test_explanation_summary(self):
        engine = ExplanationEngine()
        explanation = engine.explain(
            topic="Summary Test",
            conclusion="Complete",
            findings=["Point 1"]
        )
        summary = explanation.summary()
        assert "Summary Test" in summary
    
    def test_repr(self):
        engine = ExplanationEngine()
        assert "stakeholder" in repr(engine).lower()
    
    def test_format_output(self):
        engine = ExplanationEngine()
        explanation = engine.explain(
            topic="Test Topic",
            conclusion="Test conclusion reached",
            findings=["Finding 1", "Finding 2"]
        )
        formatted = engine.format_output(explanation)
        assert "EXPLANATION: Test Topic" in formatted
        assert "Audience:" in formatted
        assert "[HEADLINE]" in formatted
        assert "CLARITAS v1.0" in formatted
    
    def test_format_output_with_counterfactuals(self):
        engine = ExplanationEngine()
        explanation = engine.explain(
            topic="Decision Analysis",
            conclusion="Proceed with caution",
            findings=["Risk identified"],
            counterfactual_scenarios=[
                {"name": "market", "current_value": "stable", "alternative_value": "volatile", "impact_if_changed": "higher risk", "sensitivity": 0.35}
            ]
        )
        formatted = engine.format_output(explanation)
        assert "[COUNTERFACTUAL ANALYSIS]" in formatted
        assert "SENSITIVITY:" in formatted
    
    def test_format_output_verification_section(self):
        engine = ExplanationEngine()
        explanation = engine.explain(
            topic="Quality Test",
            conclusion="High quality",
            findings=["Evidence 1"]
        )
        formatted = engine.format_output(explanation)
        assert "[VERIFICATION]" in formatted
        assert "OVERALL QUALITY:" in formatted


class TestIntegration:
    """Integration tests."""
    
    def test_full_workflow(self):
        engine = ExplanationEngine(config=ExplanationConfig.for_stakeholders())
        
        explanation = engine.explain(
            topic="Market Entry Decision",
            conclusion="Proceed with caution - favorable conditions with manageable risks",
            findings=[
                "Market size is $5B with 8% CAGR",
                "Competition is fragmented",
                "Entry barriers are moderate"
            ],
            factors=[
                {"name": "Market Size", "impact": "high", "direction": "positive"},
                {"name": "Competition", "impact": "medium", "direction": "neutral"},
                {"name": "Entry Barriers", "impact": "medium", "direction": "negative"}
            ],
            recommendations=[
                "Conduct detailed market research",
                "Build partnership network",
                "Prepare phased entry strategy"
            ]
        )
        
        assert explanation.topic == "Market Entry Decision"
        assert len(explanation.layers) > 0
        assert explanation.quality is not None
        
        exec_version = engine.adapt_for_audience(explanation, AudienceLevel.EXECUTIVE)
        assert exec_version.audience.level == "executive"
        
        tech_version = engine.adapt_for_audience(explanation, AudienceLevel.TECHNICAL)
        assert tech_version.audience.level == "technical"
    
    def test_counterfactual_integration(self):
        engine = ExplanationEngine()
        
        explanation = engine.explain(
            topic="Investment Decision",
            conclusion="Invest in Project A",
            findings=["ROI of 25%", "Strategic alignment"],
            counterfactual_scenarios=[
                {"name": "Market conditions", "current_value": "favorable", "alternative_value": "recession", "impact_if_changed": "ROI drops to 10%", "sensitivity": 0.35},
                {"name": "Team capacity", "current_value": "full", "alternative_value": "half", "impact_if_changed": "Timeline doubles", "sensitivity": 0.20}
            ]
        )
        
        assert len(explanation.counterfactuals) >= 2
        sorted_by_sensitivity = sorted(explanation.counterfactuals, key=lambda x: abs(x.probability_shift), reverse=True)
        assert sorted_by_sensitivity[0].probability_shift >= sorted_by_sensitivity[-1].probability_shift
