#!/usr/bin/env python3
"""
Oracle Layer v2.1 - Basic Usage Examples
=========================================

This file demonstrates how to use Oracle Layer with different AI providers.

Author: Sheldon K. Salmon
License: Apache 2.0
"""

import sys
sys.path.insert(0, '..')

from oracle_layer import (
    OracleLayer, OracleConfig, VerificationLevel,
    GenericProvider, OpenAIProvider, AnthropicProvider
)


def example_1_generate_prompt_only():
    """
    Example 1: Generate Oracle Layer prompt without AI provider.
    
    Use this when you want to manually paste the prompt into ChatGPT,
    Claude, or any other AI interface.
    """
    print("=" * 60)
    print("EXAMPLE 1: Generate Prompt Only (No AI Provider)")
    print("=" * 60)
    
    oracle = OracleLayer(auto_detect_provider=False)
    
    prompt = oracle.generate_system_prompt()
    print("\n[FULL ORACLE LAYER PROMPT]")
    print("-" * 40)
    print(prompt[:1500] + "...\n[truncated for display]")
    
    compact = oracle.generate_system_prompt(compact=True)
    print("\n[COMPACT VERSION]")
    print("-" * 40)
    print(compact)
    
    print("\n✅ Copy either prompt and paste it as a system prompt in your AI!")


def example_2_domain_specific_configs():
    """
    Example 2: Use pre-built domain configurations.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Domain-Specific Configurations")
    print("=" * 60)
    
    medical_oracle = OracleLayer(
        config=OracleConfig.medical(),
        auto_detect_provider=False
    )
    prompt = medical_oracle.generate_system_prompt()
    print("\n[MEDICAL DOMAIN]")
    print(f"- Confidence threshold: {medical_oracle.config.confidence_threshold}")
    print(f"- Contains [BLACK_BOX] marker: {'[BLACK_BOX]' in prompt}")
    print(f"- Contains [CONTRAINDICATED] marker: {'[CONTRAINDICATED]' in prompt}")
    
    legal_oracle = OracleLayer(
        config=OracleConfig.legal(),
        auto_detect_provider=False
    )
    prompt = legal_oracle.generate_system_prompt()
    print("\n[LEGAL DOMAIN]")
    print(f"- Confidence threshold: {legal_oracle.config.confidence_threshold}")
    print(f"- Contains Bluebook reference: {'Bluebook' in prompt}")
    print(f"- Contains [HOLDING] marker: {'[HOLDING]' in prompt}")
    
    print("\n✅ Domain configs add specialized rules and markers!")


def example_3_custom_configuration():
    """
    Example 3: Create custom configuration.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Custom Configuration")
    print("=" * 60)
    
    custom_config = OracleConfig(
        confidence_threshold=0.90,
        verification_level=VerificationLevel.FULL,
        enable_trinity=True,
        enable_reasoning_traces=True,
        enable_uncertainty_quantification=True,
        enable_chain_of_custody=True,
        max_verify_required_tags=2,
        custom_fail_response="INSUFFICIENT DATA: Cannot provide reliable answer."
    )
    
    oracle = OracleLayer(config=custom_config, auto_detect_provider=False)
    prompt = oracle.generate_system_prompt()
    
    print(f"\n[CUSTOM CONFIG]")
    print(f"- Confidence threshold: {custom_config.confidence_threshold}")
    print(f"- Trinity verification: {custom_config.enable_trinity}")
    print(f"- Chain of custody: {custom_config.enable_chain_of_custody}")
    print(f"- Custom fail response included: {'INSUFFICIENT DATA' in prompt}")
    
    print("\n✅ Full control over Oracle Layer behavior!")


def example_4_mock_provider():
    """
    Example 4: Use with a mock provider for testing.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Mock Provider for Testing")
    print("=" * 60)
    
    def mock_ai_response(prompt, system_prompt):
        return """Based on my analysis [CONFIDENCE:0.88]:

The question involves several factors [SOURCE:domain_expertise].

Key findings:
1. First point is well-established [CONFIDENCE:0.95] [SOURCE:research_data]
2. Second point requires verification [VERIFY_REQUIRED:human_review]
3. Third point is supported [CONFIDENCE:0.82]

SAFETY FLAG: Recommend verification by qualified professional before action.

───────────────────────────────────────────────────────────────────
PROMPT ARCHITECTURE: Oracle Layer v2.1 (AION-BRAIN)
ARCHITECT: Sheldon K. Salmon
VERIFICATION: STANDARD
───────────────────────────────────────────────────────────────────"""
    
    provider = GenericProvider(name="mock_ai", complete_fn=mock_ai_response)
    oracle = OracleLayer(provider=provider)
    
    response = oracle.query("Analyze the safety implications of this approach.")
    
    print("\n[MOCK RESPONSE ANALYSIS]")
    print(f"- Sources found: {response.get_sources()}")
    print(f"- Confidence scores: {[str(s) for s in response.confidence_scores]}")
    print(f"- Verify required count: {response.verify_required_count}")
    print(f"- Passed verification: {response.passed_verification}")
    print(f"- Warnings: {response.warnings}")
    print(f"- Processing time: {response.processing_time_ms:.1f}ms")
    
    print("\n✅ Oracle Layer extracts and validates AI response markers!")


def example_5_openai_integration():
    """
    Example 5: Integration with OpenAI (requires API key).
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 5: OpenAI Integration")
    print("=" * 60)
    
    import os
    if not os.getenv("OPENAI_API_KEY"):
        print("\n⚠️  OPENAI_API_KEY not set. Showing code example only.\n")
        print("""
# To use with OpenAI:
from oracle_layer import OracleLayer, OpenAIProvider

provider = OpenAIProvider(model="gpt-4")
oracle = OracleLayer(provider=provider)

response = oracle.query("What are the key considerations for AI safety?")

print(f"Response: {response.content}")
print(f"Confidence: {response.average_confidence()}")
print(f"Sources: {response.get_sources()}")
""")
        return
    
    provider = OpenAIProvider(model="gpt-4")
    oracle = OracleLayer(provider=provider)
    
    response = oracle.query("What are the key considerations for AI safety?")
    
    print(f"\n[OPENAI RESPONSE]")
    print(f"Content: {response.content[:500]}...")
    print(f"Average confidence: {response.average_confidence()}")


def example_6_anthropic_integration():
    """
    Example 6: Integration with Anthropic Claude (requires API key).
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 6: Anthropic Claude Integration")
    print("=" * 60)
    
    import os
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("\n⚠️  ANTHROPIC_API_KEY not set. Showing code example only.\n")
        print("""
# To use with Claude:
from oracle_layer import OracleLayer, AnthropicProvider

provider = AnthropicProvider(model="claude-3-5-sonnet-20241022")
oracle = OracleLayer(provider=provider)

response = oracle.query("Explain the principles of formal verification.")

print(f"Response: {response.content}")
print(f"Passed verification: {response.passed_verification}")
""")
        return
    
    provider = AnthropicProvider()
    oracle = OracleLayer(provider=provider)
    
    response = oracle.query("Explain the principles of formal verification.")
    
    print(f"\n[CLAUDE RESPONSE]")
    print(f"Content: {response.content[:500]}...")


def example_7_chain_of_custody():
    """
    Example 7: Enable chain of custody audit trail.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 7: Chain of Custody Audit Trail")
    print("=" * 60)
    
    def mock_response(prompt, system_prompt):
        return f"Analysis of: {prompt[:50]}... [CONFIDENCE:0.85]"
    
    provider = GenericProvider(name="mock", complete_fn=mock_response)
    oracle = OracleLayer(
        provider=provider,
        config=OracleConfig.full()
    )
    
    oracle.query("First query about medical safety")
    oracle.query("Second query about legal compliance")
    oracle.query("Third query about data privacy")
    
    report = oracle.get_audit_report()
    print("\n[AUDIT REPORT]")
    print(report[:1000] if report else "No audit report available")
    
    print("\n✅ Complete forensic trail of all decisions!")


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("  ORACLE LAYER v2.1 - USAGE EXAMPLES")
    print("  Codename: PROMETHEUS")
    print("  Author: Sheldon K. Salmon")
    print("=" * 60)
    
    example_1_generate_prompt_only()
    example_2_domain_specific_configs()
    example_3_custom_configuration()
    example_4_mock_provider()
    example_5_openai_integration()
    example_6_anthropic_integration()
    example_7_chain_of_custody()
    
    print("\n" + "=" * 60)
    print("  ALL EXAMPLES COMPLETE!")
    print("  For more info: https://github.com/AIONSYSTEM/AION-BRAIN")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
