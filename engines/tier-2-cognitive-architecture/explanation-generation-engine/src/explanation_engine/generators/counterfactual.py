"""
EXPLANATION ENGINE v1.0 - Counterfactual Generator
====================================================

Generates "what if" explanations for alternative scenarios.
"""

from typing import List, Dict, Any, Optional
from ..types import CounterfactualExplanation


class CounterfactualGenerator:
    """
    Counterfactual Explanation Generator
    
    Creates "what if" scenarios to help understand:
    - What factors would change the outcome
    - How sensitive the conclusion is to key variables
    - Alternative paths that could have been taken
    """
    
    SENSITIVITY_THRESHOLDS = {
        "high": 0.30,
        "medium": 0.15,
        "low": 0.05
    }
    
    @classmethod
    def generate_counterfactual(
        cls,
        original_outcome: str,
        factor_name: str,
        factor_change: str,
        alternative_outcome: str,
        probability_shift: float,
        insight: Optional[str] = None
    ) -> CounterfactualExplanation:
        """Generate a single counterfactual explanation."""
        if insight is None:
            if abs(probability_shift) > cls.SENSITIVITY_THRESHOLDS["high"]:
                insight = f"The outcome is highly sensitive to {factor_name}"
            elif abs(probability_shift) > cls.SENSITIVITY_THRESHOLDS["medium"]:
                insight = f"{factor_name} has moderate influence on the outcome"
            else:
                insight = f"Changing {factor_name} has limited impact"
        
        return CounterfactualExplanation(
            original_outcome=original_outcome,
            changed_factor=f"{factor_name} changed to {factor_change}",
            alternative_outcome=alternative_outcome,
            probability_shift=probability_shift,
            insight=insight
        )
    
    @classmethod
    def generate_sensitivity_analysis(
        cls,
        outcome: str,
        factors: List[Dict[str, Any]]
    ) -> List[CounterfactualExplanation]:
        """Generate counterfactuals for sensitivity analysis."""
        counterfactuals = []
        
        for factor in factors:
            name = factor.get("name", "factor")
            current = factor.get("current_value", "current")
            alternative = factor.get("alternative_value", "alternative")
            impact = factor.get("impact_if_changed", "different outcome")
            sensitivity = factor.get("sensitivity", 0.15)
            
            cf = cls.generate_counterfactual(
                original_outcome=outcome,
                factor_name=name,
                factor_change=str(alternative),
                alternative_outcome=impact,
                probability_shift=sensitivity
            )
            counterfactuals.append(cf)
        
        return sorted(counterfactuals, key=lambda x: abs(x.probability_shift), reverse=True)
    
    @classmethod
    def generate_decision_alternatives(
        cls,
        decision: str,
        outcome: str,
        alternatives: List[Dict[str, str]]
    ) -> List[CounterfactualExplanation]:
        """Generate counterfactuals for decision alternatives."""
        counterfactuals = []
        
        for alt in alternatives:
            alt_decision = alt.get("alternative", "different choice")
            alt_outcome = alt.get("expected_outcome", "different result")
            probability = alt.get("probability_shift", 0.10)
            
            cf = CounterfactualExplanation(
                original_outcome=outcome,
                changed_factor=f"chose {alt_decision} instead of {decision}",
                alternative_outcome=alt_outcome,
                probability_shift=probability,
                insight=f"Alternative path: {alt_decision}"
            )
            counterfactuals.append(cf)
        
        return counterfactuals
    
    @classmethod
    def generate_timing_counterfactuals(
        cls,
        outcome: str,
        timing_scenarios: List[Dict[str, Any]]
    ) -> List[CounterfactualExplanation]:
        """Generate counterfactuals for timing variations."""
        counterfactuals = []
        
        for scenario in timing_scenarios:
            timing = scenario.get("timing", "different time")
            alt_outcome = scenario.get("outcome", "different result")
            shift = scenario.get("probability_shift", 0.05)
            
            cf = CounterfactualExplanation(
                original_outcome=outcome,
                changed_factor=f"acted {timing}",
                alternative_outcome=alt_outcome,
                probability_shift=shift,
                insight=f"Timing matters: {timing} would change the outcome"
            )
            counterfactuals.append(cf)
        
        return counterfactuals
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for counterfactual generation."""
        return """
COUNTERFACTUAL EXPLANATION GENERATION:
├─ For each key factor:
│   ├─ What if this factor were different?
│   ├─ How would the outcome change?
│   └─ How sensitive is the conclusion to this factor?
├─ Sensitivity Analysis:
│   ├─ HIGH: >30% probability shift
│   ├─ MEDIUM: 15-30% probability shift
│   └─ LOW: <15% probability shift
└─ Format: "If [factor] were [alternative], then [new outcome]"
"""
