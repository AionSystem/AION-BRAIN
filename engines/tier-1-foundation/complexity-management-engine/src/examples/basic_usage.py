#!/usr/bin/env python3
"""
SIMPLEXITY v2.0 - Basic Usage Examples
=======================================

This file demonstrates how to use SIMPLEXITY with different modes and configurations.

Author: Sheldon K. Salmon
License: Apache 2.0
"""

import sys
sys.path.insert(0, '..')

from simplexity import (
    Simplexity, SimplexityConfig, OperationalMode,
    ComplexityScore, ComplexityTrajectory
)
from simplexity.config import (
    AudienceProfile, ExpertiseLevel, CognitiveState,
    TimeAvailable, DecisionStakes
)


def example_1_generate_prompt():
    """
    Example 1: Generate SIMPLEXITY prompt for any AI.
    
    Use this when you want to manually paste the prompt into ChatGPT,
    Claude, or any other AI interface.
    """
    print("=" * 60)
    print("EXAMPLE 1: Generate Prompt (No AI Provider)")
    print("=" * 60)
    
    engine = Simplexity()
    
    prompt = engine.generate_system_prompt()
    print("\n[FULL SIMPLEXITY PROMPT]")
    print("-" * 40)
    print(prompt[:2000] + "...\n[truncated for display]")
    
    compact = engine.generate_system_prompt(compact=True)
    print("\n[COMPACT VERSION]")
    print("-" * 40)
    print(compact)
    
    print("\n✅ Copy either prompt and paste it as a system prompt in your AI!")


def example_2_operational_modes():
    """
    Example 2: Use different operational modes.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 2: Operational Modes")
    print("=" * 60)
    
    quick = Simplexity(config=SimplexityConfig.quick())
    print(f"\n[QUICK MODE]")
    print(f"- Mode: {quick.config.mode.value}")
    print(f"- Dynamics enabled: {quick.config.enable_dynamics}")
    print(f"- MVC enabled: {quick.config.enable_mvc}")
    
    standard = Simplexity(config=SimplexityConfig.standard())
    print(f"\n[STANDARD MODE]")
    print(f"- Mode: {standard.config.mode.value}")
    print(f"- All modules enabled: True")
    
    deep = Simplexity(config=SimplexityConfig.deep())
    print(f"\n[DEEP MODE]")
    print(f"- Mode: {deep.config.mode.value}")
    print(f"- Complexity ceiling: {deep.config.complexity_ceiling}")
    
    crisis = Simplexity(config=SimplexityConfig.crisis())
    print(f"\n[CRISIS MODE]")
    print(f"- Mode: {crisis.config.mode.value}")
    print(f"- Safety alerts: {crisis.config.enable_safety_alerts}")
    
    print("\n✅ Choose the mode that fits your situation!")


def example_3_complexity_scoring():
    """
    Example 3: Score complexity and understand the results.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Complexity Scoring")
    print("=" * 60)
    
    engine = Simplexity()
    
    simple = engine.score_complexity(scale=2, coupling=2, dynamics=2, uncertainty=2, emergence=2)
    print(f"\n[SIMPLE SYSTEM]")
    print(f"- Composite: {simple.composite:.1f}")
    print(f"- Level: {simple.level}")
    print(f"- Recommendation: {simple.recommendation}")
    
    moderate = engine.score_complexity(scale=5, coupling=5, dynamics=4, uncertainty=4, emergence=3)
    print(f"\n[MODERATE SYSTEM]")
    print(f"- Composite: {moderate.composite:.1f}")
    print(f"- Level: {moderate.level}")
    print(f"- Recommendation: {moderate.recommendation}")
    
    complex_sys = engine.score_complexity(
        scale=8, coupling=7, dynamics=6, uncertainty=5, emergence=4,
        trajectory=ComplexityTrajectory.GROWING
    )
    print(f"\n[COMPLEX SYSTEM]")
    print(f"- Composite: {complex_sys.composite:.1f}")
    print(f"- Level: {complex_sys.level}")
    print(f"- Trajectory: {complex_sys.trajectory.value}")
    print(f"- Recommendation: {complex_sys.recommendation}")
    
    print("\n✅ Complexity scores guide your simplification strategy!")


def example_4_audience_calibration():
    """
    Example 4: Calibrate output for different audiences.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Audience Calibration")
    print("=" * 60)
    
    engine = Simplexity(config=SimplexityConfig.standard())
    
    exec_audience = AudienceProfile(
        expertise=ExpertiseLevel.INTERMEDIATE,
        state=CognitiveState.STRESSED,
        time_available=TimeAvailable.LIMITED,
        stakes=DecisionStakes.HIGH
    )
    exec_calibration = engine.calibrate_for_audience(exec_audience)
    print(f"\n[EXECUTIVE AUDIENCE]")
    print(f"- Output level: {exec_calibration.output_level.name}")
    print(f"- Complexity factor: {exec_calibration.complexity_factor:.0%}")
    print(f"- Adjustments: {exec_calibration.adjustments}")
    
    tech_audience = AudienceProfile(
        expertise=ExpertiseLevel.EXPERT,
        state=CognitiveState.FOCUSED,
        time_available=TimeAvailable.AMPLE,
        stakes=DecisionStakes.HIGH
    )
    tech_calibration = engine.calibrate_for_audience(tech_audience)
    print(f"\n[TECHNICAL EXPERT AUDIENCE]")
    print(f"- Output level: {tech_calibration.output_level.name}")
    print(f"- Complexity factor: {tech_calibration.complexity_factor:.0%}")
    
    crisis_audience = AudienceProfile(
        expertise=ExpertiseLevel.EXPERT,
        state=CognitiveState.CRISIS,
        time_available=TimeAvailable.IMMEDIATE,
        stakes=DecisionStakes.CRITICAL
    )
    crisis_calibration = engine.calibrate_for_audience(crisis_audience)
    print(f"\n[CRISIS SITUATION]")
    print(f"- Output level: {crisis_calibration.output_level.name}")
    print(f"- Complexity factor: {crisis_calibration.complexity_factor:.0%}")
    
    print("\n✅ Always calibrate output for your audience!")


def example_5_safety_alerts():
    """
    Example 5: Check safety thresholds.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Safety Alerts")
    print("=" * 60)
    
    engine = Simplexity()
    
    safe_score = engine.score_complexity(scale=4, coupling=4, dynamics=3, uncertainty=3, emergence=2)
    alerts = engine.check_safety_thresholds(safe_score)
    print(f"\n[SAFE SYSTEM]")
    print(f"- Composite: {safe_score.composite:.1f}")
    print(f"- Alerts: {alerts if alerts else 'None - all clear!'}")
    
    dangerous_score = engine.score_complexity(
        scale=8, coupling=8, dynamics=8, uncertainty=8, emergence=8,
        trajectory=ComplexityTrajectory.EXPLOSIVE
    )
    alerts = engine.check_safety_thresholds(dangerous_score)
    print(f"\n[DANGEROUS SYSTEM]")
    print(f"- Composite: {dangerous_score.composite:.1f}")
    print(f"- Alerts:")
    for alert in alerts:
        print(f"  ⚠ {alert}")
    
    print("\n✅ Safety alerts help prevent disaster!")


def example_6_full_analysis():
    """
    Example 6: Run a complete analysis.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 6: Full Analysis")
    print("=" * 60)
    
    engine = Simplexity(config=SimplexityConfig.standard())
    
    audience = AudienceProfile(
        expertise=ExpertiseLevel.EXPERT,
        state=CognitiveState.FOCUSED,
        time_available=TimeAvailable.LIMITED,
        stakes=DecisionStakes.HIGH
    )
    
    analysis = engine.analyze(
        problem="Our software system has 150+ microservices, frequent outages, and teams struggle to make changes",
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
    
    print(analysis.summary())
    
    print(f"\n[DETAILED RESULTS]")
    print(f"- Processing time: {analysis.processing_time_ms:.1f}ms")
    print(f"- Abstraction: {analysis.abstraction_result}")
    print(f"- Decomposition: {analysis.decomposition_result}")
    
    print("\n✅ Full analysis gives you the complete picture!")


def example_7_integration_with_oracle():
    """
    Example 7: How to integrate with Oracle Layer.
    """
    print("\n" + "=" * 60)
    print("EXAMPLE 7: Integration with Oracle Layer")
    print("=" * 60)
    
    print("""
To use SIMPLEXITY with Oracle Layer:

1. First, use SIMPLEXITY to reduce complexity to MVC
2. Then, use Oracle Layer to quantify uncertainty in the simplified model

Example workflow:
```python
from simplexity import Simplexity
from oracle_layer import OracleLayer

# Step 1: Simplify with SIMPLEXITY
simplexity = Simplexity()
analysis = simplexity.analyze(
    problem="Complex system",
    goal="Make it understandable"
)

# Step 2: Verify with Oracle Layer
oracle = OracleLayer()
simplified_prompt = f'''
Based on SIMPLEXITY analysis (score: {analysis.complexity_score.composite:.1f}):
{analysis.problem}

Provide verified analysis with confidence scores.
'''

# The Oracle Layer adds verification and uncertainty quantification
# to the simplified model from SIMPLEXITY
```
""")
    
    print("✅ SIMPLEXITY + Oracle Layer = Verified Simple Understanding!")


def main():
    """Run all examples."""
    print("\n" + "=" * 60)
    print("  SIMPLEXITY v2.0 - USAGE EXAMPLES")
    print("  Codename: SIMPLEXITY")
    print("  Author: Sheldon K. Salmon")
    print("=" * 60)
    
    example_1_generate_prompt()
    example_2_operational_modes()
    example_3_complexity_scoring()
    example_4_audience_calibration()
    example_5_safety_alerts()
    example_6_full_analysis()
    example_7_integration_with_oracle()
    
    print("\n" + "=" * 60)
    print("  ALL EXAMPLES COMPLETE!")
    print("  For more info: https://github.com/AIONSYSTEM/AION-BRAIN")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
