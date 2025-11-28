"""
DECISION ENGINE v1.0 - Scoring Systems
=======================================

Bias detection, satisficing, optionality, temporal, and ethics scoring.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional, Tuple


class BiasType(Enum):
    """Cognitive biases detected by Kahneman framework."""
    ANCHORING = "anchoring"
    LOSS_AVERSION = "loss_aversion"
    AVAILABILITY = "availability"
    CONFIRMATION = "confirmation"
    OVERCONFIDENCE = "overconfidence"
    STATUS_QUO = "status_quo"
    SUNK_COST = "sunk_cost"
    PLANNING_FALLACY = "planning_fallacy"


@dataclass
class DebiasingStrategy:
    """Strategy to counter a detected bias."""
    bias_type: BiasType
    strategy: str
    applied: bool = False


@dataclass
class PreMortemCause:
    """A potential failure cause from pre-mortem analysis."""
    description: str
    probability: float
    severity: str
    mitigation: str = ""


@dataclass
class BiasAssessment:
    """Complete bias assessment from Kahneman framework."""
    detected_biases: List[BiasType]
    debiasing_strategies: List[DebiasingStrategy]
    premortem_causes: List[PreMortemCause]
    bias_severity: str = "medium"
    
    def to_dict(self) -> dict:
        return {
            "biases": [b.value for b in self.detected_biases],
            "strategies": [
                {"bias": s.bias_type.value, "strategy": s.strategy}
                for s in self.debiasing_strategies
            ],
            "premortem": [
                {"cause": p.description, "probability": p.probability, "severity": p.severity}
                for p in self.premortem_causes
            ],
            "severity": self.bias_severity
        }


class AspirationalLevel(Enum):
    """Aspiration levels for satisficing."""
    STRETCH = "stretch"
    TARGET = "target"
    MINIMUM = "minimum"
    UNACCEPTABLE = "unacceptable"


@dataclass
class SatisficingResult:
    """Result of Simon satisficing analysis."""
    minimum_outcome: str
    target_outcome: str
    stretch_outcome: str
    decision_deadline: str
    search_stopping_rule: str
    reversibility_assessment: str
    current_level: AspirationalLevel = AspirationalLevel.TARGET
    
    def to_dict(self) -> dict:
        return {
            "minimum": self.minimum_outcome,
            "target": self.target_outcome,
            "stretch": self.stretch_outcome,
            "deadline": self.decision_deadline,
            "stopping_rule": self.search_stopping_rule,
            "reversibility": self.reversibility_assessment,
            "current": self.current_level.value
        }


class FragilityCategory(Enum):
    """Fragility classification from Taleb framework."""
    FRAGILE = "fragile"
    ROBUST = "robust"
    ANTIFRAGILE = "antifragile"


@dataclass
class BlackSwanScenario:
    """A black swan stress test scenario."""
    scenario: str
    impact: str
    survival_probability: float
    recovery_plan: str = ""


@dataclass
class OptionalityScore:
    """Optionality assessment from Taleb framework."""
    fragility: FragilityCategory
    reversibility: str
    max_downside: str
    max_upside: str
    optionality_level: str
    barbell_assessment: str
    black_swans: List[BlackSwanScenario]
    via_negativa: List[str]
    
    def to_dict(self) -> dict:
        return {
            "fragility": self.fragility.value,
            "reversibility": self.reversibility,
            "max_downside": self.max_downside,
            "max_upside": self.max_upside,
            "optionality": self.optionality_level,
            "barbell": self.barbell_assessment,
            "black_swans": [
                {"scenario": s.scenario, "impact": s.impact}
                for s in self.black_swans
            ],
            "via_negativa": self.via_negativa
        }


class TemporalPhase(Enum):
    """Temporal phases from Bergson framework."""
    GESTATION = "gestation"
    EMERGENCE = "emergence"
    RIPENESS = "ripeness"
    DECAY = "decay"
    CLOSURE = "closure"


class TemporalVerdict(Enum):
    """Temporal action recommendation."""
    ACT_NOW = "act_now"
    WAIT = "wait"
    PREPARE = "prepare"
    ABANDON = "abandon"


@dataclass
class TemporalAlignment:
    """Temporal assessment from Bergson framework."""
    phase: TemporalPhase
    external_readiness: float
    internal_readiness: float
    chronos_factors: List[str]
    kairos_factors: List[str]
    verdict: TemporalVerdict
    
    def to_dict(self) -> dict:
        return {
            "phase": self.phase.value,
            "external_readiness": self.external_readiness,
            "internal_readiness": self.internal_readiness,
            "chronos": self.chronos_factors,
            "kairos": self.kairos_factors,
            "verdict": self.verdict.value
        }


class EthicalVerdict(Enum):
    """Ethical verdict from Rawls/Singer framework."""
    JUST = "just"
    PROBLEMATIC = "problematic"
    UNJUST = "unjust"


class MoralCircle(Enum):
    """Scope of moral consideration."""
    NARROW = "narrow"
    MODERATE = "moderate"
    EXPANSIVE = "expansive"


@dataclass
class StakeholderImpact:
    """Impact on a single stakeholder."""
    stakeholder: str
    category: str
    utility_impact: int
    reasoning: str = ""


@dataclass
class EthicalAssessment:
    """Ethical assessment from Rawls/Singer framework."""
    stakeholder_impacts: List[StakeholderImpact]
    least_advantaged: str
    veil_of_ignorance_passes: bool
    total_benefits: int
    total_harms: int
    net_utility: int
    moral_circle: MoralCircle
    verdict: EthicalVerdict
    redesign_suggestions: List[str]
    
    def to_dict(self) -> dict:
        return {
            "stakeholders": [
                {"name": s.stakeholder, "category": s.category, "impact": s.utility_impact}
                for s in self.stakeholder_impacts
            ],
            "least_advantaged": self.least_advantaged,
            "veil_passes": self.veil_of_ignorance_passes,
            "benefits": self.total_benefits,
            "harms": self.total_harms,
            "net_utility": self.net_utility,
            "moral_circle": self.moral_circle.value,
            "verdict": self.verdict.value,
            "redesign": self.redesign_suggestions
        }


class ConfidenceLevel(Enum):
    """Confidence in recommendation."""
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    VERY_LOW = "very_low"


class TimelineVerdict(Enum):
    """Timeline recommendation."""
    IMMEDIATE = "immediate"
    WAIT_DAYS = "wait_days"
    WAIT_FOR_TRIGGER = "wait_for_trigger"
    DECLINE = "decline"
