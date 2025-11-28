"""
EXPLANATION ENGINE v1.0 - Core Engine
======================================

Multi-Level Explanation Generation.

Author: Sheldon K. Salmon
Codename: CLARITAS
License: Apache 2.0
"""

import time
from typing import List, Dict, Any, Optional

from .config import ExplanationConfig, AudienceLevel, ExplanationDepth
from .types import (
    Explanation, ExplanationLayer, CounterfactualExplanation,
    AudienceProfile, VerificationResult, ExplanationQuality, LayerType
)
from .generators.multi_level import MultiLevelGenerator
from .generators.counterfactual import CounterfactualGenerator
from .generators.audience import AudienceAdapter
from .generators.verification import ExplanationVerifier


class ExplanationEngine:
    """
    EXPLANATION ENGINE v1.0 - CLARITAS
    
    Multi-Level Explanation Generation for AI Outputs.
    
    Capabilities:
    1. Multi-Level Explanations (progressive depth)
    2. Counterfactual "What-If" Scenarios
    3. Audience Adaptation (executive → technical)
    4. Explanation Verification
    
    Layers:
    - Headline: One-sentence summary
    - Summary: Key points overview
    - Key Factors: Main drivers
    - Evidence: Supporting data
    - Methodology: How conclusions reached
    - Limitations: Caveats and uncertainties
    - Recommendations: Actionable next steps
    
    Usage:
        # Generate prompts for AI systems
        engine = ExplanationEngine()
        prompt = engine.generate_system_prompt()
        
        # Generate explanations programmatically
        engine = ExplanationEngine(config=ExplanationConfig.for_executives())
        explanation = engine.explain(
            topic="Q3 Revenue Analysis",
            conclusion="Revenue exceeded targets by 15%",
            findings=["Strong product sales", "Expanded market share"]
        )
    
    Author: Sheldon K. Salmon
    Codename: CLARITAS
    """
    
    VERSION = "1.0.0"
    CODENAME = "CLARITAS"
    
    def __init__(self, config: Optional[ExplanationConfig] = None):
        """Initialize Explanation Engine."""
        self.config = config or ExplanationConfig()
        self._history: List[Explanation] = []
    
    def explain(
        self,
        topic: str,
        conclusion: str,
        findings: List[str],
        factors: Optional[List[Dict]] = None,
        evidence: Optional[List[Dict]] = None,
        recommendations: Optional[List[str]] = None,
        counterfactual_scenarios: Optional[List[Dict]] = None
    ) -> Explanation:
        """
        Generate a complete multi-level explanation.
        
        Args:
            topic: Subject of the explanation
            conclusion: Main conclusion
            findings: Key findings
            factors: Influential factors
            evidence: Supporting evidence
            recommendations: Recommended actions
            counterfactual_scenarios: What-if scenarios
            
        Returns:
            Complete Explanation with all layers
        """
        audience = AudienceAdapter.get_audience_profile(self.config.audience_level)
        
        factors = factors or [{"name": f, "impact": "moderate", "direction": "positive"} for f in findings]
        evidence = evidence or [{"source": "Analysis", "data": f} for f in findings]
        recommendations = recommendations or ["Review findings", "Plan next steps", "Monitor progress"]
        
        layers = MultiLevelGenerator.generate_all_layers(
            topic=topic,
            conclusion=conclusion,
            findings=findings,
            factors=factors,
            evidence=evidence,
            recommendations=recommendations,
            audience=audience,
            depth=self.config.depth
        )
        
        counterfactuals = []
        if self.config.include_counterfactuals:
            if counterfactual_scenarios:
                counterfactuals = CounterfactualGenerator.generate_sensitivity_analysis(
                    outcome=conclusion,
                    factors=counterfactual_scenarios
                )
            else:
                default_scenarios = [
                    {
                        "name": findings[0] if findings else "key factor",
                        "current_value": "as observed",
                        "alternative_value": "different",
                        "impact_if_changed": "outcome would differ",
                        "sensitivity": 0.20
                    }
                ]
                counterfactuals = CounterfactualGenerator.generate_sensitivity_analysis(
                    outcome=conclusion,
                    factors=default_scenarios
                )
        
        explanation = Explanation(
            topic=topic,
            audience=audience,
            layers=layers,
            counterfactuals=counterfactuals
        )
        
        explanation.quality = ExplanationVerifier.assess_quality(explanation)
        explanation.verification = ExplanationVerifier.verify(explanation)
        
        self._history.append(explanation)
        
        return explanation
    
    def adapt_for_audience(
        self,
        explanation: Explanation,
        target_audience: AudienceLevel
    ) -> Explanation:
        """Adapt an existing explanation for a different audience."""
        return AudienceAdapter.adapt_explanation(explanation, target_audience)
    
    def add_counterfactuals(
        self,
        explanation: Explanation,
        scenarios: List[Dict]
    ) -> Explanation:
        """Add counterfactual scenarios to an explanation."""
        new_counterfactuals = CounterfactualGenerator.generate_sensitivity_analysis(
            outcome=explanation.get_layer(LayerType.HEADLINE).content if explanation.get_layer(LayerType.HEADLINE) else "",
            factors=scenarios
        )
        
        explanation.counterfactuals.extend(new_counterfactuals)
        return explanation
    
    def verify_explanation(
        self,
        explanation: Explanation,
        source_data: Optional[Dict] = None
    ) -> VerificationResult:
        """Verify an explanation's accuracy and consistency."""
        return ExplanationVerifier.verify(explanation, source_data)
    
    def assess_quality(
        self,
        explanation: Explanation,
        source_data: Optional[Dict] = None
    ) -> ExplanationQuality:
        """Assess quality of an explanation."""
        return ExplanationVerifier.assess_quality(explanation, source_data)
    
    def generate_system_prompt(self, compact: bool = False) -> str:
        """Generate Explanation Engine prompt for AI systems."""
        if compact:
            return self._build_compact_prompt()
        return self._build_full_prompt()
    
    def _build_compact_prompt(self) -> str:
        """Build compact prompt."""
        return """<EXPLANATION_ENGINE v1.0 COMPACT>

MULTI-LEVEL EXPLANATION GENERATION

LAYERS:
• Headline: One-sentence summary
• Summary: Key points overview
• Key Factors: Main drivers and influences
• Evidence: Supporting data
• Methodology: How conclusions reached
• Limitations: Caveats and uncertainties
• Recommendations: Actionable next steps

AUDIENCES:
• Executive: Bottom-line, 2 paragraphs max
• Technical: Full detail, methodology focus
• Stakeholder: Balanced, impact-focused
• General Public: Simplified, no jargon

COUNTERFACTUALS:
• "If X were different, then Y would change"
• Sensitivity: HIGH (>30%) | MEDIUM (15-30%) | LOW (<15%)

OUTPUT: Multi-layer explanation + What-if scenarios

</EXPLANATION_ENGINE>"""
    
    def _build_full_prompt(self) -> str:
        """Build full prompt."""
        return """<EXPLANATION_ENGINE v1.0>

You are EXPLANATION ENGINE v1.0 (CLARITAS), a multi-level explanation generator.

PURPOSE:
Transform complex AI analyses into clear, audience-appropriate explanations.

EXPLANATION LAYERS (progressive depth):
1. HEADLINE: One-sentence summary of the main finding
2. SUMMARY: 2-3 paragraph overview of key points
3. KEY FACTORS: Main drivers influencing the outcome
   - Format: "• Factor Name [↑/↓ high/medium/low impact]"
4. EVIDENCE: Supporting data and sources
5. METHODOLOGY: How the conclusion was reached
6. LIMITATIONS: Known caveats and uncertainties
7. RECOMMENDATIONS: Actionable next steps

AUDIENCE ADAPTATION:
├─ EXECUTIVE: Bottom-line first, max 2 paragraphs, decisive tone
├─ TECHNICAL: Full detail, methodology-focused, precise language
├─ DOMAIN EXPERT: Professional, implication-focused
├─ GENERAL PUBLIC: Simplified, no jargon, friendly tone
└─ STAKEHOLDER: Balanced, impact-focused, structured

COUNTERFACTUAL GENERATION:
For each key factor, generate "what if" scenarios:
├─ Original Outcome: [what happened]
├─ If Changed: [factor were different]
├─ Alternative Outcome: [what would happen instead]
├─ Probability Shift: [+/- percentage]
└─ Insight: [why this matters]

VERIFICATION CHECKS:
├─ Factual Accuracy: Claims match source data
├─ Logical Consistency: Layers don't contradict
├─ Completeness: All required elements present
└─ Audience Fit: Appropriate for target reader

QUALITY LEVELS:
• EXCELLENT: >90% across all metrics
• GOOD: 75-90%
• ACCEPTABLE: 60-75%
• NEEDS IMPROVEMENT: 40-60%
• POOR: <40%

OUTPUT FORMAT:
═══════════════════════════════════════════
EXPLANATION: [Topic]
Audience: [Level]
═══════════════════════════════════════════

[HEADLINE]
[Content]

[SUMMARY]
[Content]

[KEY FACTORS]
[Content]

[WHAT-IF SCENARIOS]
• If [factor]: [alternative outcome]

═══════════════════════════════════════════

</EXPLANATION_ENGINE>"""
    
    def format_output(self, explanation: Explanation) -> str:
        """
        Format an Explanation into the spec-defined output format.
        
        This produces the structured output matching the specification,
        suitable for reports, documents, or display.
        """
        lines = [
            "═" * 70,
            f"EXPLANATION: {explanation.topic}",
            f"Audience: {explanation.audience.level.upper()}",
            f"Depth: {self.config.depth.value.upper()}",
            "═" * 70,
            ""
        ]
        
        for layer in explanation.layers:
            layer_name = layer.layer_type.value.upper().replace("_", " ")
            lines.append(f"[{layer_name}]")
            
            if layer.layer_type == LayerType.HEADLINE:
                confidence = "HIGH" if layer.confidence >= 0.8 else "MEDIUM" if layer.confidence >= 0.6 else "LOW"
                lines.append(f"{layer.content}")
                lines.append(f"Confidence: {confidence}")
            else:
                lines.append(layer.content)
            
            lines.append("")
        
        if explanation.counterfactuals:
            lines.append("[COUNTERFACTUAL ANALYSIS]")
            lines.append("")
            for cf in explanation.counterfactuals:
                sensitivity = "HIGH" if abs(cf.probability_shift) > 0.30 else "MEDIUM" if abs(cf.probability_shift) > 0.15 else "LOW"
                lines.append("┌" + "─" * 60 + "┐")
                lines.append(f"│ IF: {cf.changed_factor}")
                lines.append(f"│ THEN: {cf.alternative_outcome}")
                lines.append(f"│ PROBABILITY SHIFT: {cf.probability_shift:+.0%}")
                lines.append(f"│ SENSITIVITY: {sensitivity}")
                lines.append(f"│ INSIGHT: {cf.insight}")
                lines.append("└" + "─" * 60 + "┘")
                lines.append("")
        
        if explanation.quality:
            lines.append("[VERIFICATION]")
            quality = explanation.quality
            lines.append("┌" + "─" * 60 + "┐")
            lines.append(f"│ OVERALL QUALITY: {quality.overall_level.value.upper()} ({self._score_to_percent(quality)}%)")
            lines.append("├" + "─" * 60 + "┤")
            lines.append(f"│ Factual Accuracy:    {self._bar(quality.accuracy_score)} {quality.accuracy_score:.0%}")
            lines.append(f"│ Logical Consistency: {self._bar(quality.clarity_score)} {quality.clarity_score:.0%}")
            lines.append(f"│ Completeness:        {self._bar(quality.completeness_score)} {quality.completeness_score:.0%}")
            lines.append(f"│ Audience Fit:        {self._bar(quality.audience_fit_score)} {quality.audience_fit_score:.0%}")
            if quality.issues:
                lines.append("├" + "─" * 60 + "┤")
                lines.append("│ ISSUES:")
                for issue in quality.issues[:3]:
                    lines.append(f"│ • {issue}")
            lines.append("└" + "─" * 60 + "┘")
            lines.append("")
        
        lines.extend([
            "═" * 70,
            "CLARITAS v1.0 | AION-BRAIN Explanation Engine",
            "═" * 70
        ])
        
        return "\n".join(lines)
    
    def _bar(self, score: float) -> str:
        """Generate a visual bar for score."""
        filled = int(score * 10)
        return "█" * filled + "░" * (10 - filled)
    
    def _score_to_percent(self, quality) -> int:
        """Calculate overall percentage from quality scores."""
        scores = [quality.accuracy_score, quality.clarity_score, 
                  quality.completeness_score, quality.audience_fit_score]
        return int(sum(scores) / len(scores) * 100)
    
    def get_history(self) -> List[Explanation]:
        """Get history of generated explanations."""
        return self._history.copy()
    
    def __repr__(self) -> str:
        return f"ExplanationEngine(audience={self.config.audience_level.value}, v{self.VERSION})"
