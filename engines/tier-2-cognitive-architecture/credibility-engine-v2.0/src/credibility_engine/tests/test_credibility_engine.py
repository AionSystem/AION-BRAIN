"""
CREDIBILITY ENGINE v2.0 - Test Suite
======================================

Comprehensive tests for the Credibility Engine.
"""

import pytest
from datetime import datetime, timedelta
from credibility_engine import (
    CredibilityEngine, CredibilityConfig,
    CredibilityScore, AssetType, DecayModel,
    EvidenceAsset, DecayAlert, AlertPriority,
    CredibilityHealth, FraudSignal
)
from credibility_engine.modules.decay_math import DecayMathematics
from credibility_engine.modules.signals import SignalInstrumentation
from credibility_engine.modules.explainability import ExplainabilityEngine
from credibility_engine.modules.automation import ActionAutomation
from credibility_engine.modules.fraud import FraudDetection
from credibility_engine.modules.provenance import ProvenanceSystem


def create_test_asset(
    asset_id: str = "test-001",
    asset_type: AssetType = AssetType.LIVE_DEMO,
    days_ago: int = 30
) -> EvidenceAsset:
    """Helper to create test assets."""
    return EvidenceAsset(
        asset_id=asset_id,
        asset_type=asset_type,
        name=f"Test {asset_type.value}",
        created_date=datetime.now() - timedelta(days=days_ago + 10),
        last_refresh=datetime.now() - timedelta(days=days_ago)
    )


class TestDecayMathematics:
    """Test decay calculations."""
    
    def test_exponential_decay_no_time(self):
        score = DecayMathematics.exponential_decay(100.0, 0, 90)
        assert score == 100.0
    
    def test_exponential_decay_half_life(self):
        score = DecayMathematics.exponential_decay(100.0, 90, 90)
        assert 49.0 < score < 51.0
    
    def test_exponential_decay_two_half_lives(self):
        score = DecayMathematics.exponential_decay(100.0, 180, 90)
        assert 24.0 < score < 26.0
    
    def test_weibull_decay(self):
        score = DecayMathematics.weibull_decay(100.0, 50, scale=100, shape=1.5)
        assert 0 < score < 100
    
    def test_confidence_interval(self):
        lower, upper = DecayMathematics.calculate_confidence_interval(75.0)
        assert lower < 75.0
        assert upper > 75.0
    
    def test_project_future_score(self):
        future = DecayMathematics.project_future_score(100.0, 30, 90)
        assert future < 100.0
    
    def test_determine_health_healthy(self):
        health = DecayMathematics.determine_health(85.0)
        assert health == CredibilityHealth.HEALTHY
    
    def test_determine_health_attention(self):
        health = DecayMathematics.determine_health(65.0)
        assert health == CredibilityHealth.ATTENTION
    
    def test_determine_health_warning(self):
        health = DecayMathematics.determine_health(45.0)
        assert health == CredibilityHealth.WARNING
    
    def test_determine_health_critical(self):
        health = DecayMathematics.determine_health(25.0)
        assert health == CredibilityHealth.CRITICAL
    
    def test_determine_health_expired(self):
        health = DecayMathematics.determine_health(10.0)
        assert health == CredibilityHealth.EXPIRED
    
    def test_calculate_score_full(self):
        asset = create_test_asset(days_ago=45)
        score = DecayMathematics.calculate_score(asset)
        assert isinstance(score, CredibilityScore)
        assert 0 <= score.current_score <= 100


class TestSignalInstrumentation:
    """Test signal processing."""
    
    def test_normalize_signal(self):
        normalized = SignalInstrumentation.normalize_signal(75.0, baseline=50.0)
        assert normalized > 50
    
    def test_proof_freshness(self):
        freshness = SignalInstrumentation.calculate_proof_freshness(
            days_since_demo=30,
            days_since_case_study=60,
            days_since_testimonial=45
        )
        assert 0 <= freshness <= 100
    
    def test_social_momentum(self):
        momentum = SignalInstrumentation.calculate_social_momentum(
            mention_velocity=15.0,
            sentiment_trend=0.7,
            amplification_rate=2.5
        )
        assert 0 <= momentum <= 100
    
    def test_relevance_index(self):
        relevance = SignalInstrumentation.calculate_relevance_index(
            search_volume_trend=0.2,
            market_alignment=0.8,
            competitor_comparison=0.6
        )
        assert 0 <= relevance <= 100
    
    def test_endorsement_quality(self):
        quality = SignalInstrumentation.calculate_endorsement_quality(
            endorser_authority=0.9,
            endorsement_recency_days=15,
            endorsement_specificity=0.85
        )
        assert 0 <= quality <= 100
    
    def test_fraud_penalty_no_signals(self):
        penalty = SignalInstrumentation.calculate_fraud_penalty(0, 0, 0)
        assert penalty == 100.0
    
    def test_fraud_penalty_some_signals(self):
        penalty = SignalInstrumentation.calculate_fraud_penalty(1, 1, 0)
        assert penalty < 100.0
    
    def test_composite_calculation(self):
        composite = SignalInstrumentation.calculate_composite(80, 70, 60, 50, 90)
        assert 0 <= composite.composite <= 100
    
    def test_quick_composite(self):
        composite = SignalInstrumentation.quick_composite()
        assert composite.composite > 0


class TestExplainability:
    """Test score explanations."""
    
    def test_explain_healthy_score(self):
        score = CredibilityScore(
            asset_id="test",
            current_score=85.0,
            initial_score=100.0,
            decay_percentage=15.0,
            health=CredibilityHealth.HEALTHY,
            days_since_refresh=30.0,
            half_life_days=90,
            projected_30_day_score=75.0,
            confidence_interval=(80.0, 90.0)
        )
        explanation = ExplainabilityEngine.explain_score(score)
        assert "healthy" in explanation.headline.lower()
    
    def test_explain_critical_score(self):
        score = CredibilityScore(
            asset_id="test",
            current_score=25.0,
            initial_score=100.0,
            decay_percentage=75.0,
            health=CredibilityHealth.CRITICAL,
            days_since_refresh=180.0,
            half_life_days=90,
            projected_30_day_score=15.0,
            confidence_interval=(20.0, 30.0)
        )
        explanation = ExplainabilityEngine.explain_score(score)
        assert "immediate" in explanation.headline.lower() or "action" in explanation.headline.lower()
    
    def test_attribution_breakdown(self):
        composite = SignalInstrumentation.quick_composite()
        attributions = ExplainabilityEngine.attribution_breakdown(composite)
        assert len(attributions) == 5


class TestActionAutomation:
    """Test alert generation and playbooks."""
    
    def test_generate_alert_healthy(self):
        score = CredibilityScore(
            asset_id="test",
            current_score=85.0,
            initial_score=100.0,
            decay_percentage=15.0,
            health=CredibilityHealth.HEALTHY,
            days_since_refresh=30.0,
            half_life_days=90,
            projected_30_day_score=75.0,
            confidence_interval=(80.0, 90.0)
        )
        alert = ActionAutomation.generate_alert(score)
        assert alert is None
    
    def test_generate_alert_warning(self):
        score = CredibilityScore(
            asset_id="test",
            current_score=45.0,
            initial_score=100.0,
            decay_percentage=55.0,
            health=CredibilityHealth.WARNING,
            days_since_refresh=90.0,
            half_life_days=90,
            projected_30_day_score=30.0,
            confidence_interval=(40.0, 50.0)
        )
        alert = ActionAutomation.generate_alert(score)
        assert alert is not None
        assert alert.priority == AlertPriority.IMMEDIATE_ACTION
    
    def test_select_playbook_critical(self):
        score = CredibilityScore(
            asset_id="test",
            current_score=25.0,
            initial_score=100.0,
            decay_percentage=75.0,
            health=CredibilityHealth.CRITICAL,
            days_since_refresh=150.0,
            half_life_days=90,
            projected_30_day_score=15.0,
            confidence_interval=(20.0, 30.0)
        )
        playbook = ActionAutomation.select_playbook(score)
        assert playbook is not None
        assert "critical" in playbook.name.lower() or "emergency" in playbook.name.lower()
    
    def test_get_all_playbooks(self):
        playbooks = ActionAutomation.get_all_playbooks()
        assert len(playbooks) >= 3


class TestFraudDetection:
    """Test fraud detection."""
    
    def test_authentic_testimonial(self):
        check = FraudDetection.check_testimonial_authenticity(
            account_age_days=365,
            posting_history_count=50,
            has_verification=True,
            content_uniqueness=0.9
        )
        assert check.is_authentic == True
        assert check.confidence > 0.7
    
    def test_suspicious_testimonial(self):
        check = FraudDetection.check_testimonial_authenticity(
            account_age_days=5,
            posting_history_count=2,
            has_verification=False,
            content_uniqueness=0.3
        )
        assert check.is_authentic == False
        assert len(check.flags) >= 2
    
    def test_velocity_anomaly_normal(self):
        anomaly = FraudDetection.detect_velocity_anomaly(
            metric_name="mentions",
            observed_value=12.0,
            historical_mean=10.0,
            historical_std=3.0
        )
        assert anomaly.is_suspicious == False
    
    def test_velocity_anomaly_suspicious(self):
        anomaly = FraudDetection.detect_velocity_anomaly(
            metric_name="mentions",
            observed_value=50.0,
            historical_mean=10.0,
            historical_std=5.0
        )
        assert anomaly.is_suspicious == True
    
    def test_source_trust_calculation(self):
        trust = FraudDetection.calculate_source_trust(0.8, 0.9, True)
        assert 0 <= trust <= 1.0
    
    def test_compliance_check(self):
        compliance = FraudDetection.check_compliance(
            has_disclosure=True,
            data_handling="encrypted",
            platform="twitter"
        )
        assert compliance.ftc_compliant == True


class TestProvenance:
    """Test provenance system."""
    
    def test_add_record(self):
        system = ProvenanceSystem()
        record = system.add_record(
            asset_id="asset-001",
            source_url="https://example.com/testimonial",
            content="Great product!",
            verifier="admin",
            verification_method="manual"
        )
        assert record.record_id is not None
        assert record.content_hash is not None
    
    def test_verify_record(self):
        system = ProvenanceSystem()
        record = system.add_record(
            asset_id="asset-001",
            source_url="https://example.com",
            content="Test content",
            verifier="admin",
            verification_method="manual"
        )
        result = system.verify_record(record, "Test content")
        assert result.is_valid == True
        assert result.hash_matches == True
    
    def test_verify_tampered_content(self):
        system = ProvenanceSystem()
        record = system.add_record(
            asset_id="asset-001",
            source_url="https://example.com",
            content="Original content",
            verifier="admin",
            verification_method="manual"
        )
        result = system.verify_record(record, "Tampered content")
        assert result.is_valid == False
        assert result.hash_matches == False
    
    def test_chain_integrity(self):
        system = ProvenanceSystem()
        system.add_record("a1", "url1", "content1", "v1", "m1")
        system.add_record("a2", "url2", "content2", "v2", "m2")
        system.add_record("a3", "url3", "content3", "v3", "m3")
        
        assert system.verify_chain_integrity() == True
        assert system.get_chain_length() == 3


class TestCredibilityConfig:
    """Test configuration."""
    
    def test_default_config(self):
        config = CredibilityConfig()
        assert config.enable_fraud_detection == True
    
    def test_quick_config(self):
        config = CredibilityConfig.quick()
        assert config.enable_fraud_detection == False
    
    def test_enterprise_config(self):
        config = CredibilityConfig.enterprise()
        assert config.enable_provenance == True


class TestCredibilityEngine:
    """Test main Credibility Engine."""
    
    def test_create_engine(self):
        engine = CredibilityEngine()
        assert engine.VERSION == "2.0.0"
    
    def test_add_asset(self):
        engine = CredibilityEngine()
        asset = create_test_asset()
        engine.add_asset(asset)
        assert engine.get_asset("test-001") is not None
    
    def test_remove_asset(self):
        engine = CredibilityEngine()
        asset = create_test_asset()
        engine.add_asset(asset)
        result = engine.remove_asset("test-001")
        assert result == True
        assert engine.get_asset("test-001") is None
    
    def test_calculate_score(self):
        engine = CredibilityEngine()
        asset = create_test_asset(days_ago=45)
        score = engine.calculate_score(asset)
        assert isinstance(score, CredibilityScore)
    
    def test_generate_prompt(self):
        engine = CredibilityEngine()
        prompt = engine.generate_system_prompt()
        assert "CREDIBILITY" in prompt
    
    def test_compact_prompt(self):
        engine = CredibilityEngine()
        prompt = engine.generate_system_prompt(compact=True)
        assert len(prompt) < 2000
    
    def test_full_analysis(self):
        engine = CredibilityEngine()
        
        engine.add_asset(create_test_asset("demo-1", AssetType.LIVE_DEMO, 30))
        engine.add_asset(create_test_asset("case-1", AssetType.CASE_STUDY, 60))
        engine.add_asset(create_test_asset("test-1", AssetType.TESTIMONIAL, 150))
        
        analysis = engine.analyze()
        
        assert analysis.report.total_assets == 3
        assert len(analysis.assets) == 3
    
    def test_analysis_summary(self):
        engine = CredibilityEngine()
        engine.add_asset(create_test_asset())
        analysis = engine.analyze()
        summary = analysis.summary()
        assert "CREDIBILITY ENGINE" in summary
    
    def test_generate_alerts(self):
        engine = CredibilityEngine()
        engine.add_asset(create_test_asset("old-asset", AssetType.LIVE_DEMO, 180))
        engine.calculate_all_scores()
        alerts = engine.generate_alerts()
        assert len(alerts) > 0
    
    def test_repr(self):
        engine = CredibilityEngine()
        engine.add_asset(create_test_asset())
        assert "assets=1" in repr(engine)


class TestIntegration:
    """Integration tests."""
    
    def test_full_workflow(self):
        engine = CredibilityEngine(config=CredibilityConfig.enterprise())
        
        engine.add_asset(EvidenceAsset(
            asset_id="demo-2024",
            asset_type=AssetType.LIVE_DEMO,
            name="Q4 2024 Product Demo",
            created_date=datetime.now() - timedelta(days=100),
            last_refresh=datetime.now() - timedelta(days=45)
        ))
        
        engine.add_asset(EvidenceAsset(
            asset_id="case-acme",
            asset_type=AssetType.CASE_STUDY,
            name="ACME Corp Success Story",
            created_date=datetime.now() - timedelta(days=200),
            last_refresh=datetime.now() - timedelta(days=120)
        ))
        
        analysis = engine.analyze()
        
        assert analysis.report.total_assets == 2
        assert analysis.report.overall_health in list(CredibilityHealth)
        assert len(analysis.report.recommendations) > 0
    
    def test_fraud_detection_integration(self):
        engine = CredibilityEngine()
        
        check = engine.check_fraud(
            account_age_days=7,
            posting_history=3,
            verified=False
        )
        
        assert check.is_authentic == False or len(check.flags) > 0
