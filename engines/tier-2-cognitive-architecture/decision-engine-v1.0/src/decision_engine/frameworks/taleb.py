"""
DECISION ENGINE v1.0 - Framework 3: Taleb
==========================================

Antifragility and Optionality based on Nassim Taleb's research.
"""

from dataclasses import dataclass
from typing import List, Optional
from ..scoring import (
    FragilityCategory, OptionalityScore, BlackSwanScenario
)


class TalebFramework:
    """
    Framework 3: Taleb (Antifragility & Optionality)
    
    Focus: Test if decision survives uncertainty and stress
    Based on: Nassim Taleb's antifragility research
    Key Question: "Does this get stronger under stress?"
    """
    
    BLACK_SWAN_TEMPLATES = [
        "Economy crashes 6 months in",
        "Key relationship ends",
        "Health issues arise",
        "Major competitor emerges",
        "Technology becomes obsolete",
        "Regulatory environment changes",
        "Key partner/employee leaves"
    ]
    
    VIA_NEGATIVA_PROMPTS = [
        "What commitments can be removed to reduce risk?",
        "What dependencies can be eliminated?",
        "What complexity can be stripped away?",
        "What assumptions can be challenged?"
    ]
    
    @classmethod
    def classify_fragility(cls, decision: str) -> FragilityCategory:
        """Classify the fragility of a decision."""
        decision_lower = decision.lower()
        
        fragile_keywords = ["all in", "everything", "only option", "no backup"]
        for kw in fragile_keywords:
            if kw in decision_lower:
                return FragilityCategory.FRAGILE
        
        antifragile_keywords = ["learn", "grow", "diversify", "options", "experiment"]
        for kw in antifragile_keywords:
            if kw in decision_lower:
                return FragilityCategory.ANTIFRAGILE
        
        return FragilityCategory.ROBUST
    
    @classmethod
    def assess_optionality(cls, decision: str) -> str:
        """Assess optionality level (asymmetric upside potential)."""
        decision_lower = decision.lower()
        
        if "capped" in decision_lower or "limited downside" in decision_lower:
            return "HIGH"
        
        if "unlimited" in decision_lower or "no ceiling" in decision_lower:
            if "risk" in decision_lower or "all" in decision_lower:
                return "MEDIUM"
            return "HIGH"
        
        if "all" in decision_lower or "everything" in decision_lower:
            return "LOW"
        
        return "MEDIUM"
    
    @classmethod
    def generate_black_swans(
        cls,
        decision: str
    ) -> List[BlackSwanScenario]:
        """Generate relevant black swan scenarios."""
        scenarios = []
        
        for template in cls.BLACK_SWAN_TEMPLATES[:5]:
            survival_prob = 0.5
            if "economy" in template.lower():
                survival_prob = 0.6
            elif "health" in template.lower():
                survival_prob = 0.4
            elif "relationship" in template.lower():
                survival_prob = 0.5
            
            scenarios.append(BlackSwanScenario(
                scenario=template,
                impact="Moderate to Severe",
                survival_probability=survival_prob,
                recovery_plan="Build resilience and backup plans"
            ))
        
        return scenarios
    
    @classmethod
    def assess_barbell(cls, decision: str) -> str:
        """Assess barbell strategy alignment (90% conservative, 10% aggressive)."""
        decision_lower = decision.lower()
        
        if "side" in decision_lower or "experiment" in decision_lower:
            return "ALIGNED: Conservative base maintained while exploring"
        elif "all in" in decision_lower or "quit" in decision_lower:
            return "MISALIGNED: Consider maintaining conservative base"
        else:
            return "PARTIALLY ALIGNED: Evaluate conservative/aggressive split"
    
    @classmethod
    def suggest_via_negativa(cls, decision: str) -> List[str]:
        """Suggest what to remove to reduce risk."""
        suggestions = [
            "Remove single points of failure",
            "Eliminate unnecessary complexity",
            "Reduce dependencies on specific outcomes",
            "Strip away non-essential commitments"
        ]
        
        decision_lower = decision.lower()
        if "job" in decision_lower:
            suggestions.insert(0, "Consider part-time transition before full quit")
        if "business" in decision_lower:
            suggestions.insert(0, "Remove features/commitments until MVP is validated")
        
        return suggestions[:4]
    
    @classmethod
    def analyze(cls, decision: str) -> OptionalityScore:
        """Complete Taleb optionality analysis."""
        fragility = cls.classify_fragility(decision)
        optionality = cls.assess_optionality(decision)
        black_swans = cls.generate_black_swans(decision)
        barbell = cls.assess_barbell(decision)
        via_negativa = cls.suggest_via_negativa(decision)
        
        reversibility = "medium"
        if fragility == FragilityCategory.ANTIFRAGILE:
            reversibility = "high"
        elif fragility == FragilityCategory.FRAGILE:
            reversibility = "low"
        
        return OptionalityScore(
            fragility=fragility,
            reversibility=reversibility,
            max_downside="Assess based on specific decision context",
            max_upside="Evaluate potential unlimited upside",
            optionality_level=optionality,
            barbell_assessment=barbell,
            black_swans=black_swans,
            via_negativa=via_negativa
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for Taleb framework."""
        return """
STEP 4: OPTIONALITY ANALYSIS (TALEB)
├─ Classify: FRAGILE | ROBUST | ANTIFRAGILE
├─ Assess reversibility: Can this be undone? At what cost?
├─ Check optionality: Capped downside + unlimited upside?
├─ Apply BARBELL STRATEGY test:
│   ├─ 90% Conservative: Stable income, emergency fund, core relationships
│   └─ 10% Aggressive: High-risk opportunity, career pivot attempt
├─ Run BLACK SWAN scenarios:
│   ├─ What if economy crashes?
│   ├─ What if key relationship ends?
│   ├─ What if health issues arise?
│   └─ What if competition emerges?
└─ Apply VIA NEGATIVA: What can be REMOVED to reduce risk?
"""
