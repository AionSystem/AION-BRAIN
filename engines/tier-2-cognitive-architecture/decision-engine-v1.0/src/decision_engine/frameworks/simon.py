"""
DECISION ENGINE v1.0 - Framework 2: Simon
==========================================

Satisficing based on Herbert Simon's bounded rationality.
"""

from dataclasses import dataclass
from typing import List, Optional
from ..scoring import AspirationalLevel, SatisficingResult


class SimonFramework:
    """
    Framework 2: Simon (Satisficing)
    
    Focus: Define "good enough" to prevent analysis paralysis
    Based on: Herbert Simon's bounded rationality research
    Key Question: "What's good enough to stop searching?"
    """
    
    REVERSIBILITY_TIMELINES = {
        "high": "Decide quickly, adjust later (days)",
        "medium": "Take reasonable time, set deadline (1-2 weeks)",
        "low": "Thorough analysis, seek external input (1+ month)"
    }
    
    STOPPING_RULES = {
        "first_good_enough": "Accept first option meeting minimum criteria",
        "best_of_n": "Evaluate N options, pick best (N ≤ 7)",
        "time_bound": "Decide by deadline with best available option",
        "opportunity_cost": "Stop when search cost exceeds expected improvement"
    }
    
    @classmethod
    def assess_reversibility(cls, decision: str) -> str:
        """Assess how reversible the decision is."""
        decision_lower = decision.lower()
        
        irreversible_keywords = ["marriage", "child", "surgery", "tattoo", "permanent"]
        for kw in irreversible_keywords:
            if kw in decision_lower:
                return "low"
        
        reversible_keywords = ["try", "test", "experiment", "temporary", "month"]
        for kw in reversible_keywords:
            if kw in decision_lower:
                return "high"
        
        return "medium"
    
    @classmethod
    def determine_stopping_rule(
        cls,
        decision: str,
        reversibility: str
    ) -> str:
        """Determine appropriate search stopping rule."""
        if reversibility == "high":
            return cls.STOPPING_RULES["first_good_enough"]
        elif reversibility == "low":
            return cls.STOPPING_RULES["best_of_n"]
        else:
            return cls.STOPPING_RULES["time_bound"]
    
    @classmethod
    def derive_aspiration_levels(
        cls,
        decision: str,
        minimum: Optional[str] = None,
        target: Optional[str] = None,
        stretch: Optional[str] = None
    ) -> SatisficingResult:
        """
        Derive aspiration levels for satisficing.
        
        - MINIMUM: Must-haves, proceed if achieved
        - TARGET: Would be great, realistic but ambitious
        - STRETCH: Dream scenario, unlikely but worth pursuing
        """
        if minimum is None:
            minimum = "Basic needs met, no major regrets"
        if target is None:
            target = "Meaningful improvement, sustainable satisfaction"
        if stretch is None:
            stretch = "Exceptional outcome, life-changing success"
        
        reversibility = cls.assess_reversibility(decision)
        deadline = cls.REVERSIBILITY_TIMELINES[reversibility]
        stopping_rule = cls.determine_stopping_rule(decision, reversibility)
        
        return SatisficingResult(
            minimum_outcome=minimum,
            target_outcome=target,
            stretch_outcome=stretch,
            decision_deadline=deadline,
            search_stopping_rule=stopping_rule,
            reversibility_assessment=reversibility,
            current_level=AspirationalLevel.TARGET
        )
    
    @classmethod
    def analyze(
        cls,
        decision: str,
        minimum: Optional[str] = None,
        target: Optional[str] = None,
        stretch: Optional[str] = None
    ) -> SatisficingResult:
        """Complete Simon satisficing analysis."""
        return cls.derive_aspiration_levels(decision, minimum, target, stretch)
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for Simon framework."""
        return """
STEP 3: SATISFICING (SIMON)
├─ Define MINIMUM acceptable outcome (must-haves)
├─ Define TARGET outcome (would be great)
├─ Define STRETCH outcome (dream scenario)
├─ Set decision deadline based on reversibility:
│   ├─ Highly Reversible: Decide quickly, adjust later
│   ├─ Partially Reversible: Take reasonable time, set deadline
│   └─ Irreversible: Thorough analysis, seek external input
└─ Apply search stopping rules:
    ├─ First-Good-Enough: Accept first option meeting minimum
    ├─ Best-of-N: Evaluate N options, pick best (N ≤ 7)
    ├─ Time-Bound: Decide by deadline with best available
    └─ Opportunity Cost: Stop when search cost > improvement
"""
