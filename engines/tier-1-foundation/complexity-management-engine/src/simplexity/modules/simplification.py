"""
SIMPLEXITY v2.0 - Module 4: Simplification Protocols
=====================================================

Reduce complexity while preserving essential dynamics.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from ..scoring import FragilityScore


class SimplificationLevel(Enum):
    """Levels of simplification with preservation rates."""
    PARAMETER_REDUCTION = 1
    COMPONENT_AGGREGATION = 2
    RELATIONSHIP_PRUNING = 3
    DYNAMICS_LINEARIZATION = 4
    STATIC_SNAPSHOT = 5


@dataclass
class SimplificationResult:
    """Result of simplification analysis."""
    level: SimplificationLevel
    preservation_rate: float
    elements_simplified: List[str]
    elements_preserved: List[str]
    fragility_score: FragilityScore
    rationale: str
    warnings: List[str] = field(default_factory=list)
    
    @property
    def is_safe(self) -> bool:
        return self.fragility_score.is_safe_to_remove


class SimplificationModule:
    """
    Module 4: Simplification Protocols
    
    The Simplification Ladder:
    - Level 1: Parameter reduction (95%+ preservation)
    - Level 2: Component aggregation (85%+ preservation)
    - Level 3: Relationship pruning (70%+ preservation)
    - Level 4: Dynamics linearization (60%+ preservation)
    - Level 5: Static snapshot (variable preservation)
    
    80/20 Principle: 80% of effects come from 20% of causes.
    Focus on the vital few.
    
    Anti-Fragility Check before simplifying:
    1. REDUNDANCY CHECK - Does this provide backup/failsafe?
    2. OPTIONALITY CHECK - Does this preserve future flexibility?
    3. STRESS RESPONSE CHECK - Does this help system respond to stress?
    4. LEARNING CHECK - Does this enable system learning/adaptation?
    """
    
    PRESERVATION_RATES = {
        SimplificationLevel.PARAMETER_REDUCTION: 0.95,
        SimplificationLevel.COMPONENT_AGGREGATION: 0.85,
        SimplificationLevel.RELATIONSHIP_PRUNING: 0.70,
        SimplificationLevel.DYNAMICS_LINEARIZATION: 0.60,
        SimplificationLevel.STATIC_SNAPSHOT: 0.50
    }
    
    @classmethod
    def recommend_level(cls, complexity_score: float, tolerance: str = "medium") -> SimplificationLevel:
        """Recommend simplification level based on complexity and tolerance."""
        if tolerance.lower() == "low":
            if complexity_score < 8:
                return SimplificationLevel.PARAMETER_REDUCTION
            return SimplificationLevel.COMPONENT_AGGREGATION
        elif tolerance.lower() == "high":
            if complexity_score > 12:
                return SimplificationLevel.DYNAMICS_LINEARIZATION
            return SimplificationLevel.RELATIONSHIP_PRUNING
        else:
            if complexity_score < 6:
                return SimplificationLevel.PARAMETER_REDUCTION
            elif complexity_score < 10:
                return SimplificationLevel.COMPONENT_AGGREGATION
            else:
                return SimplificationLevel.RELATIONSHIP_PRUNING
    
    @classmethod
    def anti_fragility_check(
        cls,
        element: str,
        redundancy: float = 0.0,
        optionality: float = 0.0,
        stress_response: float = 0.0,
        learning: float = 0.0
    ) -> FragilityScore:
        """Check if removing an element would create fragility."""
        return FragilityScore.calculate(
            redundancy=redundancy,
            optionality=optionality,
            stress_response=stress_response,
            learning=learning,
            rationale=f"Anti-fragility assessment for: {element}"
        )
    
    @classmethod
    def simplify(
        cls,
        complexity_score: float,
        tolerance: str = "medium",
        elements_to_simplify: Optional[List[str]] = None,
        elements_to_preserve: Optional[List[str]] = None,
        fragility_check: Optional[FragilityScore] = None
    ) -> SimplificationResult:
        """Apply simplification at appropriate level."""
        level = cls.recommend_level(complexity_score, tolerance)
        preservation = cls.PRESERVATION_RATES[level]
        
        if elements_to_simplify is None:
            elements_to_simplify = []
        if elements_to_preserve is None:
            elements_to_preserve = []
        
        if fragility_check is None:
            fragility_check = FragilityScore(score=0.0)
        
        warnings = []
        if not fragility_check.is_safe_to_remove:
            warnings.append(f"ANTI-FRAGILITY WARNING: {fragility_check.assessment}")
        
        return SimplificationResult(
            level=level,
            preservation_rate=preservation,
            elements_simplified=elements_to_simplify,
            elements_preserved=elements_to_preserve,
            fragility_score=fragility_check,
            rationale=f"Level {level.value} simplification at {preservation*100:.0f}% preservation",
            warnings=warnings
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for simplification module."""
        return """
MODULE 4: SIMPLIFICATION PROTOCOLS
Reduce complexity while preserving essential dynamics:
- Level 1: Parameter reduction (95% preservation)
- Level 2: Component aggregation (85% preservation)
- Level 3: Relationship pruning (70% preservation)
- Level 4: Dynamics linearization (60% preservation)
- Level 5: Static snapshot (variable preservation)

Apply 80/20 principle: Focus on the vital few.

ANTI-FRAGILITY CHECK before simplifying:
1. REDUNDANCY: Does this provide backup/failsafe capability?
2. OPTIONALITY: Does this preserve future flexibility?
3. STRESS RESPONSE: Does this help system respond to stress?
4. LEARNING: Does this enable system learning/adaptation?

FRAGILITY SCORE:
├─ 0: Safe to remove (no protective function)
├─ 1-3: Minor protective function (proceed with caution)
├─ 4-6: Significant protective function (preserve if possible)
└─ 7-10: Critical protective function (DO NOT REMOVE)
"""
