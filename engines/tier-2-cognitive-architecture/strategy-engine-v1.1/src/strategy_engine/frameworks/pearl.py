"""
STRATEGY ENGINE v1.1 - Framework 4: Pearl
==========================================

Causal inference and mechanism identification.
"What actually causes success?"
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Dict


class EvidenceStrength(Enum):
    """Strength of evidence for causal claims."""
    STRONG = "strong"
    MODERATE = "moderate"
    WEAK = "weak"


class CausalConfidence(Enum):
    """Overall confidence in causal model."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class CausalAssumption:
    """A causal assumption in the strategy."""
    statement: str
    evidence: EvidenceStrength
    testable: bool = True
    falsification_test: str = ""


@dataclass
class CausalRelationship:
    """A causal relationship between variables."""
    cause: str
    effect: str
    mechanism: str = ""
    confidence: EvidenceStrength = EvidenceStrength.MODERATE


@dataclass
class CausalModel:
    """Complete causal model for strategic analysis."""
    variables: List[str]
    relationships: List[CausalRelationship]
    assumptions: List[CausalAssumption]
    confounders: List[str]
    overall_confidence: CausalConfidence
    what_must_be_true: List[str]
    what_would_disprove: List[str]
    
    def to_dict(self) -> dict:
        return {
            "variables": self.variables,
            "relationships": [
                {"cause": r.cause, "effect": r.effect, "confidence": r.confidence.value}
                for r in self.relationships
            ],
            "assumptions": [
                {"statement": a.statement, "evidence": a.evidence.value}
                for a in self.assumptions
            ],
            "confounders": self.confounders,
            "confidence": self.overall_confidence.value,
            "must_be_true": self.what_must_be_true,
            "would_disprove": self.what_would_disprove
        }


class PearlFramework:
    """
    Framework 4: Pearl (Causal Inference)
    
    Focus: Causal mechanisms
    Contribution: What drives success vs. mere correlation
    Strategic Question: "What actually causes success?"
    """
    
    CAUSAL_QUESTIONS = [
        ("association", "What correlates with success?"),
        ("intervention", "If we do X, will Y happen?"),
        ("counterfactual", "Would Y have happened without X?")
    ]
    
    @classmethod
    def build_causal_model(
        cls,
        strategy_description: str,
        key_variables: Optional[List[str]] = None,
        assumptions: Optional[List[str]] = None
    ) -> CausalModel:
        """Build a causal model for the strategy."""
        if key_variables is None:
            key_variables = ["market_share", "customer_satisfaction", "revenue"]
        if assumptions is None:
            assumptions = []
        
        relationships = []
        if len(key_variables) >= 2:
            relationships.append(CausalRelationship(
                cause=key_variables[0],
                effect=key_variables[-1],
                confidence=EvidenceStrength.MODERATE
            ))
        
        causal_assumptions = [
            CausalAssumption(
                statement=a,
                evidence=EvidenceStrength.MODERATE,
                testable=True
            ) for a in assumptions
        ]
        
        if not causal_assumptions:
            causal_assumptions.append(CausalAssumption(
                statement="Strategy execution will lead to intended outcomes",
                evidence=EvidenceStrength.MODERATE
            ))
        
        strong_count = sum(1 for a in causal_assumptions if a.evidence == EvidenceStrength.STRONG)
        weak_count = sum(1 for a in causal_assumptions if a.evidence == EvidenceStrength.WEAK)
        
        if strong_count > weak_count:
            confidence = CausalConfidence.HIGH
        elif weak_count > len(causal_assumptions) / 2:
            confidence = CausalConfidence.LOW
        else:
            confidence = CausalConfidence.MEDIUM
        
        must_be_true = [a.statement for a in causal_assumptions[:3]]
        would_disprove = ["Competitors achieve same results without this strategy"]
        
        return CausalModel(
            variables=key_variables,
            relationships=relationships,
            assumptions=causal_assumptions,
            confounders=["market_conditions", "timing", "execution_quality"],
            overall_confidence=confidence,
            what_must_be_true=must_be_true,
            what_would_disprove=would_disprove
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for Pearl framework."""
        return """
STEP 4: CAUSAL MODEL (Pearl)
Distinguish what actually drives success from correlation:

CAUSAL GRAPH CONSTRUCTION:
├─ Identify variables (inputs, outputs, confounders)
├─ Draw causal arrows (X → Y means X causes Y)
├─ Identify confounders (C → X and C → Y)
└─ Find instrumental variables (I → X → Y)

CAUSAL QUESTIONS:
├─ ASSOCIATION: "What correlates with success?"
├─ INTERVENTION: "If we do X, will Y happen?"
├─ COUNTERFACTUAL: "Would Y have happened without X?"

CAUSAL ASSUMPTIONS AUDIT:
├─ Assumption 1: [State it] → Evidence: [Strong/Moderate/Weak]
├─ Assumption 2: [State it] → Evidence: [Strong/Moderate/Weak]
├─ Assumption 3: [State it] → Evidence: [Strong/Moderate/Weak]
└─ Overall Causal Confidence: [HIGH | MEDIUM | LOW]

STRATEGIC IMPLICATIONS:
├─ "What must be TRUE for our strategy to work?"
├─ "What would DISPROVE our strategic thesis?"
└─ "What are we assuming that competitors aren't?"
"""
