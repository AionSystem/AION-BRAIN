"""
DECISION ENGINE v1.0 - Framework 4: Bergson
============================================

Temporal Phase Assessment based on Henri Bergson's philosophy of time.
"""

from dataclasses import dataclass
from typing import List, Optional
from ..scoring import (
    TemporalPhase, TemporalVerdict, TemporalAlignment
)


class BergsonFramework:
    """
    Framework 4: Bergson (Temporal Phase Assessment)
    
    Focus: Determine if NOW is the right time for this decision
    Based on: Henri Bergson's philosophy of time
    Key Question: "Is this the right moment?"
    """
    
    PHASE_CHARACTERISTICS = {
        TemporalPhase.GESTATION: {
            "description": "Idea forming, not ready",
            "action_bias": "WAIT",
            "signals": ["unclear vision", "missing pieces", "not yet"]
        },
        TemporalPhase.EMERGENCE: {
            "description": "Conditions aligning",
            "action_bias": "PREPARE",
            "signals": ["coming together", "starting to", "almost ready"]
        },
        TemporalPhase.RIPENESS: {
            "description": "Optimal moment",
            "action_bias": "ACT NOW",
            "signals": ["right time", "now or never", "stars aligned", "ready"]
        },
        TemporalPhase.DECAY: {
            "description": "Opportunity fading",
            "action_bias": "ACT IMMEDIATELY or abandon",
            "signals": ["window closing", "last chance", "running out"]
        },
        TemporalPhase.CLOSURE: {
            "description": "Window closed",
            "action_bias": "ACCEPT, move on",
            "signals": ["too late", "missed", "over", "passed"]
        }
    }
    
    @classmethod
    def detect_phase(cls, decision: str) -> TemporalPhase:
        """Detect current temporal phase from decision text."""
        decision_lower = decision.lower()
        
        for phase, info in cls.PHASE_CHARACTERISTICS.items():
            for signal in info["signals"]:
                if signal in decision_lower:
                    return phase
        
        return TemporalPhase.EMERGENCE
    
    @classmethod
    def assess_external_readiness(cls, decision: str) -> float:
        """Assess external factors alignment (0-10)."""
        score = 5.0
        decision_lower = decision.lower()
        
        positive = ["market growing", "opportunity", "demand", "favorable", "timing"]
        negative = ["recession", "downturn", "competitive", "saturated", "declining"]
        
        for word in positive:
            if word in decision_lower:
                score += 1.0
        
        for word in negative:
            if word in decision_lower:
                score -= 1.0
        
        return max(0.0, min(10.0, score))
    
    @classmethod
    def assess_internal_readiness(cls, decision: str) -> float:
        """Assess internal factors readiness (0-10)."""
        score = 5.0
        decision_lower = decision.lower()
        
        positive = ["ready", "prepared", "experienced", "skilled", "confident", "stable"]
        negative = ["unprepared", "learning", "uncertain", "stressed", "unstable"]
        
        for word in positive:
            if word in decision_lower:
                score += 1.0
        
        for word in negative:
            if word in decision_lower:
                score -= 1.0
        
        return max(0.0, min(10.0, score))
    
    @classmethod
    def determine_verdict(
        cls,
        phase: TemporalPhase,
        external: float,
        internal: float
    ) -> TemporalVerdict:
        """Determine temporal action recommendation."""
        combined = (external + internal) / 2
        
        if phase == TemporalPhase.CLOSURE:
            return TemporalVerdict.ABANDON
        
        if phase == TemporalPhase.RIPENESS and combined >= 6.0:
            return TemporalVerdict.ACT_NOW
        
        if phase == TemporalPhase.DECAY:
            if combined >= 5.0:
                return TemporalVerdict.ACT_NOW
            return TemporalVerdict.ABANDON
        
        if internal >= 6.0 and external >= 6.0:
            return TemporalVerdict.ACT_NOW
        elif internal >= 6.0:
            return TemporalVerdict.WAIT
        else:
            return TemporalVerdict.PREPARE
    
    @classmethod
    def analyze(cls, decision: str) -> TemporalAlignment:
        """Complete Bergson temporal analysis."""
        phase = cls.detect_phase(decision)
        external = cls.assess_external_readiness(decision)
        internal = cls.assess_internal_readiness(decision)
        verdict = cls.determine_verdict(phase, external, internal)
        
        chronos = ["Calendar deadlines", "Age/life stage", "Market windows"]
        kairos = ["Intuitive readiness", "Energy levels", "Relationship alignment"]
        
        return TemporalAlignment(
            phase=phase,
            external_readiness=external,
            internal_readiness=internal,
            chronos_factors=chronos,
            kairos_factors=kairos,
            verdict=verdict
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for Bergson framework."""
        return """
STEP 5: TEMPORAL ASSESSMENT (BERGSON)
├─ Identify current PHASE:
│   ├─ GESTATION: Idea forming, not ready → WAIT
│   ├─ EMERGENCE: Conditions aligning → PREPARE
│   ├─ RIPENESS: Optimal moment → ACT NOW
│   ├─ DECAY: Opportunity fading → ACT IMMEDIATELY or abandon
│   └─ CLOSURE: Window closed → ACCEPT, move on
├─ Assess EXTERNAL alignment (market, timing, opportunity window)
├─ Assess INTERNAL readiness (skills, finances, relationships, health)
├─ Check CHRONOS (calendar deadlines, biological clock)
├─ Check KAIROS (does this FEEL like the right moment?)
└─ Verdict: ACT NOW | WAIT | PREPARE | ABANDON
"""
