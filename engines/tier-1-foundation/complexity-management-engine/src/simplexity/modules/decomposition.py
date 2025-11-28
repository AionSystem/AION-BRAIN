"""
SIMPLEXITY v2.0 - Module 3: Problem Decomposition
==================================================

Break complex problems into independently solvable sub-problems.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from ..scoring import ReversibilityLevel


class DecompositionStrategy(Enum):
    """Decomposition strategies."""
    FUNCTIONAL = "functional"
    STRUCTURAL = "structural"
    TEMPORAL = "temporal"
    STAKEHOLDER = "stakeholder"
    CAUSAL = "causal"


@dataclass
class SubProblem:
    """A decomposed sub-problem."""
    name: str
    description: str
    strategy: DecompositionStrategy
    dependencies: List[str] = field(default_factory=list)
    owner: Optional[str] = None
    priority: int = 0


@dataclass 
class DecompositionResult:
    """Result of problem decomposition."""
    original_problem: str
    strategy_used: DecompositionStrategy
    sub_problems: List[SubProblem]
    reversibility: ReversibilityLevel
    is_mece: bool
    rationale: str
    warnings: List[str] = field(default_factory=list)
    
    @property
    def count(self) -> int:
        return len(self.sub_problems)


class DecompositionModule:
    """
    Module 3: Problem Decomposition
    
    Strategies:
    - FUNCTIONAL: Divides by purpose (best for process improvement)
    - STRUCTURAL: Divides by components (best for system architecture)
    - TEMPORAL: Divides by phases (best for project planning)
    - STAKEHOLDER: Divides by perspective (best for decision-making)
    - CAUSAL: Divides by cause-effect chains (best for root cause analysis)
    
    MECE Criteria:
    - Mutually Exclusive: No overlap between sub-problems
    - Collectively Exhaustive: No gaps, all territory covered
    """
    
    STRATEGY_BEST_FOR = {
        DecompositionStrategy.FUNCTIONAL: "Process improvement",
        DecompositionStrategy.STRUCTURAL: "System architecture",
        DecompositionStrategy.TEMPORAL: "Project planning",
        DecompositionStrategy.STAKEHOLDER: "Decision-making",
        DecompositionStrategy.CAUSAL: "Root cause analysis"
    }
    
    @classmethod
    def recommend_strategy(cls, goal: str) -> DecompositionStrategy:
        """Recommend decomposition strategy based on goal."""
        goal_lower = goal.lower()
        
        if any(kw in goal_lower for kw in ["process", "workflow", "improve"]):
            return DecompositionStrategy.FUNCTIONAL
        elif any(kw in goal_lower for kw in ["architect", "system", "structure"]):
            return DecompositionStrategy.STRUCTURAL
        elif any(kw in goal_lower for kw in ["project", "plan", "phase", "timeline"]):
            return DecompositionStrategy.TEMPORAL
        elif any(kw in goal_lower for kw in ["decide", "stakeholder", "perspective"]):
            return DecompositionStrategy.STAKEHOLDER
        elif any(kw in goal_lower for kw in ["root cause", "why", "cause"]):
            return DecompositionStrategy.CAUSAL
        
        return DecompositionStrategy.STRUCTURAL
    
    @classmethod
    def assess_reversibility(
        cls,
        information_loss: float,
        interface_complexity: float,
        context_dependencies: float,
        organizational_silos: float
    ) -> ReversibilityLevel:
        """Assess how reversible a decomposition is."""
        avg_score = (information_loss + interface_complexity + 
                     context_dependencies + organizational_silos) / 4.0
        
        if avg_score < 2.5:
            return ReversibilityLevel.HIGH
        elif avg_score < 5.0:
            return ReversibilityLevel.MEDIUM
        elif avg_score < 7.5:
            return ReversibilityLevel.LOW
        else:
            return ReversibilityLevel.IRREVERSIBLE
    
    @classmethod
    def decompose(
        cls,
        problem: str,
        strategy: Optional[DecompositionStrategy] = None,
        sub_problems: Optional[List[SubProblem]] = None
    ) -> DecompositionResult:
        """Decompose a problem using the specified strategy."""
        if strategy is None:
            strategy = cls.recommend_strategy(problem)
        
        if sub_problems is None:
            sub_problems = []
        
        is_mece = True
        warnings = []
        
        if len(sub_problems) > 7:
            warnings.append("More than 7 sub-problems may exceed cognitive capacity")
        
        return DecompositionResult(
            original_problem=problem,
            strategy_used=strategy,
            sub_problems=sub_problems,
            reversibility=ReversibilityLevel.HIGH,
            is_mece=is_mece,
            rationale=f"Using {strategy.value} decomposition: {cls.STRATEGY_BEST_FOR[strategy]}",
            warnings=warnings
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for decomposition module."""
        return """
MODULE 3: PROBLEM DECOMPOSITION
Break complex problems into independently solvable sub-problems using:
- Functional decomposition (by purpose)
- Structural decomposition (by components)
- Temporal decomposition (by phases)
- Stakeholder decomposition (by perspective)
- Causal decomposition (by cause-effect chains)

MECE CRITERIA:
- Mutually Exclusive: No overlap between sub-problems
- Collectively Exhaustive: No gaps, all territory covered

REVERSIBILITY SCORE: Can this decomposition be recombined?
- HIGH: Sub-problems easily recombined
- MEDIUM: Recombination possible with effort
- LOW: Decomposition hard to undo
- IRREVERSIBLE: Cannot recombine meaningfully
"""
