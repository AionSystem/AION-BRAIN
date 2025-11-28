"""
DECISION ENGINE v1.0 - Framework 5: Rawls/Singer
=================================================

Ethical Validation based on John Rawls and Peter Singer's philosophy.
"""

from dataclasses import dataclass
from typing import List, Optional
from ..scoring import (
    EthicalVerdict, MoralCircle, StakeholderImpact, EthicalAssessment
)


STAKEHOLDER_CATEGORIES = [
    "direct_beneficiaries",
    "direct_losers",
    "indirect_affected",
    "voiceless"
]


class RawlsSingerFramework:
    """
    Framework 5: Rawls/Singer (Ethical Validation)
    
    Focus: Ensure decision is fair to all stakeholders
    Based on: John Rawls' justice theory and Peter Singer's utilitarianism
    Key Question: "Is this fair to everyone affected?"
    """
    
    @classmethod
    def map_stakeholders(
        cls,
        decision: str,
        explicit_stakeholders: Optional[List[str]] = None
    ) -> List[StakeholderImpact]:
        """Map all stakeholders affected by the decision."""
        stakeholders = []
        
        if explicit_stakeholders:
            for s in explicit_stakeholders:
                stakeholders.append(StakeholderImpact(
                    stakeholder=s,
                    category="explicit",
                    utility_impact=0,
                    reasoning="User-provided stakeholder"
                ))
        
        stakeholders.append(StakeholderImpact(
            stakeholder="Self",
            category="direct_beneficiaries",
            utility_impact=50,
            reasoning="Primary decision-maker"
        ))
        
        decision_lower = decision.lower()
        
        if "family" in decision_lower or "partner" in decision_lower:
            stakeholders.append(StakeholderImpact(
                stakeholder="Family/Partner",
                category="indirect_affected",
                utility_impact=-20,
                reasoning="May experience stress or lifestyle changes"
            ))
        
        if "job" in decision_lower or "employer" in decision_lower:
            stakeholders.append(StakeholderImpact(
                stakeholder="Employer/Colleagues",
                category="direct_losers",
                utility_impact=-15,
                reasoning="Transition costs and workload redistribution"
            ))
        
        if "business" in decision_lower or "customer" in decision_lower:
            stakeholders.append(StakeholderImpact(
                stakeholder="Future Customers",
                category="direct_beneficiaries",
                utility_impact=30,
                reasoning="Will benefit from product/service"
            ))
        
        if "children" in decision_lower:
            stakeholders.append(StakeholderImpact(
                stakeholder="Children",
                category="voiceless",
                utility_impact=-10,
                reasoning="May experience uncertainty or lifestyle changes"
            ))
        
        if not explicit_stakeholders and len(stakeholders) < 3:
            stakeholders.append(StakeholderImpact(
                stakeholder="Community",
                category="indirect_affected",
                utility_impact=5,
                reasoning="General societal impact"
            ))
        
        return stakeholders
    
    @classmethod
    def identify_least_advantaged(
        cls,
        stakeholders: List[StakeholderImpact]
    ) -> str:
        """Identify the least advantaged stakeholder (Rawls)."""
        if not stakeholders:
            return "Unknown"
        
        min_impact = min(stakeholders, key=lambda s: s.utility_impact)
        return min_impact.stakeholder
    
    @classmethod
    def veil_of_ignorance_test(
        cls,
        stakeholders: List[StakeholderImpact]
    ) -> bool:
        """
        Rawls' Veil of Ignorance Test:
        Would you design this outcome if you didn't know which stakeholder you'd be?
        """
        if not stakeholders:
            return True
        
        min_impact = min(s.utility_impact for s in stakeholders)
        
        if min_impact < -50:
            return False
        
        total = sum(s.utility_impact for s in stakeholders)
        if total > 0 and min_impact > -30:
            return True
        
        return min_impact > -20
    
    @classmethod
    def calculate_utility(
        cls,
        stakeholders: List[StakeholderImpact]
    ) -> tuple:
        """Calculate utilitarian calculus (Singer)."""
        benefits = sum(s.utility_impact for s in stakeholders if s.utility_impact > 0)
        harms = abs(sum(s.utility_impact for s in stakeholders if s.utility_impact < 0))
        net = benefits - harms
        return benefits, harms, net
    
    @classmethod
    def assess_moral_circle(cls, decision: str) -> MoralCircle:
        """Assess scope of moral consideration."""
        decision_lower = decision.lower()
        
        expansive_keywords = ["future generation", "environment", "global", "society"]
        for kw in expansive_keywords:
            if kw in decision_lower:
                return MoralCircle.EXPANSIVE
        
        moderate_keywords = ["community", "team", "network", "ecosystem"]
        for kw in moderate_keywords:
            if kw in decision_lower:
                return MoralCircle.MODERATE
        
        return MoralCircle.NARROW
    
    @classmethod
    def determine_verdict(
        cls,
        veil_passes: bool,
        net_utility: int,
        moral_circle: MoralCircle
    ) -> EthicalVerdict:
        """Determine ethical verdict."""
        if not veil_passes:
            return EthicalVerdict.UNJUST
        
        if net_utility < -20:
            return EthicalVerdict.UNJUST
        elif net_utility < 10:
            return EthicalVerdict.PROBLEMATIC
        else:
            return EthicalVerdict.JUST
    
    @classmethod
    def suggest_redesigns(
        cls,
        stakeholders: List[StakeholderImpact],
        verdict: EthicalVerdict
    ) -> List[str]:
        """Suggest ways to redesign decision for better ethics."""
        suggestions = []
        
        if verdict == EthicalVerdict.UNJUST:
            suggestions.append("Fundamentally reconsider approach to protect harmed parties")
        
        for s in stakeholders:
            if s.utility_impact < -20:
                suggestions.append(f"Mitigate harm to {s.stakeholder}")
        
        if verdict != EthicalVerdict.JUST:
            suggestions.append("Consider phased approach to minimize disruption")
            suggestions.append("Build in explicit protections for vulnerable stakeholders")
        
        return suggestions[:3]
    
    @classmethod
    def analyze(
        cls,
        decision: str,
        explicit_stakeholders: Optional[List[str]] = None
    ) -> EthicalAssessment:
        """Complete Rawls/Singer ethical analysis."""
        stakeholders = cls.map_stakeholders(decision, explicit_stakeholders)
        least_advantaged = cls.identify_least_advantaged(stakeholders)
        veil_passes = cls.veil_of_ignorance_test(stakeholders)
        benefits, harms, net = cls.calculate_utility(stakeholders)
        moral_circle = cls.assess_moral_circle(decision)
        verdict = cls.determine_verdict(veil_passes, net, moral_circle)
        redesigns = cls.suggest_redesigns(stakeholders, verdict)
        
        return EthicalAssessment(
            stakeholder_impacts=stakeholders,
            least_advantaged=least_advantaged,
            veil_of_ignorance_passes=veil_passes,
            total_benefits=benefits,
            total_harms=harms,
            net_utility=net,
            moral_circle=moral_circle,
            verdict=verdict,
            redesign_suggestions=redesigns
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for Rawls/Singer framework."""
        return """
STEP 6: ETHICAL VALIDATION (RAWLS/SINGER)
├─ MAP all stakeholders:
│   ├─ Direct beneficiaries
│   ├─ Direct losers
│   ├─ Indirect affected
│   └─ Voiceless (future generations, children, environment)
├─ VEIL OF IGNORANCE test (Rawls):
│   ├─ Identify least advantaged stakeholder
│   ├─ Ask: "Would I design this if I might BE them?"
│   └─ If NO: Can decision be redesigned to protect them?
├─ UTILITARIAN CALCULUS (Singer):
│   ├─ Quantify benefits (+ utility units)
│   ├─ Quantify harms (- utility units)
│   └─ Calculate NET UTILITY
├─ MORAL CIRCLE assessment: Narrow | Moderate | Expansive
└─ Verdict: JUST ✅ | PROBLEMATIC ⚠️ | UNJUST ❌
"""
