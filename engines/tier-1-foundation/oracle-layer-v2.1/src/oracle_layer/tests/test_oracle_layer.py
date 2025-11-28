"""
Oracle Layer v2.1 Test Suite
============================

Tests for verifying Oracle Layer functionality.
Run with: pytest test_oracle_layer.py -v
"""

import pytest
from oracle_layer import (
    OracleLayer, OracleConfig, VerificationLevel,
    ConfidenceScore, ReasoningTrace, TrinityVerification,
    VerificationResult, VerificationStatus,
    GenericProvider, AIResponse
)


class TestConfidenceScore:
    """Tests for ConfidenceScore class."""
    
    def test_basic_confidence(self):
        score = ConfidenceScore(0.85)
        assert score.value == 0.85
        assert score.total_uncertainty == 0.0
        assert str(score) == "0.85"
    
    def test_confidence_with_uncertainty(self):
        score = ConfidenceScore(0.80, epistemic_uncertainty=0.10, aleatoric_uncertainty=0.05)
        assert score.value == 0.80
        assert 0.11 < score.total_uncertainty < 0.12
        assert "±" in str(score)
    
    def test_confidence_bounds(self):
        score = ConfidenceScore(0.75, epistemic_uncertainty=0.10)
        assert score.lower_bound == 0.65
        assert score.upper_bound == 0.85
    
    def test_meets_threshold(self):
        score = ConfidenceScore(0.80, epistemic_uncertainty=0.05)
        assert score.meets_threshold(0.80, conservative=False)
        assert score.meets_threshold(0.75, conservative=True)
        assert not score.meets_threshold(0.80, conservative=True)
    
    def test_invalid_confidence(self):
        with pytest.raises(ValueError):
            ConfidenceScore(1.5)
        with pytest.raises(ValueError):
            ConfidenceScore(-0.1)


class TestOracleConfig:
    """Tests for OracleConfig class."""
    
    def test_default_config(self):
        config = OracleConfig()
        assert config.confidence_threshold == 0.80
        assert config.verification_level == VerificationLevel.STANDARD
        assert config.enable_trinity == True
    
    def test_minimal_config(self):
        config = OracleConfig.minimal()
        assert config.verification_level == VerificationLevel.MINIMAL
        assert config.enable_trinity == False
        assert config.enable_reasoning_traces == False
    
    def test_full_config(self):
        config = OracleConfig.full()
        assert config.verification_level == VerificationLevel.FULL
        assert config.enable_trinity == True
        assert config.enable_chain_of_custody == True
    
    def test_medical_config(self):
        config = OracleConfig.medical()
        assert config.domain == "medical"
        assert config.confidence_threshold == 0.90
        assert "healthcare professional" in config.custom_fail_response
    
    def test_legal_config(self):
        config = OracleConfig.legal()
        assert config.domain == "legal"
        assert config.confidence_threshold == 0.85
        assert "legal advice" in config.custom_fail_response
    
    def test_invalid_threshold(self):
        with pytest.raises(ValueError):
            OracleConfig(confidence_threshold=1.5)


class TestReasoningTrace:
    """Tests for ReasoningTrace class."""
    
    def test_add_steps(self):
        trace = ReasoningTrace()
        trace.add_step(
            input_data="Test input",
            analysis="Test analysis",
            conclusion="Test conclusion",
            confidence=0.85
        )
        assert len(trace.steps) == 1
        assert trace.steps[0].step_number == 1
    
    def test_synthesize(self):
        trace = ReasoningTrace()
        trace.add_step("Input 1", "Analysis 1", "Conclusion 1", 0.80)
        trace.add_step("Input 2", "Analysis 2", "Conclusion 2", 0.90)
        trace.synthesize("Final conclusion", caveats=["Caveat 1"])
        
        assert trace.final_conclusion == "Final conclusion"
        assert abs(trace.combined_confidence.value - 0.85) < 0.001
        assert len(trace.caveats) == 1
    
    def test_prompt_format(self):
        trace = ReasoningTrace()
        trace.add_step("Test", "Analysis", "Conclusion", 0.80)
        trace.synthesize("Final")
        
        formatted = trace.to_prompt_format()
        assert "[REASONING_STEP_1]" in formatted
        assert "[FINAL_SYNTHESIS]" in formatted


class TestTrinityVerification:
    """Tests for TrinityVerification class."""
    
    def test_set_perspectives(self):
        trinity = TrinityVerification(claim="Test claim")
        
        trinity.set_advocate(
            evidence=["Evidence 1", "Evidence 2"],
            confidence=0.85,
            conclusion="STRONG_SUPPORT"
        )
        trinity.set_skeptic(
            evidence=["Counter evidence"],
            confidence=0.70,
            conclusion="WEAK_REJECT"
        )
        trinity.set_arbiter(
            evidence=["Balanced view"],
            confidence=0.80,
            conclusion="Qualified approval",
            decision="APPROVE_WITH_QUALIFICATION"
        )
        
        assert trinity.advocate is not None
        assert trinity.skeptic is not None
        assert trinity.arbiter is not None
        assert trinity.final_decision == "APPROVE_WITH_QUALIFICATION"
    
    def test_prompt_format(self):
        trinity = TrinityVerification(claim="Test claim")
        trinity.set_advocate(["E1"], 0.80, "SUPPORT")
        
        formatted = trinity.to_prompt_format()
        assert "[TRINITY VERIFICATION]" in formatted
        assert "ADVOCATE" in formatted


class TestVerificationResult:
    """Tests for VerificationResult class."""
    
    def test_create_result(self):
        result = VerificationResult(
            claim="Test claim",
            status=VerificationStatus.VERIFIED,
            confidence=ConfidenceScore(0.90),
            source="test_source"
        )
        assert result.status == VerificationStatus.VERIFIED
        assert result.hash is not None
        assert len(result.hash) == 16
    
    def test_prompt_format(self):
        result = VerificationResult(
            claim="Test",
            status=VerificationStatus.VERIFIED,
            confidence=ConfidenceScore(0.85)
        )
        formatted = result.to_prompt_format()
        assert "✅" in formatted
        assert "VERIFIED" in formatted


class TestOracleLayer:
    """Tests for main OracleLayer class."""
    
    def test_create_oracle(self):
        oracle = OracleLayer(auto_detect_provider=False)
        assert oracle.config is not None
        assert oracle.VERSION == "2.1.0"
        assert oracle.CODENAME == "PROMETHEUS"
    
    def test_generate_system_prompt(self):
        oracle = OracleLayer(auto_detect_provider=False)
        prompt = oracle.generate_system_prompt()
        
        assert "<ORACLE_LAYER" in prompt
        assert "version=\"2.1\"" in prompt
        assert "PROMETHEUS" in prompt
        assert "<fabrication:block>" in prompt
        assert "CHECKPOINT" in prompt
    
    def test_generate_compact_prompt(self):
        oracle = OracleLayer(auto_detect_provider=False)
        prompt = oracle.generate_system_prompt(compact=True)
        
        assert "<ORACLE v2.1>" in prompt
        assert "AION-BRAIN" in prompt
        assert len(prompt) < len(oracle.generate_system_prompt())
    
    def test_config_affects_prompt(self):
        oracle_minimal = OracleLayer(
            config=OracleConfig.minimal(),
            auto_detect_provider=False
        )
        oracle_full = OracleLayer(
            config=OracleConfig.full(),
            auto_detect_provider=False
        )
        
        minimal_prompt = oracle_minimal.generate_system_prompt()
        full_prompt = oracle_full.generate_system_prompt()
        
        assert "CROSS_VALIDATION" not in minimal_prompt
        assert "CROSS_VALIDATION" in full_prompt
    
    def test_medical_domain_prompt(self):
        oracle = OracleLayer(
            config=OracleConfig.medical(),
            auto_detect_provider=False
        )
        prompt = oracle.generate_system_prompt()
        
        assert "medical" in prompt.lower()
        assert "[BLACK_BOX]" in prompt
        assert "[CONTRAINDICATED]" in prompt
    
    def test_legal_domain_prompt(self):
        oracle = OracleLayer(
            config=OracleConfig.legal(),
            auto_detect_provider=False
        )
        prompt = oracle.generate_system_prompt()
        
        assert "legal" in prompt.lower()
        assert "Bluebook" in prompt
        assert "[HOLDING]" in prompt
    
    def test_query_without_provider_raises(self):
        oracle = OracleLayer(auto_detect_provider=False)
        with pytest.raises(ValueError) as exc_info:
            oracle.query("Test query")
        assert "No AI provider" in str(exc_info.value)
    
    def test_query_with_mock_provider(self):
        def mock_complete(prompt, system_prompt):
            return f"Mock response [CONFIDENCE:0.85] [SOURCE:test]"
        
        provider = GenericProvider(name="mock", complete_fn=mock_complete)
        oracle = OracleLayer(provider=provider)
        
        response = oracle.query("Test query")
        
        assert response.content is not None
        assert response.verification_markers["sources"] == ["test"]
        assert len(response.confidence_scores) == 1
        assert response.confidence_scores[0].value == 0.85
    
    def test_response_parsing(self):
        def mock_complete(prompt, system_prompt):
            return """Here is my analysis [CONFIDENCE:0.90].
            The claim is supported [SOURCE:PubMed123].
            However, one aspect [VERIFY_REQUIRED:human_review].
            Another point [CONFIDENCE:0.75 ±0.10]."""
        
        provider = GenericProvider(name="mock", complete_fn=mock_complete)
        oracle = OracleLayer(provider=provider)
        
        response = oracle.query("Analyze this")
        
        assert len(response.confidence_scores) == 2
        assert response.verify_required_count == 1
        assert "PubMed123" in response.get_sources()
    
    def test_chain_of_custody(self):
        def mock_complete(prompt, system_prompt):
            return "Response [CONFIDENCE:0.85]"
        
        provider = GenericProvider(name="mock", complete_fn=mock_complete)
        oracle = OracleLayer(
            provider=provider,
            config=OracleConfig.full()
        )
        
        oracle.query("Query 1")
        oracle.query("Query 2")
        
        report = oracle.get_audit_report()
        assert report is not None
        assert "Entry 1" in report
        assert "Entry 2" in report
    
    def test_repr(self):
        oracle = OracleLayer(auto_detect_provider=False)
        repr_str = repr(oracle)
        assert "OracleLayer" in repr_str
        assert "2.1" in repr_str


class TestResponseParsing:
    """Tests for parsing Oracle Layer markers from responses."""
    
    def test_parse_sources(self):
        from oracle_layer.core import ResponseParser
        
        text = "Claim 1 [SOURCE:PubMed123]. Claim 2 [SOURCE:FDA.gov]."
        markers = ResponseParser.extract_markers(text)
        
        assert markers["sources"] == ["PubMed123", "FDA.gov"]
    
    def test_parse_confidence(self):
        from oracle_layer.core import ResponseParser
        
        text = "High confidence [CONFIDENCE:0.95]. Medium [CONFIDENCE:0.70 ±0.15]."
        markers = ResponseParser.extract_markers(text)
        scores = ResponseParser.extract_confidence_scores(markers)
        
        assert len(scores) == 2
        assert scores[0].value == 0.95
        assert scores[1].value == 0.70
        assert scores[1].epistemic_uncertainty == 0.15
    
    def test_parse_verify_required(self):
        from oracle_layer.core import ResponseParser
        
        text = "Uncertain [VERIFY_REQUIRED]. Needs review [VERIFY_REQUIRED:human_review]."
        markers = ResponseParser.extract_markers(text)
        count = ResponseParser.count_verify_required(markers)
        
        assert count == 2
    
    def test_parse_safety_flags(self):
        from oracle_layer.core import ResponseParser
        
        text = "SAFETY FLAG: Consult a physician before taking this medication."
        markers = ResponseParser.extract_markers(text)
        
        assert len(markers["safety_flags"]) == 1
        assert "physician" in markers["safety_flags"][0]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
