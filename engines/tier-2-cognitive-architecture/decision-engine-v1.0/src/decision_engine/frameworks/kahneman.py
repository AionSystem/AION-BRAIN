"""
DECISION ENGINE v1.0 - Framework 1: Kahneman
=============================================

Bias Detection based on Daniel Kahneman's behavioral economics.
"""

from dataclasses import dataclass
from typing import List, Optional
from ..scoring import (
    BiasType, BiasAssessment, DebiasingStrategy, PreMortemCause
)


BIAS_KEYWORDS = {
    BiasType.ANCHORING: ["first", "initial", "original", "started with", "they offered"],
    BiasType.LOSS_AVERSION: ["lose", "give up", "sacrifice", "cost", "risk losing"],
    BiasType.AVAILABILITY: ["recently", "just saw", "friend did", "heard about", "everyone"],
    BiasType.CONFIRMATION: ["proves", "confirms", "knew it", "always thought"],
    BiasType.OVERCONFIDENCE: ["definitely", "certainly", "sure", "guaranteed", "no doubt"],
    BiasType.STATUS_QUO: ["change is risky", "comfortable", "devil you know", "stable"],
    BiasType.SUNK_COST: ["already invested", "spent years", "too late to stop", "come this far"],
    BiasType.PLANNING_FALLACY: ["should be easy", "won't take long", "just need to", "quick"]
}


DEBIASING_STRATEGIES = {
    BiasType.ANCHORING: "Generate 3 alternative starting points, not just the first number given",
    BiasType.LOSS_AVERSION: "Reframe as 'what do I gain?' instead of 'what do I lose?'",
    BiasType.AVAILABILITY: "Seek statistical base rates, not just recent anecdotes",
    BiasType.CONFIRMATION: "Actively seek disconfirming evidence - what would prove you wrong?",
    BiasType.OVERCONFIDENCE: "Ask 'what would need to be true for me to be wrong?'",
    BiasType.STATUS_QUO: "Calculate the true cost of inaction over 5 years",
    BiasType.SUNK_COST: "Ask 'If I hadn't invested X, would I start now?'",
    BiasType.PLANNING_FALLACY: "Use reference class forecasting - how long did similar projects take?"
}


class KahnemanFramework:
    """
    Framework 1: Kahneman (Bias Detection)
    
    Focus: Identify and mitigate cognitive biases
    Based on: Daniel Kahneman's behavioral economics research
    Key Question: "What biases are distorting this decision?"
    """
    
    @classmethod
    def detect_biases(cls, decision_text: str) -> List[BiasType]:
        """Detect cognitive biases in decision text."""
        detected = []
        text_lower = decision_text.lower()
        
        for bias_type, keywords in BIAS_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    if bias_type not in detected:
                        detected.append(bias_type)
                    break
        
        return detected
    
    @classmethod
    def get_debiasing_strategy(cls, bias: BiasType) -> DebiasingStrategy:
        """Get debiasing strategy for a specific bias."""
        return DebiasingStrategy(
            bias_type=bias,
            strategy=DEBIASING_STRATEGIES.get(bias, "Consider alternative perspectives")
        )
    
    @classmethod
    def run_premortem(
        cls,
        decision: str,
        time_horizon: str = "12 months"
    ) -> List[PreMortemCause]:
        """
        Run pre-mortem analysis: Imagine the decision failed. Why?
        
        Generates potential failure causes ranked by probability and severity.
        """
        generic_causes = [
            PreMortemCause(
                description="Underestimated time/resources required",
                probability=0.40,
                severity="HIGH",
                mitigation="Build in 50% buffer for time and budget"
            ),
            PreMortemCause(
                description="Key assumption proved false",
                probability=0.35,
                severity="HIGH",
                mitigation="Validate assumptions with experiments before full commitment"
            ),
            PreMortemCause(
                description="External circumstances changed unfavorably",
                probability=0.30,
                severity="MEDIUM",
                mitigation="Build flexibility to pivot if environment shifts"
            ),
            PreMortemCause(
                description="Relationship stress from decision impact",
                probability=0.25,
                severity="HIGH",
                mitigation="Align with stakeholders early, set explicit expectations"
            ),
            PreMortemCause(
                description="Opportunity cost of alternatives not taken",
                probability=0.20,
                severity="MEDIUM",
                mitigation="Document alternatives and conditions for revisiting"
            )
        ]
        
        decision_lower = decision.lower()
        
        if "business" in decision_lower or "startup" in decision_lower:
            generic_causes.insert(0, PreMortemCause(
                description="Runway depleted before product-market fit",
                probability=0.45,
                severity="CRITICAL",
                mitigation="Extend runway to 24 months or reduce burn rate 40%"
            ))
        
        if "job" in decision_lower or "career" in decision_lower:
            generic_causes.insert(0, PreMortemCause(
                description="New role/venture didn't match expectations",
                probability=0.35,
                severity="HIGH",
                mitigation="Trial period or side project validation first"
            ))
        
        return generic_causes[:5]
    
    @classmethod
    def analyze(
        cls,
        decision: str,
        include_premortem: bool = True
    ) -> BiasAssessment:
        """Complete Kahneman bias analysis."""
        biases = cls.detect_biases(decision)
        
        strategies = [cls.get_debiasing_strategy(b) for b in biases]
        
        premortem = []
        if include_premortem:
            premortem = cls.run_premortem(decision)
        
        severity = "low"
        if len(biases) >= 3:
            severity = "high"
        elif len(biases) >= 1:
            severity = "medium"
        
        return BiasAssessment(
            detected_biases=biases,
            debiasing_strategies=strategies,
            premortem_causes=premortem,
            bias_severity=severity
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for Kahneman framework."""
        return """
STEP 2: BIAS DETECTION (KAHNEMAN)
├─ Scan for primary biases:
│   ├─ Anchoring (over-relying on first information)
│   ├─ Loss Aversion (losses feel 2x worse than gains)
│   ├─ Availability (recent events weighted too heavily)
│   ├─ Confirmation (seeking supporting evidence only)
│   ├─ Overconfidence (overestimating accuracy)
│   ├─ Status Quo (preferring current state)
│   ├─ Sunk Cost (continuing due to past investment)
│   └─ Planning Fallacy (underestimating time/cost)
├─ Run PRE-MORTEM: Imagine it's 12 months later and decision FAILED. Why?
│   ├─ Generate 5-7 specific failure causes
│   ├─ Rank by probability and severity
│   └─ Create mitigation plans for top 3
└─ Provide debiasing strategy for each detected bias
"""
