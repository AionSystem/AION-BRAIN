"""
SIMPLEXITY v2.0 - Module 1: Abstraction Layering
=================================================

Navigate between levels of detail without losing coherence.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional, List


class AbstractionLevel(Enum):
    """The five abstraction levels."""
    PARADIGM = 5
    SYSTEM = 4
    STRUCTURE = 3
    PROCESS = 2
    COMPONENT = 1


@dataclass
class AbstractionResult:
    """Result of abstraction analysis."""
    current_level: AbstractionLevel
    recommended_level: AbstractionLevel
    rationale: str
    zoom_direction: Optional[str] = None
    coherence_notes: List[str] = None
    
    def __post_init__(self):
        if self.coherence_notes is None:
            self.coherence_notes = []


class AbstractionModule:
    """
    Module 1: Abstraction Layering
    
    Navigate between five levels:
    - Level 5: PARADIGM - Mental models, worldviews, fundamental assumptions
    - Level 4: SYSTEM - Interconnected components, feedback loops, emergence
    - Level 3: STRUCTURE - Organizational patterns, relationships, flows
    - Level 2: PROCESS - Sequences, workflows, mechanisms
    - Level 1: COMPONENT - Individual elements, parameters, specific instances
    """
    
    LEVEL_DESCRIPTIONS = {
        AbstractionLevel.PARADIGM: "Mental models, worldviews, fundamental assumptions",
        AbstractionLevel.SYSTEM: "Interconnected components, feedback loops, emergence",
        AbstractionLevel.STRUCTURE: "Organizational patterns, relationships, flows",
        AbstractionLevel.PROCESS: "Sequences, workflows, mechanisms",
        AbstractionLevel.COMPONENT: "Individual elements, parameters, specific instances"
    }
    
    GOAL_RECOMMENDATIONS = {
        "immediate_action": (AbstractionLevel.COMPONENT, AbstractionLevel.PROCESS),
        "tactical_planning": (AbstractionLevel.PROCESS, AbstractionLevel.STRUCTURE),
        "strategic_planning": (AbstractionLevel.STRUCTURE, AbstractionLevel.SYSTEM),
        "vision_transformation": (AbstractionLevel.SYSTEM, AbstractionLevel.PARADIGM)
    }
    
    @classmethod
    def recommend_level(cls, goal_type: str) -> AbstractionLevel:
        """Recommend abstraction level based on goal type."""
        if goal_type in cls.GOAL_RECOMMENDATIONS:
            return cls.GOAL_RECOMMENDATIONS[goal_type][0]
        return AbstractionLevel.STRUCTURE
    
    @classmethod
    def analyze(
        cls,
        current_level: AbstractionLevel,
        goal_type: str,
        signals: Optional[List[str]] = None
    ) -> AbstractionResult:
        """Analyze and recommend abstraction level."""
        recommended = cls.recommend_level(goal_type)
        
        zoom_direction = None
        if recommended.value < current_level.value:
            zoom_direction = "ZOOM IN - Need specifics to act"
        elif recommended.value > current_level.value:
            zoom_direction = "ZOOM OUT - Need perspective to decide"
        
        coherence_notes = []
        if zoom_direction == "ZOOM IN":
            coherence_notes.append("Danger: Getting lost in details")
            coherence_notes.append("Signal: 'But how exactly do I...?'")
        elif zoom_direction == "ZOOM OUT":
            coherence_notes.append("Danger: Losing connection to action")
            coherence_notes.append("Signal: 'But why am I doing this?'")
        
        return AbstractionResult(
            current_level=current_level,
            recommended_level=recommended,
            rationale=f"Goal type '{goal_type}' maps to {recommended.name} level",
            zoom_direction=zoom_direction,
            coherence_notes=coherence_notes
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for abstraction module."""
        return """
MODULE 1: ABSTRACTION LAYERING
Navigate between 5 levels:
- Level 5: Paradigm (mental models, worldviews)
- Level 4: System (interconnected components, feedback loops)
- Level 3: Structure (patterns, relationships, flows)
- Level 2: Process (sequences, workflows)
- Level 1: Component (individual elements)

ZOOM IN: When you need specifics to act
├─ Signal: "But how exactly do I...?"
├─ Action: Descend one level
└─ Danger: Getting lost in details

ZOOM OUT: When you need perspective to decide
├─ Signal: "But why am I doing this?"
├─ Action: Ascend one level
└─ Danger: Losing connection to action
"""
