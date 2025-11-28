"""
STRATEGY ENGINE v1.1 - Framework 5: Ostrom
===========================================

Resource governance and sustainable advantage.
"How do we sustain this advantage?"
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class EcosystemHealth(Enum):
    """Health of the competitive ecosystem."""
    THRIVING = "thriving"
    STABLE = "stable"
    STRESSED = "stressed"
    DECLINING = "declining"


@dataclass
class GovernancePrinciple:
    """One of Ostrom's 8 principles applied strategically."""
    number: int
    name: str
    strategic_question: str
    assessment: str = ""
    score: int = 5


@dataclass
class ResourceGovernance:
    """Complete resource governance analysis."""
    principles: List[GovernancePrinciple]
    sustainability_score: int
    ecosystem_health: EcosystemHealth
    moat_erosion_risks: List[str]
    ecosystem_recommendations: List[str]
    
    def to_dict(self) -> dict:
        return {
            "principles": [
                {"number": p.number, "name": p.name, "score": p.score}
                for p in self.principles
            ],
            "sustainability_score": self.sustainability_score,
            "ecosystem_health": self.ecosystem_health.value,
            "erosion_risks": self.moat_erosion_risks,
            "recommendations": self.ecosystem_recommendations
        }


class OstromFramework:
    """
    Framework 5: Ostrom (Commons Governance)
    
    Focus: Resource sustainability
    Contribution: Maintaining competitive advantage over time
    Strategic Question: "How do we sustain this advantage?"
    """
    
    EIGHT_PRINCIPLES = [
        (1, "Clear Boundaries", "Who is part of our ecosystem? Who is excluded?"),
        (2, "Congruence with Local Conditions", "Does strategy fit market realities?"),
        (3, "Collective-Choice Arrangements", "Who makes strategic decisions?"),
        (4, "Monitoring", "How do we track competitive position?"),
        (5, "Graduated Sanctions", "How do we respond to competitive threats?"),
        (6, "Conflict Resolution", "How do we handle internal disputes?"),
        (7, "Minimal Recognition of Rights", "Is our right to compete recognized?"),
        (8, "Nested Enterprises", "How does local strategy fit global picture?")
    ]
    
    EROSION_FACTORS = [
        ("technology_shift", "New entrants with better tech"),
        ("commoditization", "Price pressure, feature parity"),
        ("regulatory_change", "New laws removing barriers"),
        ("talent_drain", "Key people leaving"),
        ("customer_shift", "Preferences changing"),
        ("ecosystem_collapse", "Key partners failing")
    ]
    
    @classmethod
    def assess_governance(
        cls,
        organization_description: str,
        current_advantages: Optional[List[str]] = None
    ) -> ResourceGovernance:
        """Assess resource governance and sustainability."""
        principles = []
        for num, name, question in cls.EIGHT_PRINCIPLES:
            principles.append(GovernancePrinciple(
                number=num,
                name=name,
                strategic_question=question,
                score=5
            ))
        
        avg_score = sum(p.score for p in principles) / len(principles)
        sustainability = int(avg_score)
        
        if sustainability >= 7:
            health = EcosystemHealth.THRIVING
        elif sustainability >= 5:
            health = EcosystemHealth.STABLE
        elif sustainability >= 3:
            health = EcosystemHealth.STRESSED
        else:
            health = EcosystemHealth.DECLINING
        
        erosion_risks = ["Technology disruption", "Commoditization pressure"]
        
        recommendations = [
            "Strengthen monitoring of competitive position",
            "Build conflict resolution mechanisms",
            "Ensure strategy alignment across organization levels"
        ]
        
        return ResourceGovernance(
            principles=principles,
            sustainability_score=sustainability,
            ecosystem_health=health,
            moat_erosion_risks=erosion_risks,
            ecosystem_recommendations=recommendations
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for Ostrom framework."""
        return """
STEP 5: RESOURCE GOVERNANCE (Ostrom)
Assess sustainability of competitive advantage:

OSTROM'S 8 PRINCIPLES (Strategic Application):

1. CLEAR BOUNDARIES
   └─ Who is part of our ecosystem? Who is excluded?

2. CONGRUENCE WITH LOCAL CONDITIONS
   └─ Does strategy fit market realities?

3. COLLECTIVE-CHOICE ARRANGEMENTS
   └─ Who makes strategic decisions? Are stakeholders aligned?

4. MONITORING
   └─ How do we track competitive position? Early warning systems?

5. GRADUATED SANCTIONS
   └─ How do we respond to competitive threats?

6. CONFLICT RESOLUTION
   └─ How do we handle internal disputes?

7. MINIMAL RECOGNITION OF RIGHTS
   └─ Is our right to compete recognized? Regulatory positioning?

8. NESTED ENTERPRISES
   └─ How does local strategy fit global picture?

SUSTAINABILITY ASSESSMENT:
├─ Moat Durability: [How long will advantages last?]
├─ Resource Depletion Risk: [Are we exhausting our advantages?]
└─ Ecosystem Health: [Is our ecosystem sustainable?]
"""
