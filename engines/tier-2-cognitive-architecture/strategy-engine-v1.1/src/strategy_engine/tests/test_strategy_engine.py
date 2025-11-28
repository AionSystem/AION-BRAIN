"""
STRATEGY ENGINE v1.1 - Test Suite
==================================

Comprehensive tests for the Strategy Engine.
"""

import pytest
from strategy_engine import (
    StrategyEngine, StrategyConfig, AnalysisMode,
    MoatDurabilityIndex, MoatStrength, CompetitorProfile,
    ResponseProbability, PayoffMatrix, EthicsFlag
)
from strategy_engine.config import OrganizationContext, StrategicPosition
from strategy_engine.scoring import EthicsAssessment
from strategy_engine.frameworks.sun_tzu import SunTzuFramework, TerrainAnalysis
from strategy_engine.frameworks.meadows import MeadowsFramework, LeveragePoint
from strategy_engine.frameworks.barabasi import BarabasiFramework, NetworkDynamics
from strategy_engine.frameworks.pearl import PearlFramework, CausalModel
from strategy_engine.frameworks.ostrom import OstromFramework, ResourceGovernance


class TestMoatDurabilityIndex:
    """Test Moat Durability Index calculations."""
    
    def test_create_moat(self):
        moat = MoatDurabilityIndex(imitation_difficulty=7, switching_costs=6)
        assert moat.imitation_difficulty == 7
        assert moat.switching_costs == 6
    
    def test_score_calculation(self):
        moat = MoatDurabilityIndex(
            imitation_difficulty=8,
            switching_costs=7,
            network_effects=6,
            scale_advantages=5,
            brand_trust=4,
            regulatory_moat=3
        )
        expected = 8*0.25 + 7*0.20 + 6*0.20 + 5*0.15 + 4*0.10 + 3*0.10
        assert abs(moat.score - expected) < 0.01
    
    def test_fortress_moat(self):
        moat = MoatDurabilityIndex(
            imitation_difficulty=9, switching_costs=9, network_effects=9,
            scale_advantages=8, brand_trust=8, regulatory_moat=8
        )
        assert moat.strength == MoatStrength.FORTRESS
        assert "10+" in moat.durability_years
    
    def test_strong_moat(self):
        moat = MoatDurabilityIndex(
            imitation_difficulty=7, switching_costs=7, network_effects=7,
            scale_advantages=6, brand_trust=6, regulatory_moat=5
        )
        assert moat.strength == MoatStrength.STRONG
    
    def test_moderate_moat(self):
        moat = MoatDurabilityIndex(
            imitation_difficulty=5, switching_costs=5, network_effects=5,
            scale_advantages=4, brand_trust=4, regulatory_moat=4
        )
        assert moat.strength == MoatStrength.MODERATE
    
    def test_weak_moat(self):
        moat = MoatDurabilityIndex(
            imitation_difficulty=3, switching_costs=3, network_effects=3,
            scale_advantages=2, brand_trust=2, regulatory_moat=2
        )
        assert moat.strength == MoatStrength.WEAK
    
    def test_no_moat(self):
        moat = MoatDurabilityIndex(
            imitation_difficulty=1, switching_costs=1, network_effects=1,
            scale_advantages=1, brand_trust=1, regulatory_moat=1
        )
        assert moat.strength == MoatStrength.NONE
    
    def test_weakest_dimensions(self):
        moat = MoatDurabilityIndex(
            imitation_difficulty=8, switching_costs=2, network_effects=7,
            scale_advantages=3, brand_trust=6, regulatory_moat=1
        )
        weakest = moat.get_weakest_dimensions(3)
        assert weakest[0][0] == "regulatory_moat"
        assert weakest[1][0] == "switching_costs"
    
    def test_invalid_score(self):
        with pytest.raises(ValueError):
            MoatDurabilityIndex(imitation_difficulty=15)


class TestCompetitorProfile:
    """Test competitor profiling."""
    
    def test_create_profile(self):
        profile = CompetitorProfile(
            name="Competitor A",
            posture="aggressive",
            resources="abundant"
        )
        assert profile.name == "Competitor A"
        assert profile.posture == "aggressive"
    
    def test_to_dict(self):
        profile = CompetitorProfile(name="Test", posture="defensive")
        d = profile.to_dict()
        assert d["name"] == "Test"
        assert d["posture"] == "defensive"


class TestPayoffMatrix:
    """Test game theory payoff matrix."""
    
    def test_default_matrix(self):
        matrix = PayoffMatrix()
        assert matrix.aggressive_aggressive == (-2, -2)
        assert matrix.passive_passive == (1, 1)
    
    def test_find_nash(self):
        matrix = PayoffMatrix()
        nash = matrix.find_nash_equilibrium()
        assert isinstance(nash, str)
    
    def test_recommend_strategy(self):
        matrix = PayoffMatrix()
        strategy = matrix.recommend_strategy()
        assert "strategy" in strategy.lower()


class TestEthicsAssessment:
    """Test ethical guardrails."""
    
    def test_green_flag(self):
        assessment = EthicsAssessment.assess(["grow market share", "improve product"])
        assert assessment.flag == EthicsFlag.GREEN
    
    def test_yellow_flag(self):
        assessment = EthicsAssessment.assess(["predatory pricing strategy"])
        assert assessment.flag in (EthicsFlag.YELLOW, EthicsFlag.RED)
    
    def test_red_flag(self):
        assessment = EthicsAssessment.assess([
            "predatory pricing",
            "regulatory capture",
            "monopolistic practices"
        ])
        assert assessment.flag == EthicsFlag.RED


class TestStrategyConfig:
    """Test configuration options."""
    
    def test_default_config(self):
        config = StrategyConfig()
        assert config.mode == AnalysisMode.FULL
    
    def test_full_config(self):
        config = StrategyConfig.full()
        assert config.enable_response_simulator == True
        assert config.enable_moat_assessment == True
    
    def test_quick_config(self):
        config = StrategyConfig.quick()
        assert config.mode == AnalysisMode.QUICK
        assert config.time_horizon_years == 1
    
    def test_terrain_only(self):
        config = StrategyConfig.terrain_only()
        assert config.mode == AnalysisMode.TERRAIN
        assert config.enable_response_simulator == False
    
    def test_moat_only(self):
        config = StrategyConfig.moat_only()
        assert config.mode == AnalysisMode.MOAT
        assert config.enable_moat_assessment == True


class TestSunTzuFramework:
    """Test Framework 1: Sun Tzu."""
    
    def test_analyze_terrain(self):
        result = SunTzuFramework.analyze_terrain(
            industry="SaaS",
            competitors=["Competitor A", "Competitor B"]
        )
        assert isinstance(result, TerrainAnalysis)
        assert len(result.direct_competitors) == 2
    
    def test_high_concentration(self):
        result = SunTzuFramework.analyze_terrain(
            industry="Enterprise",
            competitors=["Big A", "Big B"]
        )
        assert result.concentration.value == "high"
    
    def test_prompt_section(self):
        prompt = SunTzuFramework.get_prompt_section()
        assert "TERRAIN ANALYSIS" in prompt
        assert "Sun Tzu" in prompt


class TestMeadowsFramework:
    """Test Framework 2: Meadows."""
    
    def test_identify_leverage(self):
        result = MeadowsFramework.identify_leverage_points(
            system_description="Growing SaaS platform with network effects"
        )
        assert len(result.highest_leverage_points) > 0
        assert len(result.reinforcing_loops) > 0
    
    def test_leverage_points_structure(self):
        result = MeadowsFramework.identify_leverage_points("Test system")
        for lp in result.highest_leverage_points:
            assert 1 <= lp.level <= 12
    
    def test_prompt_section(self):
        prompt = MeadowsFramework.get_prompt_section()
        assert "LEVERAGE POINTS" in prompt
        assert "Meadows" in prompt


class TestBarabasiFramework:
    """Test Framework 3: Barabási."""
    
    def test_analyze_network(self):
        result = BarabasiFramework.analyze_network(
            market_description="Platform marketplace",
            current_adoption=10.0
        )
        assert isinstance(result, NetworkDynamics)
        assert result.tipping_point is not None
    
    def test_preferential_attachment(self):
        result = BarabasiFramework.analyze_network(
            market_description="Network platform with strong effects"
        )
        assert result.preferential_attachment == True
    
    def test_prompt_section(self):
        prompt = BarabasiFramework.get_prompt_section()
        assert "NETWORK DYNAMICS" in prompt
        assert "Barabási" in prompt


class TestPearlFramework:
    """Test Framework 4: Pearl."""
    
    def test_build_causal_model(self):
        result = PearlFramework.build_causal_model(
            strategy_description="Increase market share through differentiation",
            key_variables=["differentiation", "market_share", "revenue"]
        )
        assert isinstance(result, CausalModel)
        assert len(result.variables) == 3
    
    def test_causal_assumptions(self):
        result = PearlFramework.build_causal_model(
            strategy_description="Test",
            assumptions=["Market will grow", "Customers will adopt"]
        )
        assert len(result.assumptions) == 2
    
    def test_prompt_section(self):
        prompt = PearlFramework.get_prompt_section()
        assert "CAUSAL MODEL" in prompt
        assert "Pearl" in prompt


class TestOstromFramework:
    """Test Framework 5: Ostrom."""
    
    def test_assess_governance(self):
        result = OstromFramework.assess_governance(
            organization_description="B2B SaaS company",
            current_advantages=["Strong brand", "Network effects"]
        )
        assert isinstance(result, ResourceGovernance)
        assert len(result.principles) == 8
    
    def test_sustainability_score(self):
        result = OstromFramework.assess_governance("Test org")
        assert 1 <= result.sustainability_score <= 10
    
    def test_prompt_section(self):
        prompt = OstromFramework.get_prompt_section()
        assert "RESOURCE GOVERNANCE" in prompt
        assert "Ostrom" in prompt


class TestStrategyEngine:
    """Test main Strategy Engine."""
    
    def test_create_engine(self):
        engine = StrategyEngine()
        assert engine.config.mode == AnalysisMode.FULL
    
    def test_generate_prompt(self):
        engine = StrategyEngine()
        prompt = engine.generate_system_prompt()
        assert "STRATEGY_ENGINE" in prompt
        assert "Sun Tzu" in prompt
    
    def test_generate_compact_prompt(self):
        engine = StrategyEngine()
        prompt = engine.generate_system_prompt(compact=True)
        assert len(prompt) < 3000
    
    def test_generate_quick_prompt(self):
        engine = StrategyEngine(config=StrategyConfig.quick())
        prompt = engine.generate_system_prompt()
        assert "QUICK_STRATEGY" in prompt
    
    def test_calculate_moat(self):
        engine = StrategyEngine()
        moat = engine.calculate_moat(imitation=8, switching=7, network=6)
        assert moat.imitation_difficulty == 8
        assert moat.score > 0
    
    def test_simulate_response(self):
        engine = StrategyEngine()
        competitors = [
            CompetitorProfile(name="A", posture="aggressive"),
            CompetitorProfile(name="B", posture="defensive")
        ]
        response = engine.simulate_response("Launch new product", competitors)
        assert response.your_move == "Launch new product"
        assert len(response.competitor_profiles) == 2
    
    def test_check_ethics_green(self):
        engine = StrategyEngine()
        ethics = engine.check_ethics(["grow market", "improve quality"])
        assert ethics.flag == EthicsFlag.GREEN
    
    def test_analyze(self):
        engine = StrategyEngine()
        analysis = engine.analyze(
            organization="Acme Corp",
            industry="SaaS",
            strategic_question="How do we compete against incumbents?"
        )
        assert analysis.organization == "Acme Corp"
        assert analysis.synthesis is not None
        assert analysis.moat_durability is not None
    
    def test_analyze_with_competitors(self):
        engine = StrategyEngine()
        analysis = engine.analyze(
            organization="StartupX",
            industry="FinTech",
            strategic_question="How do we differentiate?",
            competitors=["BigBank", "FinTechY", "TradFin"]
        )
        assert len(analysis.terrain_analysis["actors"]["direct_competitors"]) == 3
    
    def test_analyze_with_moat_scores(self):
        engine = StrategyEngine()
        analysis = engine.analyze(
            organization="Test",
            industry="Tech",
            strategic_question="Test question",
            moat_scores={
                "imitation": 8,
                "switching": 7,
                "network": 9,
                "scale": 6,
                "brand": 5,
                "regulatory": 3
            }
        )
        assert analysis.moat_durability.imitation_difficulty == 8
    
    def test_analysis_summary(self):
        engine = StrategyEngine()
        analysis = engine.analyze(
            organization="TestCo",
            industry="Tech",
            strategic_question="Test"
        )
        summary = analysis.summary()
        assert "STRATEGY ENGINE" in summary
        assert "TestCo" in summary
    
    def test_analysis_history(self):
        engine = StrategyEngine()
        engine.analyze("Org1", "Industry1", "Q1")
        engine.analyze("Org2", "Industry2", "Q2")
        history = engine.get_analysis_history()
        assert len(history) == 2
    
    def test_repr(self):
        engine = StrategyEngine()
        assert "full" in repr(engine).lower()


class TestIntegration:
    """Integration tests."""
    
    def test_full_analysis_pipeline(self):
        engine = StrategyEngine(config=StrategyConfig.full())
        
        analysis = engine.analyze(
            organization="Acme SaaS",
            industry="B2B Project Management",
            strategic_question="How do we compete against Asana, Monday.com, and Notion?",
            competitors=["Asana", "Monday.com", "Notion", "ClickUp"],
            current_advantages=["Construction vertical expertise", "Custom workflows"],
            planned_move="Launch freemium tier",
            moat_scores={
                "imitation": 4,
                "switching": 5,
                "network": 3,
                "scale": 4,
                "brand": 2,
                "regulatory": 1
            }
        )
        
        assert analysis.terrain_analysis is not None
        assert analysis.leverage_analysis is not None
        assert analysis.network_analysis is not None
        assert analysis.causal_model is not None
        assert analysis.governance_analysis is not None
        
        assert analysis.moat_durability is not None
        assert analysis.moat_durability.strength in (MoatStrength.WEAK, MoatStrength.MODERATE)
        
        assert analysis.competitive_response is not None
        assert analysis.competitive_response.your_move == "Launch freemium tier"
        
        assert analysis.synthesis is not None
        assert analysis.synthesis.ethics_flag == EthicsFlag.GREEN
        
        assert len(analysis.recommendations) > 0
    
    def test_quick_mode(self):
        engine = StrategyEngine(config=StrategyConfig.quick())
        
        analysis = engine.analyze(
            organization="Quick Test",
            industry="Tech",
            strategic_question="What should we do next?"
        )
        
        assert analysis.synthesis is not None
        assert analysis.moat_durability is not None
