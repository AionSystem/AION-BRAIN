#!/usr/bin/env python3
"""
STRATEGY ENGINE v1.1 - Basic Usage Examples
=============================================

This file demonstrates how to use Strategy Engine with different modes.

Author: Sheldon K. Salmon
License: Apache 2.0
"""

import sys
sys.path.insert(0, '..')

from strategy_engine import (
    StrategyEngine, StrategyConfig, MoatDurabilityIndex,
    CompetitorProfile, EthicsFlag
)


def example_1_generate_prompt():
    """
    Example 1: Generate Strategy Engine prompt for any AI.
    """
    print("=" * 70)
    print("EXAMPLE 1: Generate Prompt (No AI Provider)")
    print("=" * 70)
    
    engine = StrategyEngine()
    
    prompt = engine.generate_system_prompt()
    print("\n[FULL STRATEGY ENGINE PROMPT]")
    print("-" * 40)
    print(prompt[:2000] + "...\n[truncated for display]")
    
    compact = engine.generate_system_prompt(compact=True)
    print("\n[COMPACT VERSION]")
    print("-" * 40)
    print(compact)
    
    print("\n Copy either prompt and paste it as a system prompt in your AI!")


def example_2_moat_durability():
    """
    Example 2: Calculate Moat Durability Index.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Moat Durability Index")
    print("=" * 70)
    
    engine = StrategyEngine()
    
    startup_moat = engine.calculate_moat(
        imitation=4,
        switching=3,
        network=2,
        scale=3,
        brand=2,
        regulatory=1
    )
    print(f"\n[STARTUP MOAT]")
    print(f"- MDI Score: {startup_moat.score:.2f}")
    print(f"- Strength: {startup_moat.strength.value.upper()}")
    print(f"- Durability: {startup_moat.durability_years}")
    print(f"- Weakest dimensions: {startup_moat.get_weakest_dimensions(2)}")
    
    platform_moat = engine.calculate_moat(
        imitation=7,
        switching=8,
        network=9,
        scale=7,
        brand=6,
        regulatory=3
    )
    print(f"\n[PLATFORM COMPANY MOAT]")
    print(f"- MDI Score: {platform_moat.score:.2f}")
    print(f"- Strength: {platform_moat.strength.value.upper()}")
    print(f"- Durability: {platform_moat.durability_years}")
    
    print("\n MDI helps you quantify and improve competitive advantages!")


def example_3_competitive_response():
    """
    Example 3: Simulate competitive responses.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Competitive Response Simulator")
    print("=" * 70)
    
    engine = StrategyEngine()
    
    competitors = [
        CompetitorProfile(name="BigCorp", posture="aggressive", resources="abundant"),
        CompetitorProfile(name="StartupX", posture="opportunistic", resources="constrained"),
        CompetitorProfile(name="OldGuard", posture="defensive", resources="adequate")
    ]
    
    response = engine.simulate_response(
        your_move="Launch aggressive freemium tier",
        competitors=competitors
    )
    
    print(f"\n[YOUR MOVE]: {response.your_move}")
    print(f"\n[COMPETITOR PROFILES]:")
    for comp in response.competitor_profiles:
        print(f"  - {comp.name}: {comp.posture} ({comp.resources})")
    
    print(f"\n[LIKELY RESPONSES]:")
    for r in response.response_matrix:
        print(f"  - {r.competitor}: {r.response_type} ({r.probability}%) → Counter: {r.your_counter}")
    
    print(f"\n[GAME THEORY]:")
    print(f"  - Nash Equilibrium: {response.nash_equilibrium}")
    print(f"  - Optimal Strategy: {response.optimal_strategy}")
    
    print("\n Anticipate competitor moves before they make them!")


def example_4_ethics_check():
    """
    Example 4: Check strategy against ethical guardrails.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Ethics Guardrails")
    print("=" * 70)
    
    engine = StrategyEngine()
    
    good_strategy = engine.check_ethics([
        "Differentiate on quality",
        "Build customer relationships",
        "Innovate faster"
    ])
    print(f"\n[GOOD STRATEGY]")
    print(f"- Ethics Flag: [{good_strategy.flag.value.upper()}]")
    
    risky_strategy = engine.check_ethics([
        "Undercut competitors with predatory pricing",
        "Lock in customers"
    ])
    print(f"\n[RISKY STRATEGY]")
    print(f"- Ethics Flag: [{risky_strategy.flag.value.upper()}]")
    print(f"- Concerns: {risky_strategy.concerns}")
    
    print("\n Strategy Engine won't recommend harmful practices!")


def example_5_full_analysis():
    """
    Example 5: Run complete 6-step strategic analysis.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Full Strategic Analysis")
    print("=" * 70)
    
    engine = StrategyEngine(config=StrategyConfig.full())
    
    analysis = engine.analyze(
        organization="Acme SaaS",
        industry="B2B Project Management",
        strategic_question="How do we compete against Asana, Monday.com, and Notion?",
        competitors=["Asana", "Monday.com", "Notion", "ClickUp"],
        current_advantages=["Construction vertical expertise", "Custom workflows", "Strong support"],
        planned_move="Launch freemium tier to capture market share",
        moat_scores={
            "imitation": 5,
            "switching": 4,
            "network": 3,
            "scale": 4,
            "brand": 3,
            "regulatory": 1
        }
    )
    
    print(analysis.summary())
    
    print(f"\n[DETAILED RESULTS]")
    print(f"- Processing time: {analysis.processing_time_ms:.1f}ms")
    print(f"- Terrain type: {analysis.terrain_analysis['terrain']['type']}")
    print(f"- Top leverage points: {analysis.leverage_analysis['interventions']}")
    
    print("\n Full 6-step analysis gives you the complete strategic picture!")


def example_6_integration():
    """
    Example 6: How to integrate with other AION-BRAIN engines.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Integration with Other Engines")
    print("=" * 70)
    
    print("""
Strategy Engine works well with other AION-BRAIN engines:

1. STRATEGY ENGINE + SIMPLEXITY:
   - Use SIMPLEXITY to reduce strategic complexity
   - Then use Strategy Engine for analysis
   
2. STRATEGY ENGINE + ORACLE LAYER:
   - Use Strategy Engine to develop strategy
   - Then use Oracle Layer to validate assumptions
   
3. STRATEGY ENGINE + DECISION ENGINE:
   - Use Strategy Engine for strategic options
   - Then use Decision Engine for go/no-go decisions

Example workflow:
```python
from strategy_engine import StrategyEngine
from simplexity import Simplexity

# Step 1: Simplify the strategic landscape
simplexity = Simplexity()
complexity = simplexity.analyze("Complex market with 50 competitors")

# Step 2: Strategic analysis on simplified model
strategy = StrategyEngine()
analysis = strategy.analyze(
    organization="Our Company",
    industry="Simplified market view",
    strategic_question="Where should we focus?"
)

# Step 3: Validate with Oracle Layer
# oracle = OracleLayer()
# verified = oracle.verify(analysis.synthesis.causal_assumptions)
```
""")
    
    print(" Combine engines for comprehensive strategic intelligence!")


def main():
    """Run all examples."""
    print("\n" + "=" * 70)
    print("  STRATEGY ENGINE v1.1 - USAGE EXAMPLES")
    print("  Codename: The Strategist's Edge")
    print("  Author: Sheldon K. Salmon")
    print("=" * 70)
    
    example_1_generate_prompt()
    example_2_moat_durability()
    example_3_competitive_response()
    example_4_ethics_check()
    example_5_full_analysis()
    example_6_integration()
    
    print("\n" + "=" * 70)
    print("  ALL EXAMPLES COMPLETE!")
    print("  For more info: https://github.com/AIONSYSTEM/AION-BRAIN")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
