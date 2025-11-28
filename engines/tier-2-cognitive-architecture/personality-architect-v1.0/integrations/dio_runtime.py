"""
PERSONALITY ARCHITECT v2.0 - Dynamic Identity Orchestrator (DIO) Runtime
State machine execution for runtime persona adaptation

The DIO manages persona state transitions based on conversation context,
ensuring the persona adapts appropriately while maintaining coherence.

Author: Sheldon K. Salmon (Mr. AION)
License: MIT
"""

import re
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple, Callable
from datetime import datetime

from .persona_loader import PersonaCard


class DriftSeverity(Enum):
    """Severity levels for persona drift detection."""
    NONE = "none"
    MINOR = "minor"
    MODERATE = "moderate"
    MAJOR = "major"
    CRITICAL = "critical"


@dataclass
class PersonaState:
    """Represents a runtime state for a persona."""
    
    name: str
    description: str
    entry_triggers: List[str] = field(default_factory=list)
    exit_triggers: List[str] = field(default_factory=list)
    voice_modifiers: Dict[str, Any] = field(default_factory=dict)
    response_policy: str = ""
    drift_anchors: List[str] = field(default_factory=list)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PersonaState":
        """Create a PersonaState from a dictionary."""
        triggers = data.get("triggers", {})
        return cls(
            name=data.get("state", "UNKNOWN"),
            description=data.get("description", ""),
            entry_triggers=triggers.get("entry", []),
            exit_triggers=triggers.get("exit", []),
            voice_modifiers=data.get("voice_modifiers", {}),
            response_policy=data.get("response_policy", ""),
            drift_anchors=data.get("drift_anchors", []),
        )


@dataclass
class StateTransition:
    """Records a state transition event."""
    
    from_state: str
    to_state: str
    trigger: str
    timestamp: datetime
    rationale: str


@dataclass
class DriftReport:
    """Report from drift detection analysis."""
    
    severity: DriftSeverity
    dimension: str
    deviation: str
    current_state: str
    correction_actions: Dict[str, str] = field(default_factory=dict)


class DIORuntime:
    """
    Dynamic Identity Orchestrator Runtime.
    
    Manages persona state transitions and drift detection during conversations.
    
    Usage:
        from integrations import PersonaLoader, DIORuntime
        
        loader = PersonaLoader()
        persona = loader.load_by_name("Executive Coach")
        
        dio = DIORuntime(persona)
        
        # Analyze user input and get recommended state
        new_state, rationale = dio.analyze_input("I'm feeling really frustrated with my team")
        
        # Transition to the new state
        dio.transition_to(new_state)
        
        # Get current state modifiers for LLM prompt
        modifiers = dio.get_current_modifiers()
    """
    
    def __init__(self, persona: PersonaCard, initial_state: Optional[str] = None):
        self.persona = persona
        self.states: Dict[str, PersonaState] = {}
        self.current_state: Optional[PersonaState] = None
        self.transition_history: List[StateTransition] = []
        self.drift_alerts: List[DriftReport] = []
        
        self._load_states()
        
        if initial_state:
            self._set_initial_state(initial_state)
        elif self.states:
            first_state = list(self.states.keys())[0]
            self._set_initial_state(first_state)
    
    def _load_states(self):
        """Load states from the persona card."""
        for state_data in self.persona.runtime_states:
            state = PersonaState.from_dict(state_data)
            self.states[state.name.upper()] = state
    
    def _set_initial_state(self, state_name: str):
        """Set the initial state."""
        state_name_upper = state_name.upper()
        if state_name_upper in self.states:
            self.current_state = self.states[state_name_upper]
        else:
            raise ValueError(f"State '{state_name}' not found. Available: {list(self.states.keys())}")
    
    def get_available_states(self) -> List[str]:
        """Get list of available state names."""
        return list(self.states.keys())
    
    def get_current_state_name(self) -> str:
        """Get the name of the current state."""
        return self.current_state.name if self.current_state else "NONE"
    
    def get_current_modifiers(self) -> Dict[str, Any]:
        """Get voice modifiers for the current state."""
        if self.current_state:
            return {
                "voice_modifiers": self.current_state.voice_modifiers,
                "response_policy": self.current_state.response_policy,
                "drift_anchors": self.current_state.drift_anchors,
            }
        return {}
    
    def analyze_input(self, user_input: str) -> Tuple[Optional[str], str]:
        """
        Analyze user input to determine if a state transition is needed.
        
        Returns:
            Tuple of (recommended_state, rationale)
            If no transition needed, recommended_state will be None
        """
        
        input_lower = user_input.lower()
        
        if self.current_state:
            for trigger in self.current_state.exit_triggers:
                if self._matches_trigger(input_lower, trigger):
                    for state_name, state in self.states.items():
                        if state_name != self.current_state.name:
                            for entry in state.entry_triggers:
                                if self._matches_trigger(input_lower, entry):
                                    return (
                                        state_name,
                                        f"Exit trigger '{trigger}' matched, entry trigger '{entry}' matched for {state_name}"
                                    )
        
        for state_name, state in self.states.items():
            if self.current_state and state_name == self.current_state.name:
                continue
            
            for trigger in state.entry_triggers:
                if self._matches_trigger(input_lower, trigger):
                    return (
                        state_name,
                        f"Entry trigger '{trigger}' matched for {state_name}"
                    )
        
        return (None, "No state transition triggered")
    
    def _matches_trigger(self, text: str, trigger: str) -> bool:
        """Check if text matches a trigger pattern."""
        
        trigger_lower = trigger.lower()
        
        emotional_patterns = {
            "emotional distress detected": [
                "frustrated", "angry", "upset", "stressed", "anxious",
                "worried", "scared", "overwhelmed", "depressed", "sad",
                "hurt", "disappointed", "confused", "lost", "stuck"
            ],
            "emotional language detected": [
                "feel", "feeling", "felt", "emotion", "heart",
                "struggle", "hard", "difficult", "pain", "joy"
            ],
            "frustration expressed": [
                "frustrated", "annoying", "annoyed", "hate", "angry",
                "why won't", "doesn't work", "broken", "useless"
            ],
            "crisis indicators": [
                "suicide", "kill myself", "end it all", "self-harm",
                "hurt myself", "can't go on", "no point", "want to die"
            ],
            "confusion detected": [
                "confused", "don't understand", "what do you mean",
                "lost", "unclear", "help me understand", "explain"
            ],
            "learning request": [
                "teach me", "how do", "what is", "explain", "learn",
                "show me", "help me understand", "tutorial"
            ],
        }
        
        if trigger_lower in emotional_patterns:
            keywords = emotional_patterns[trigger_lower]
            return any(kw in text for kw in keywords)
        
        trigger_words = trigger_lower.split()
        return any(word in text for word in trigger_words if len(word) > 3)
    
    def transition_to(self, state_name: str, trigger: str = "manual") -> bool:
        """
        Transition to a new state.
        
        Returns:
            True if transition successful, False otherwise
        """
        
        state_name_upper = state_name.upper()
        
        if state_name_upper not in self.states:
            return False
        
        from_state = self.current_state.name if self.current_state else "NONE"
        to_state = state_name_upper
        
        self.current_state = self.states[state_name_upper]
        
        transition = StateTransition(
            from_state=from_state,
            to_state=to_state,
            trigger=trigger,
            timestamp=datetime.now(),
            rationale=f"Transitioned from {from_state} to {to_state} via trigger: {trigger}"
        )
        self.transition_history.append(transition)
        
        return True
    
    def detect_drift(self, response: str) -> DriftReport:
        """
        Analyze a response for drift from the persona's core identity.
        
        Returns:
            DriftReport with severity and correction recommendations
        """
        
        response_lower = response.lower()
        
        voice = self.persona.voice_signature
        favorites = voice.get("favorites", voice.get("vocabulary", {}).get("favorites", []))
        avoids = voice.get("avoids", voice.get("vocabulary", {}).get("avoids", []))
        
        avoid_violations = [word for word in avoids if word.lower() in response_lower]
        favorite_usage = sum(1 for word in favorites if word.lower() in response_lower)
        
        if avoid_violations:
            severity = DriftSeverity.MAJOR if len(avoid_violations) > 2 else DriftSeverity.MODERATE
            report = DriftReport(
                severity=severity,
                dimension="VOCABULARY",
                deviation=f"Used avoided words: {', '.join(avoid_violations)}",
                current_state=self.get_current_state_name(),
                correction_actions={
                    "immediate": f"Avoid these words in next response: {', '.join(avoid_violations)}",
                    "short_term": "Increase usage of signature vocabulary",
                    "persistent": "Review and reinforce vocabulary guidelines",
                }
            )
            self.drift_alerts.append(report)
            return report
        
        if self.current_state and favorite_usage == 0 and len(favorites) > 0:
            anchors = self.current_state.drift_anchors
            anchor_usage = sum(1 for anchor in anchors if anchor.lower() in response_lower)
            
            if anchor_usage == 0 and len(response) > 100:
                report = DriftReport(
                    severity=DriftSeverity.MINOR,
                    dimension="TONE",
                    deviation="No signature vocabulary or state anchors detected",
                    current_state=self.get_current_state_name(),
                    correction_actions={
                        "immediate": f"Consider using: {', '.join(favorites[:3])}",
                        "short_term": "Reintroduce character voice markers",
                    }
                )
                self.drift_alerts.append(report)
                return report
        
        return DriftReport(
            severity=DriftSeverity.NONE,
            dimension="",
            deviation="",
            current_state=self.get_current_state_name(),
        )
    
    def get_state_prompt_addition(self) -> str:
        """Get additional prompt text for the current state."""
        
        if not self.current_state:
            return ""
        
        return self.persona.get_current_state_prompt(self.current_state.name)
    
    def get_transition_log(self) -> List[Dict[str, Any]]:
        """Get the state transition history as a list of dicts."""
        return [
            {
                "from": t.from_state,
                "to": t.to_state,
                "trigger": t.trigger,
                "timestamp": t.timestamp.isoformat(),
                "rationale": t.rationale,
            }
            for t in self.transition_history
        ]
    
    def get_drift_summary(self) -> Dict[str, Any]:
        """Get a summary of drift alerts."""
        
        if not self.drift_alerts:
            return {"status": "COHERENT", "alerts": 0, "details": []}
        
        critical = sum(1 for a in self.drift_alerts if a.severity == DriftSeverity.CRITICAL)
        major = sum(1 for a in self.drift_alerts if a.severity == DriftSeverity.MAJOR)
        moderate = sum(1 for a in self.drift_alerts if a.severity == DriftSeverity.MODERATE)
        minor = sum(1 for a in self.drift_alerts if a.severity == DriftSeverity.MINOR)
        
        if critical > 0:
            status = "CRITICAL_DRIFT"
        elif major > 0:
            status = "MAJOR_DRIFT"
        elif moderate > 0:
            status = "MODERATE_DRIFT"
        elif minor > 0:
            status = "MINOR_DRIFT"
        else:
            status = "COHERENT"
        
        return {
            "status": status,
            "alerts": len(self.drift_alerts),
            "breakdown": {
                "critical": critical,
                "major": major,
                "moderate": moderate,
                "minor": minor,
            },
            "recent_alerts": [
                {
                    "severity": a.severity.value,
                    "dimension": a.dimension,
                    "deviation": a.deviation,
                }
                for a in self.drift_alerts[-5:]
            ]
        }


def run_dio_analysis(
    persona: PersonaCard,
    conversation: List[Dict[str, str]],
    initial_state: Optional[str] = None
) -> Dict[str, Any]:
    """
    Run a full DIO analysis on a conversation.
    
    Args:
        persona: The PersonaCard to analyze with
        conversation: List of {"role": "user"|"assistant", "content": "..."} messages
        initial_state: Optional starting state
        
    Returns:
        Full DIO analysis report
    """
    
    dio = DIORuntime(persona, initial_state)
    
    for msg in conversation:
        if msg["role"] == "user":
            recommended, rationale = dio.analyze_input(msg["content"])
            if recommended:
                dio.transition_to(recommended, trigger=rationale)
        elif msg["role"] == "assistant":
            dio.detect_drift(msg["content"])
    
    return {
        "final_state": dio.get_current_state_name(),
        "transitions": dio.get_transition_log(),
        "drift_summary": dio.get_drift_summary(),
        "available_states": dio.get_available_states(),
    }


if __name__ == "__main__":
    print("DIO Runtime Module")
    print("=" * 50)
    print()
    print("Usage:")
    print("  from integrations import PersonaLoader, DIORuntime")
    print()
    print("  loader = PersonaLoader()")
    print("  persona = loader.load_by_name('Executive Coach')")
    print("  dio = DIORuntime(persona)")
    print()
    print("  state, reason = dio.analyze_input('I feel frustrated')")
    print("  if state:")
    print("      dio.transition_to(state)")
