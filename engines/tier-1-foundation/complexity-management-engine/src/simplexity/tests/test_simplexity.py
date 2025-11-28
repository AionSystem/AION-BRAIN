"""
SIMPLEXITY v2.0 - Test Suite
=============================

Comprehensive tests for the Complexity Management Engine.
"""

import pytest
from simplexity import (
    Simplexity, SimplexityConfig, OperationalMode, OutputLevel,
    ComplexityScore, ComplexityTrajectory, TransferScore, FragilityScore,
    ReversibilityLevel, AbstractionLevel, EmergenceType, DecompositionStrategy,
    SimplificationLevel, CognitiveProfile
)
from simplexity.config import (
    AudienceProfile, ExpertiseLevel, CognitiveState, 
    TimeAvailable, DecisionStakes
)
from simplexity.modules.abstraction import AbstractionModule
from simplexity.modules.emergence import EmergenceModule
from simplexity.modules.decomposition import DecompositionModule
from simplexity.modules.simplification import SimplificationModule
from simplexity.modules.dynamics import DynamicsModule
from simplexity.modules.calibration import CalibrationModule
from simplexity.modules.transfer import TransferModule, TransferDestination
from simplexity.modules.mvc import MVCModule


class TestComplexityScore:
    """Test complexity scoring system."""
    
    def test_create_score(self):
        score = ComplexityScore(scale=5, coupling=6, dynamics=4, uncertainty=5, emergence=3)
        assert score.scale == 5
        assert score.coupling == 6
        
    def test_composite_calculation(self):
        score = ComplexityScore(scale=3, coupling=4, dynamics=3, uncertainty=3, emergence=3)
        assert 7 < score.composite < 8
        
    def test_level_low(self):
        score = ComplexityScore(scale=2, coupling=2, dynamics=2, uncertainty=2, emergence=2)
        assert score.level == "LOW"
        
    def test_level_moderate(self):
        score = ComplexityScore(scale=4, coupling=4, dynamics=4, uncertainty=4, emergence=4)
        assert score.level == "MODERATE"
        
    def test_level_high(self):
        score = ComplexityScore(scale=6, coupling=6, dynamics=6, uncertainty=6, emergence=6)
        assert score.level == "HIGH"
        
    def test_level_extreme(self):
        score = ComplexityScore(scale=8, coupling=8, dynamics=8, uncertainty=8, emergence=8)
        assert score.level == "EXTREME"
        
    def test_exceeds_ceiling(self):
        score = ComplexityScore(scale=8, coupling=8, dynamics=8, uncertainty=8, emergence=8)
        assert score.exceeds_ceiling(15.0) == True
        
    def test_trajectory(self):
        score = ComplexityScore(trajectory=ComplexityTrajectory.EXPLOSIVE)
        assert score.trajectory == ComplexityTrajectory.EXPLOSIVE
        
    def test_invalid_dimension(self):
        with pytest.raises(ValueError):
            ComplexityScore(scale=11)


class TestTransferScore:
    """Test transfer scoring."""
    
    def test_create_transfer_score(self):
        score = TransferScore(score=5.0, source_area="UI")
        assert score.score == 5.0
        
    def test_acceptable_transfer(self):
        score = TransferScore(score=3.0)
        assert score.is_acceptable == True
        
    def test_unacceptable_transfer(self):
        score = TransferScore(score=8.0)
        assert score.is_acceptable == False
        
    def test_invalid_score(self):
        with pytest.raises(ValueError):
            TransferScore(score=15.0)


class TestFragilityScore:
    """Test fragility scoring."""
    
    def test_safe_to_remove(self):
        score = FragilityScore(score=2.0)
        assert score.is_safe_to_remove == True
        
    def test_not_safe_to_remove(self):
        score = FragilityScore(score=7.0)
        assert score.is_safe_to_remove == False
        
    def test_calculate_from_impacts(self):
        score = FragilityScore.calculate(
            redundancy=4.0,
            optionality=6.0,
            stress_response=5.0,
            learning=5.0
        )
        assert score.score == 5.0


class TestSimplexityConfig:
    """Test configuration options."""
    
    def test_default_config(self):
        config = SimplexityConfig()
        assert config.mode == OperationalMode.STANDARD
        
    def test_quick_config(self):
        config = SimplexityConfig.quick()
        assert config.mode == OperationalMode.QUICK
        assert config.enable_dynamics == False
        
    def test_deep_config(self):
        config = SimplexityConfig.deep()
        assert config.mode == OperationalMode.DEEP
        assert config.complexity_ceiling == 20.0
        
    def test_crisis_config(self):
        config = SimplexityConfig.crisis()
        assert config.mode == OperationalMode.QUICK
        assert config.enable_mvc == True


class TestAudienceProfile:
    """Test audience profiling."""
    
    def test_default_profile(self):
        profile = AudienceProfile()
        assert profile.expertise == ExpertiseLevel.INTERMEDIATE
        
    def test_crisis_output_level(self):
        profile = AudienceProfile(state=CognitiveState.CRISIS)
        assert profile.recommended_output_level() == OutputLevel.SINGLE_INSIGHT
        
    def test_expert_high_stakes(self):
        profile = AudienceProfile(
            expertise=ExpertiseLevel.MASTER,
            stakes=DecisionStakes.CRITICAL
        )
        assert profile.recommended_output_level() == OutputLevel.COMPLETE_COMPLEXITY
        
    def test_complexity_reduction(self):
        stressed = AudienceProfile(state=CognitiveState.STRESSED)
        assert stressed.complexity_reduction_factor() == 0.6


class TestAbstractionModule:
    """Test Module 1: Abstraction Layering."""
    
    def test_recommend_for_immediate_action(self):
        level = AbstractionModule.recommend_level("immediate_action")
        assert level == AbstractionLevel.COMPONENT
        
    def test_recommend_for_strategic_planning(self):
        level = AbstractionModule.recommend_level("strategic_planning")
        assert level == AbstractionLevel.STRUCTURE
        
    def test_analyze_zoom_in(self):
        result = AbstractionModule.analyze(
            current_level=AbstractionLevel.SYSTEM,
            goal_type="immediate_action"
        )
        assert "ZOOM IN" in result.zoom_direction
        
    def test_prompt_section(self):
        prompt = AbstractionModule.get_prompt_section()
        assert "Level 5: Paradigm" in prompt


class TestEmergenceModule:
    """Test Module 2: Emergence Detection."""
    
    def test_detect_adaptive(self):
        result = EmergenceModule.detect("The market adapts to new information")
        assert EmergenceType.ADAPTIVE in result.detected_types
        
    def test_detect_feedback(self):
        result = EmergenceModule.detect("Feedback loops amplify the signal")
        assert EmergenceType.WEAK in result.detected_types
        
    def test_no_emergence(self):
        result = EmergenceModule.detect("A simple linear process")
        assert len(result.detected_types) == 0


class TestDecompositionModule:
    """Test Module 3: Problem Decomposition."""
    
    def test_recommend_functional(self):
        strategy = DecompositionModule.recommend_strategy("Improve the workflow")
        assert strategy == DecompositionStrategy.FUNCTIONAL
        
    def test_recommend_temporal(self):
        strategy = DecompositionModule.recommend_strategy("Plan the project timeline")
        assert strategy == DecompositionStrategy.TEMPORAL
        
    def test_reversibility_high(self):
        level = DecompositionModule.assess_reversibility(1.0, 1.0, 1.0, 1.0)
        assert level == ReversibilityLevel.HIGH
        
    def test_reversibility_irreversible(self):
        level = DecompositionModule.assess_reversibility(9.0, 9.0, 9.0, 9.0)
        assert level == ReversibilityLevel.IRREVERSIBLE


class TestSimplificationModule:
    """Test Module 4: Simplification Protocols."""
    
    def test_recommend_low_complexity(self):
        level = SimplificationModule.recommend_level(4.0)
        assert level == SimplificationLevel.PARAMETER_REDUCTION
        
    def test_recommend_high_complexity(self):
        level = SimplificationModule.recommend_level(14.0, tolerance="high")
        assert level == SimplificationLevel.DYNAMICS_LINEARIZATION
        
    def test_anti_fragility_check(self):
        score = SimplificationModule.anti_fragility_check(
            element="backup system",
            redundancy=8.0,
            optionality=6.0,
            stress_response=7.0,
            learning=5.0
        )
        assert not score.is_safe_to_remove


class TestDynamicsModule:
    """Test Module 5: Complexity Dynamics."""
    
    def test_growing_trajectory(self):
        trajectory = DynamicsModule.assess_trajectory([5.0, 6.0, 7.0], 9.0)
        assert trajectory == ComplexityTrajectory.GROWING
        
    def test_stable_trajectory(self):
        trajectory = DynamicsModule.assess_trajectory([5.0, 5.0, 5.0], 5.0)
        assert trajectory == ComplexityTrajectory.STABLE
        
    def test_explosive_trajectory(self):
        trajectory = DynamicsModule.assess_trajectory([5.0, 5.0, 5.0], 10.0)
        assert trajectory == ComplexityTrajectory.EXPLOSIVE


class TestCalibrationModule:
    """Test Module 6: Cognitive Load Calibration."""
    
    def test_crisis_calibration(self):
        profile = CognitiveProfile(
            expertise=ExpertiseLevel.EXPERT,
            state=CognitiveState.CRISIS,
            time=TimeAvailable.IMMEDIATE,
            stakes=DecisionStakes.HIGH
        )
        result = CalibrationModule.calibrate(profile)
        assert result.output_level == OutputLevel.SINGLE_INSIGHT
        
    def test_complexity_factor_stressed(self):
        profile = CognitiveProfile(
            expertise=ExpertiseLevel.INTERMEDIATE,
            state=CognitiveState.STRESSED,
            time=TimeAvailable.LIMITED,
            stakes=DecisionStakes.MEDIUM
        )
        factor = CalibrationModule.calculate_complexity_factor(profile)
        assert factor < 1.0


class TestTransferModule:
    """Test Module 7: Complexity Transfer Detection."""
    
    def test_detect_transfer(self):
        destinations = [
            TransferDestination(
                area="operations",
                description="Moved to ops team",
                new_complexity_estimate=5.0
            )
        ]
        result = TransferModule.detect_transfer(
            source_area="development",
            original_complexity=10.0,
            simplified_complexity=5.0,
            destinations=destinations
        )
        assert result.transfer_score.score == 10.0
        
    def test_true_simplification(self):
        result = TransferModule.detect_transfer(
            source_area="code",
            original_complexity=10.0,
            simplified_complexity=3.0,
            destinations=[]
        )
        assert result.is_true_simplification == True


class TestMVCModule:
    """Test Module 8: Minimum Viable Complexity."""
    
    def test_analyze_mvc(self):
        elements = [
            {"name": "core_feature", "purpose": "Main function", "essential": True},
            {"name": "nice_to_have", "purpose": "Extra", "essential": False, "keep": False}
        ]
        result = MVCModule.analyze(
            goal="Build MVP",
            success_criteria=["Must work", "Must be fast"],
            all_elements=elements,
            original_complexity=10.0
        )
        assert result.elements_kept == 1
        assert result.elements_removed == 1


class TestSimplexity:
    """Test main Simplexity engine."""
    
    def test_create_engine(self):
        engine = Simplexity()
        assert engine.config.mode == OperationalMode.STANDARD
        
    def test_generate_prompt(self):
        engine = Simplexity()
        prompt = engine.generate_system_prompt()
        assert "SIMPLEXITY" in prompt
        assert "MODULE 1" in prompt
        
    def test_generate_compact_prompt(self):
        engine = Simplexity()
        prompt = engine.generate_system_prompt(compact=True)
        assert len(prompt) < 2000
        
    def test_generate_quick_prompt(self):
        engine = Simplexity(config=SimplexityConfig.quick())
        prompt = engine.generate_system_prompt()
        assert "QUICK MODE" in prompt
        
    def test_score_complexity(self):
        engine = Simplexity()
        score = engine.score_complexity(scale=7, coupling=6)
        assert score.scale == 7
        assert score.coupling == 6
        
    def test_check_safety_alerts(self):
        engine = Simplexity()
        score = ComplexityScore(scale=8, coupling=8, dynamics=8, uncertainty=8, emergence=8)
        alerts = engine.check_safety_thresholds(score)
        assert len(alerts) > 0
        
    def test_explosive_trajectory_alert(self):
        engine = Simplexity()
        score = ComplexityScore(trajectory=ComplexityTrajectory.EXPLOSIVE)
        alerts = engine.check_safety_thresholds(score)
        assert any("EXPLOSIVE" in a for a in alerts)
        
    def test_analyze(self):
        engine = Simplexity()
        analysis = engine.analyze(
            problem="Complex software system",
            goal="Simplify architecture"
        )
        assert analysis.complexity_score is not None
        assert len(analysis.recommendations) > 0
        
    def test_analyze_with_audience(self):
        engine = Simplexity()
        audience = AudienceProfile(
            expertise=ExpertiseLevel.NOVICE,
            state=CognitiveState.STRESSED
        )
        analysis = engine.analyze(
            problem="Complex issue",
            goal="Understand it",
            audience=audience
        )
        assert analysis.calibration is not None
        
    def test_analysis_history(self):
        engine = Simplexity()
        engine.analyze("Problem 1")
        engine.analyze("Problem 2")
        history = engine.get_analysis_history()
        assert len(history) == 2
        
    def test_repr(self):
        engine = Simplexity()
        assert "standard" in repr(engine).lower()


class TestIntegration:
    """Integration tests."""
    
    def test_full_analysis_pipeline(self):
        engine = Simplexity(config=SimplexityConfig.standard())
        
        audience = AudienceProfile(
            expertise=ExpertiseLevel.EXPERT,
            state=CognitiveState.FOCUSED,
            time_available=TimeAvailable.LIMITED,
            stakes=DecisionStakes.HIGH
        )
        
        analysis = engine.analyze(
            problem="Our software system has grown to 150+ microservices with increasing outages",
            goal="Create manageable improvement roadmap",
            audience=audience,
            complexity_inputs={
                "scale": 8,
                "coupling": 7,
                "dynamics": 6,
                "uncertainty": 5,
                "emergence": 4
            }
        )
        
        assert analysis.complexity_score.level in ("HIGH", "EXTREME")
        assert analysis.calibration is not None
        assert analysis.dynamics_result is not None
        assert len(analysis.recommendations) > 0
        
    def test_crisis_mode_analysis(self):
        engine = Simplexity(config=SimplexityConfig.crisis())
        
        audience = AudienceProfile(state=CognitiveState.CRISIS)
        
        analysis = engine.analyze(
            problem="System is down!",
            goal="Get it working now",
            audience=audience
        )
        
        assert analysis.calibration.output_level == OutputLevel.SINGLE_INSIGHT
