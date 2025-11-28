"""
SIMPLEXITY v2.0 - Module 8: Minimum Viable Complexity
======================================================

Find the least complexity needed to achieve the goal.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class MVCElement:
    """An element in the minimum viable complexity."""
    name: str
    purpose: str
    is_essential: bool
    justification: str


@dataclass
class MVCResult:
    """Result of MVC analysis."""
    goal: str
    success_criteria: List[str]
    essential_elements: List[MVCElement]
    optional_elements: List[MVCElement]
    removed_elements: List[str]
    mvc_score: float
    original_score: float
    reduction_achieved: float
    when_to_increase: List[str]
    warnings: List[str] = field(default_factory=list)
    
    @property
    def elements_kept(self) -> int:
        return len(self.essential_elements)
    
    @property
    def elements_removed(self) -> int:
        return len(self.removed_elements)


class MVCModule:
    """
    Module 8: Minimum Viable Complexity (NEW in v2.0)
    
    Find the least complexity needed for the goal:
    1. Define success criteria
    2. Start with simplest possible model
    3. Add complexity only when criteria not met
    4. Verify each element is necessary
    5. Document MVC boundary
    
    The goal is not zero complexity, but the minimum that works.
    """
    
    MVC_PROTOCOL = [
        "Define success criteria clearly",
        "Start with simplest possible model",
        "Test against success criteria",
        "Add complexity only when criteria not met",
        "Verify each addition is necessary",
        "Document why each element exists",
        "Identify conditions for MVC increase"
    ]
    
    @classmethod
    def analyze(
        cls,
        goal: str,
        success_criteria: List[str],
        all_elements: List[Dict],
        original_complexity: float
    ) -> MVCResult:
        """Analyze and identify minimum viable complexity."""
        essential = []
        optional = []
        removed = []
        
        for elem in all_elements:
            name = elem.get("name", "unknown")
            purpose = elem.get("purpose", "")
            is_essential = elem.get("essential", False)
            
            mvc_element = MVCElement(
                name=name,
                purpose=purpose,
                is_essential=is_essential,
                justification=elem.get("justification", "")
            )
            
            if is_essential:
                essential.append(mvc_element)
            elif elem.get("keep", True):
                optional.append(mvc_element)
            else:
                removed.append(name)
        
        if all_elements:
            mvc_score = original_complexity * (len(essential) / len(all_elements))
        else:
            mvc_score = original_complexity
        
        reduction = original_complexity - mvc_score
        
        when_to_increase = [
            "Success criteria not met with current model",
            "New requirements added",
            "Edge cases discovered that matter"
        ]
        
        warnings = []
        if len(essential) == 0:
            warnings.append("No essential elements identified - review success criteria")
        if mvc_score < original_complexity * 0.3:
            warnings.append("Large reduction - verify nothing critical removed")
        
        return MVCResult(
            goal=goal,
            success_criteria=success_criteria,
            essential_elements=essential,
            optional_elements=optional,
            removed_elements=removed,
            mvc_score=mvc_score,
            original_score=original_complexity,
            reduction_achieved=reduction,
            when_to_increase=when_to_increase,
            warnings=warnings
        )
    
    @classmethod
    def iterative_build(
        cls,
        goal: str,
        success_criteria: List[str],
        candidate_elements: List[str]
    ) -> List[str]:
        """
        Build MVC iteratively by adding elements one at a time.
        Returns ordered list of elements to add.
        """
        return sorted(candidate_elements, key=lambda x: len(x))
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for MVC module."""
        return """
MODULE 8: MINIMUM VIABLE COMPLEXITY (MVC)
Find the least complexity needed for the goal:
1. Define success criteria
2. Start with simplest possible model
3. Add complexity only when criteria not met
4. Verify each element is necessary
5. Document MVC boundary

MVC PROTOCOL:
├─ What are the success criteria?
├─ What's the simplest model that might work?
├─ What does it get right/wrong?
├─ What single addition would most improve it?
├─ Why is each element necessary?
└─ When would MVC need to increase?

GOAL: Not zero complexity, but minimum that works.
"""
