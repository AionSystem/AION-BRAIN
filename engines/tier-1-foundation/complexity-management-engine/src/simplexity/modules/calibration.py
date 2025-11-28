"""
SIMPLEXITY v2.0 - Module 6: Cognitive Load Calibration
=======================================================

Match output complexity to user's cognitive capacity.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from ..config import (
    ExpertiseLevel, CognitiveState, TimeAvailable, 
    DecisionStakes, OutputLevel, AudienceProfile
)


@dataclass
class CognitiveProfile:
    """Profile for cognitive calibration."""
    expertise: ExpertiseLevel
    state: CognitiveState
    time: TimeAvailable
    stakes: DecisionStakes
    
    @classmethod
    def from_audience_profile(cls, profile: AudienceProfile) -> "CognitiveProfile":
        return cls(
            expertise=profile.expertise,
            state=profile.state,
            time=profile.time_available,
            stakes=profile.stakes
        )


@dataclass
class CalibrationResult:
    """Result of cognitive calibration."""
    input_profile: CognitiveProfile
    output_level: OutputLevel
    complexity_factor: float
    adjustments: List[str]
    format_recommendations: List[str]
    warnings: List[str] = field(default_factory=list)


class CalibrationModule:
    """
    Module 6: Cognitive Load Calibration (NEW in v2.0)
    
    Match output to user's cognitive capacity based on:
    - Expertise: Novice / Intermediate / Expert / Master
    - State: Focused / Stressed / Fatigued / Crisis
    - Time: Ample / Limited / Urgent / Immediate
    - Stakes: Low / Medium / High / Critical
    
    Output Levels:
    - Level 1: Single insight (crisis mode)
    - Level 2: Executive summary (stressed/limited)
    - Level 3: Standard analysis (normal)
    - Level 4: Deep analysis (high stakes)
    - Level 5: Complete complexity (research/critical)
    """
    
    OUTPUT_LEVEL_FORMATS = {
        OutputLevel.SINGLE_INSIGHT: [
            "One key takeaway",
            "One recommended action",
            "Maximum 3 bullet points"
        ],
        OutputLevel.EXECUTIVE_SUMMARY: [
            "3-5 key points",
            "Prioritized recommendations",
            "Key risks and mitigations"
        ],
        OutputLevel.STANDARD_ANALYSIS: [
            "Full decomposition",
            "Detailed recommendations",
            "Trade-off analysis",
            "Confidence levels"
        ],
        OutputLevel.DEEP_ANALYSIS: [
            "Multiple perspectives",
            "Sensitivity analysis",
            "Scenario planning",
            "Meta-level insights"
        ],
        OutputLevel.COMPLETE_COMPLEXITY: [
            "Full system model",
            "All uncertainties explicit",
            "Second-order effects",
            "Gödelian limitations acknowledged"
        ]
    }
    
    @classmethod
    def determine_output_level(cls, profile: CognitiveProfile) -> OutputLevel:
        """Determine appropriate output level based on profile."""
        if profile.state == CognitiveState.CRISIS:
            return OutputLevel.SINGLE_INSIGHT
        
        if profile.state == CognitiveState.STRESSED or profile.time == TimeAvailable.IMMEDIATE:
            return OutputLevel.EXECUTIVE_SUMMARY
        
        if profile.stakes == DecisionStakes.CRITICAL and profile.expertise == ExpertiseLevel.MASTER:
            return OutputLevel.COMPLETE_COMPLEXITY
        
        if profile.stakes in (DecisionStakes.HIGH, DecisionStakes.CRITICAL):
            return OutputLevel.DEEP_ANALYSIS
        
        return OutputLevel.STANDARD_ANALYSIS
    
    @classmethod
    def calculate_complexity_factor(cls, profile: CognitiveProfile) -> float:
        """Calculate how much to reduce complexity."""
        state_factors = {
            CognitiveState.FOCUSED: 1.0,
            CognitiveState.STRESSED: 0.6,
            CognitiveState.FATIGUED: 0.4,
            CognitiveState.CRISIS: 0.2
        }
        
        expertise_factors = {
            ExpertiseLevel.NOVICE: 0.5,
            ExpertiseLevel.INTERMEDIATE: 0.75,
            ExpertiseLevel.EXPERT: 1.0,
            ExpertiseLevel.MASTER: 1.2
        }
        
        return state_factors[profile.state] * expertise_factors[profile.expertise]
    
    @classmethod
    def calibrate(cls, profile: CognitiveProfile) -> CalibrationResult:
        """Calibrate output for the given cognitive profile."""
        output_level = cls.determine_output_level(profile)
        complexity_factor = cls.calculate_complexity_factor(profile)
        
        adjustments = []
        if profile.state in (CognitiveState.STRESSED, CognitiveState.FATIGUED):
            adjustments.append(f"Reducing complexity by {int((1-complexity_factor)*100)}%")
        
        if profile.expertise == ExpertiseLevel.NOVICE:
            adjustments.append("Using high-level abstraction")
            adjustments.append("Avoiding technical jargon")
        
        format_recommendations = cls.OUTPUT_LEVEL_FORMATS[output_level]
        
        warnings = []
        if profile.state == CognitiveState.CRISIS and profile.stakes == DecisionStakes.CRITICAL:
            warnings.append("High stakes in crisis mode - ensure key information not lost")
        
        return CalibrationResult(
            input_profile=profile,
            output_level=output_level,
            complexity_factor=complexity_factor,
            adjustments=adjustments,
            format_recommendations=format_recommendations,
            warnings=warnings
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for calibration module."""
        return """
MODULE 6: COGNITIVE LOAD CALIBRATION
Match output to user's cognitive capacity:
- Expertise: Novice / Intermediate / Expert / Master
- State: Focused / Stressed / Fatigued / Crisis
- Time: Ample / Limited / Urgent / Immediate
- Stakes: Low / Medium / High / Critical

OUTPUT LEVELS:
- Level 1: Single insight (crisis mode)
- Level 2: Executive summary (stressed/limited)
- Level 3: Standard analysis (normal)
- Level 4: Deep analysis (high stakes)
- Level 5: Complete complexity (research/critical)

COMPLEXITY REDUCTION:
├─ Focused: 100% capacity
├─ Stressed: Reduce 30-50%
├─ Fatigued: Reduce 50-70%
└─ Crisis: Minimum viable complexity only
"""
