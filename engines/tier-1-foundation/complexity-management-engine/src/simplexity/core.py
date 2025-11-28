"""
SIMPLEXITY v2.0 - Core Engine
==============================

The main Simplexity engine class.

Codename: SIMPLEXITY
Author: Sheldon K. Salmon
License: Apache 2.0
"""

import time
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any

from .config import SimplexityConfig, OperationalMode, AudienceProfile, OutputLevel
from .scoring import (
    ComplexityScore, ComplexityTrajectory, TransferScore, 
    FragilityScore, ReversibilityLevel
)
from .analysis import SimplexityAnalysis, CalibrationResult
from .prompts import PromptBuilder
from .modules.abstraction import AbstractionLevel, AbstractionModule
from .modules.emergence import EmergenceModule
from .modules.decomposition import DecompositionModule
from .modules.simplification import SimplificationModule
from .modules.dynamics import DynamicsModule
from .modules.calibration import CalibrationModule, CognitiveProfile
from .modules.transfer import TransferModule
from .modules.mvc import MVCModule


class Simplexity:
    """
    SIMPLEXITY v2.0 - Complexity Management Engine
    
    The intelligent complexity navigator that transforms overwhelming
    complexity into actionable understanding.
    
    Features:
    - 8-module framework for systematic complexity management
    - Complexity scoring and trajectory tracking
    - Cognitive load calibration for audiences
    - Transfer detection to catch "balloon squeeze" effects
    - Minimum viable complexity targeting
    - Safety alerts and threshold monitoring
    
    Usage:
        # Generate prompts for AI systems
        engine = Simplexity()
        prompt = engine.generate_system_prompt()
        
        # Analyze complexity programmatically
        engine = Simplexity(config=SimplexityConfig.standard())
        analysis = engine.analyze("My complex problem", goal="Understand and simplify")
    
    Author: Sheldon K. Salmon
    Codename: SIMPLEXITY
    """
    
    VERSION = "2.0.0"
    CODENAME = "SIMPLEXITY"
    
    def __init__(
        self,
        config: Optional[SimplexityConfig] = None,
        audience: Optional[AudienceProfile] = None
    ):
        """
        Initialize SIMPLEXITY engine.
        
        Args:
            config: Engine configuration (defaults to standard mode)
            audience: Target audience profile for calibration
        """
        self.config = config or SimplexityConfig.standard()
        self.audience = audience
        self._analysis_history: List[SimplexityAnalysis] = []
    
    def generate_system_prompt(self, compact: bool = False) -> str:
        """
        Generate SIMPLEXITY prompt for AI systems.
        
        Args:
            compact: If True, generate minimal prompt
            
        Returns:
            Formatted prompt string
        """
        if compact:
            return PromptBuilder.build_compact_prompt()
        
        if self.config.mode == OperationalMode.QUICK:
            return PromptBuilder.build_quick_prompt()
        
        return PromptBuilder.build_full_prompt(self.config)
    
    def score_complexity(
        self,
        scale: float = 5.0,
        coupling: float = 5.0,
        dynamics: float = 5.0,
        uncertainty: float = 5.0,
        emergence: float = 5.0,
        trajectory: ComplexityTrajectory = ComplexityTrajectory.STABLE
    ) -> ComplexityScore:
        """
        Create a complexity score.
        
        Args:
            scale: Number of components/variables (1-10)
            coupling: Degree of interdependence (1-10)
            dynamics: Rate and type of change (1-10)
            uncertainty: Unknown unknowns (1-10)
            emergence: System-level novelty (1-10)
            trajectory: Direction of complexity change
            
        Returns:
            ComplexityScore object
        """
        return ComplexityScore(
            scale=scale,
            coupling=coupling,
            dynamics=dynamics,
            uncertainty=uncertainty,
            emergence=emergence,
            trajectory=trajectory
        )
    
    def calibrate_for_audience(
        self,
        audience: Optional[AudienceProfile] = None
    ) -> CalibrationResult:
        """
        Calibrate output for target audience.
        
        Args:
            audience: Audience profile (uses instance audience if not provided)
            
        Returns:
            CalibrationResult with output level and adjustments
        """
        profile = audience or self.audience
        if profile is None:
            profile = AudienceProfile()
        
        cognitive_profile = CognitiveProfile.from_audience_profile(profile)
        result = CalibrationModule.calibrate(cognitive_profile)
        
        return CalibrationResult(
            output_level=result.output_level,
            complexity_factor=result.complexity_factor,
            adjustments=result.adjustments,
            format_recommendations=result.format_recommendations
        )
    
    def check_safety_thresholds(
        self,
        complexity_score: ComplexityScore,
        fragility_score: Optional[FragilityScore] = None,
        transfer_score: Optional[TransferScore] = None
    ) -> List[str]:
        """
        Check for safety threshold violations.
        
        Returns:
            List of safety alert messages
        """
        alerts = []
        
        if complexity_score.exceeds_ceiling(self.config.complexity_ceiling):
            alerts.append(
                f"COMPLEXITY CEILING EXCEEDED: {complexity_score.composite:.1f} > {self.config.complexity_ceiling}"
            )
        
        if complexity_score.trajectory == ComplexityTrajectory.EXPLOSIVE:
            alerts.append("EXPLOSIVE TRAJECTORY: Immediate intervention required")
        
        if fragility_score and not fragility_score.is_safe_to_remove:
            alerts.append(f"FRAGILITY WARNING: {fragility_score.assessment}")
        
        if transfer_score and not transfer_score.is_acceptable:
            alerts.append(
                f"TRANSFER WARNING: Score {transfer_score.score:.1f} - {transfer_score.assessment}"
            )
        
        return alerts
    
    def analyze(
        self,
        problem: str,
        goal: str = "Understand and simplify",
        audience: Optional[AudienceProfile] = None,
        complexity_inputs: Optional[Dict[str, float]] = None
    ) -> SimplexityAnalysis:
        """
        Perform full SIMPLEXITY analysis.
        
        Args:
            problem: Description of the complex problem
            goal: What you need to achieve
            audience: Target audience profile
            complexity_inputs: Optional manual complexity scores
            
        Returns:
            Complete SimplexityAnalysis
        """
        start_time = time.time()
        
        if complexity_inputs:
            score = self.score_complexity(**complexity_inputs)
        else:
            score = self.score_complexity()
        
        calibration = None
        if self.config.enable_calibration and (audience or self.audience):
            calibration = self.calibrate_for_audience(audience)
        
        abstraction = AbstractionModule.analyze(
            current_level=AbstractionLevel.STRUCTURE,
            goal_type="strategic_planning"
        )
        abstraction_result = {
            "current": abstraction.current_level.name,
            "recommended": abstraction.recommended_level.name,
            "zoom": abstraction.zoom_direction
        }
        
        emergence = EmergenceModule.detect(problem)
        emergence_result = {
            "types": [t.value for t in emergence.detected_types],
            "signals": len(emergence.signals),
            "recommendations": emergence.recommendations
        }
        
        decomposition = DecompositionModule.decompose(problem)
        decomposition_result = {
            "strategy": decomposition.strategy_used.value,
            "reversibility": decomposition.reversibility.value,
            "is_mece": decomposition.is_mece
        }
        
        simplification = SimplificationModule.simplify(
            complexity_score=score.composite,
            tolerance="medium"
        )
        simplification_result = {
            "level": simplification.level.value,
            "preservation": simplification.preservation_rate,
            "is_safe": simplification.is_safe
        }
        
        dynamics_result = None
        if self.config.enable_dynamics:
            dynamics = DynamicsModule.analyze(score.composite)
            dynamics_result = {
                "trajectory": dynamics.trajectory.value,
                "velocity": dynamics.velocity,
                "interventions": dynamics.recommended_interventions
            }
        
        transfer_result = None
        if self.config.enable_transfer_detection:
            transfer_result = {
                "likely_destinations": TransferModule.suggest_destinations(problem),
                "recommendation": "Monitor for balloon squeeze effects"
            }
        
        mvc_result = None
        if self.config.enable_mvc:
            mvc_result = {
                "target": "Minimum complexity that achieves goal",
                "protocol": MVCModule.MVC_PROTOCOL[:3]
            }
        
        safety_alerts = []
        if self.config.enable_safety_alerts:
            safety_alerts = self.check_safety_thresholds(score)
        
        recommendations = [score.recommendation]
        if dynamics_result:
            recommendations.extend(dynamics_result.get("interventions", []))
        
        processing_time = (time.time() - start_time) * 1000
        
        analysis = SimplexityAnalysis(
            problem=problem,
            goal=goal,
            audience=audience.expertise.value if audience else None,
            complexity_score=score,
            calibration=calibration,
            abstraction_result=abstraction_result,
            emergence_result=emergence_result,
            decomposition_result=decomposition_result,
            simplification_result=simplification_result,
            dynamics_result=dynamics_result,
            transfer_result=transfer_result,
            mvc_result=mvc_result,
            safety_alerts=safety_alerts,
            recommendations=recommendations,
            processing_time_ms=processing_time
        )
        
        self._analysis_history.append(analysis)
        
        return analysis
    
    def get_analysis_history(self) -> List[SimplexityAnalysis]:
        """Get history of analyses performed."""
        return self._analysis_history.copy()
    
    def __repr__(self) -> str:
        return f"Simplexity(mode={self.config.mode.value}, v{self.VERSION})"
