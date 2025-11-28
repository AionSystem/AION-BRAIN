"""
SIMPLEXITY v2.0 - Module 2: Emergent Behavior Detection
========================================================

Identify system-level behaviors not predictable from components.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class EmergenceType(Enum):
    """Types of emergent behavior."""
    WEAK = "weak"
    STRONG = "strong"
    ADAPTIVE = "adaptive"


@dataclass
class EmergenceSignal:
    """A detected emergence signal."""
    signal_type: str
    description: str
    severity: str = "medium"


@dataclass
class EmergenceResult:
    """Result of emergence detection."""
    detected_types: List[EmergenceType]
    signals: List[EmergenceSignal]
    system_behaviors: List[str]
    recommendations: List[str]
    
    @property
    def has_emergence(self) -> bool:
        return len(self.detected_types) > 0


class EmergenceModule:
    """
    Module 2: Emergent Behavior Detection
    
    Emergence types:
    - WEAK: Predictable in principle, computationally expensive (e.g., traffic jams)
    - STRONG: Genuinely novel, irreducible (e.g., consciousness)
    - ADAPTIVE: Self-modifying systems (e.g., market behavior)
    
    Signals to watch for:
    - Non-additive effects (whole ≠ sum of parts)
    - Phase transitions (sudden qualitative change)
    - Feedback amplification (small cause, large effect)
    - Pattern formation (order from disorder)
    - Adaptation (system changes in response)
    """
    
    EMERGENCE_DESCRIPTIONS = {
        EmergenceType.WEAK: "Predictable in principle, computationally expensive",
        EmergenceType.STRONG: "Genuinely novel, irreducible",
        EmergenceType.ADAPTIVE: "Self-modifying systems"
    }
    
    SIGNAL_TYPES = [
        "non_additive",
        "phase_transition",
        "feedback_amplification",
        "pattern_formation",
        "adaptation"
    ]
    
    @classmethod
    def detect(
        cls,
        system_description: str,
        observed_behaviors: Optional[List[str]] = None
    ) -> EmergenceResult:
        """Detect emergence patterns in a system."""
        detected = []
        signals = []
        behaviors = observed_behaviors or []
        recommendations = []
        
        if any(kw in system_description.lower() for kw in ["feedback", "amplif", "cascade"]):
            detected.append(EmergenceType.WEAK)
            signals.append(EmergenceSignal(
                signal_type="feedback_amplification",
                description="System shows feedback-driven behavior"
            ))
            recommendations.append("Monitor for cascade effects")
        
        if any(kw in system_description.lower() for kw in ["adapt", "learn", "evolve", "market"]):
            detected.append(EmergenceType.ADAPTIVE)
            signals.append(EmergenceSignal(
                signal_type="adaptation",
                description="System exhibits adaptive behavior"
            ))
            recommendations.append("Account for system self-modification")
        
        if any(kw in system_description.lower() for kw in ["novel", "unexpected", "irreducible"]):
            detected.append(EmergenceType.STRONG)
            signals.append(EmergenceSignal(
                signal_type="pattern_formation",
                description="System shows genuinely novel behavior",
                severity="high"
            ))
            recommendations.append("Cannot fully predict from components")
        
        return EmergenceResult(
            detected_types=detected,
            signals=signals,
            system_behaviors=behaviors,
            recommendations=recommendations
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for emergence module."""
        return """
MODULE 2: EMERGENCE DETECTION
Identify system-level behaviors not predictable from components:
- Type 1 (Weak): Predictable in principle, computationally expensive
- Type 2 (Strong): Genuinely novel, irreducible
- Type 3 (Adaptive): Self-modifying systems

EMERGENCE SIGNALS:
- Non-additive effects (whole ≠ sum of parts)
- Phase transitions (sudden qualitative change)
- Feedback amplification (small cause, large effect)
- Pattern formation (order from disorder)
- Adaptation (system changes in response)
"""
