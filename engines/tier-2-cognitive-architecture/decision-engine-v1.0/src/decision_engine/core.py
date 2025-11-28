"""
DECISION ENGINE v1.0 - Core Engine
===================================

The main Decision Engine class.

Codename: DECIDERE
Author: Sheldon K. Salmon
License: Apache 2.0
"""

import time
from typing import Optional, List, Dict, Any

from .config import DecisionConfig, AnalysisMode, DecisionContext
from .scoring import (
    BiasAssessment, SatisficingResult, OptionalityScore,
    TemporalAlignment, EthicalAssessment,
    ConfidenceLevel, TimelineVerdict, TemporalVerdict, EthicalVerdict,
    FragilityCategory
)
from .analysis import DecisionAnalysis, DecisionRecommendation
from .frameworks.kahneman import KahnemanFramework
from .frameworks.simon import SimonFramework
from .frameworks.taleb import TalebFramework
from .frameworks.bergson import BergsonFramework
from .frameworks.rawls_singer import RawlsSingerFramework


class DecisionEngine:
    """
    DECISION ENGINE v1.0 - DECIDERE
    
    Personal Decision Analysis Framework integrating 5 specialized frameworks.
    
    Frameworks:
    1. KAHNEMAN — Bias Detection (overconfidence, loss aversion, etc.)
    2. SIMON — Satisficing (define "good enough" to stop overthinking)
    3. TALEB — Antifragility & Optionality (reversibility, stress testing)
    4. BERGSON — Temporal Intelligence (is NOW the right time?)
    5. RAWLS/SINGER — Ethical Validation (fairness to all stakeholders)
    
    Modes:
    - QUICK: 5-10 min (Bias, Optionality, Ethics)
    - STANDARD: 15-20 min (Full 5-framework analysis)
    - DEEP: 30-45 min (+ Pre-mortem, Cultural Lens, Iteration)
    
    Usage:
        # Generate prompts for AI systems
        engine = DecisionEngine()
        prompt = engine.generate_system_prompt()
        
        # Analyze decision programmatically
        engine = DecisionEngine(config=DecisionConfig.standard())
        analysis = engine.analyze("Should I quit my job to start a business?")
    
    Author: Sheldon K. Salmon
    Codename: DECIDERE
    """
    
    VERSION = "1.0.0"
    CODENAME = "DECIDERE"
    
    def __init__(self, config: Optional[DecisionConfig] = None):
        """Initialize Decision Engine."""
        self.config = config or DecisionConfig.standard()
        self._analysis_history: List[DecisionAnalysis] = []
    
    def generate_system_prompt(self, compact: bool = False) -> str:
        """Generate Decision Engine prompt for AI systems."""
        if compact:
            return self._build_compact_prompt()
        
        if self.config.mode == AnalysisMode.QUICK:
            return self._build_quick_prompt()
        elif self.config.mode == AnalysisMode.DEEP:
            return self._build_deep_prompt()
        
        return self._build_standard_prompt()
    
    def _build_compact_prompt(self) -> str:
        """Build minimal compact prompt."""
        return """<DECISION_ENGINE v1.0 COMPACT>

5 FRAMEWORKS:
• Kahneman: Bias detection (anchoring, loss aversion, sunk cost, etc.)
• Simon: Satisficing (minimum/target/stretch outcomes, stop searching)
• Taleb: Antifragility (fragile/robust/antifragile, optionality, black swans)
• Bergson: Temporal (gestation/emergence/ripeness/decay/closure)
• Rawls/Singer: Ethics (stakeholders, veil of ignorance, net utility)

OUTPUT: Proceed/Wait/Decline + Confidence + IF-THEN Rule + Next Steps

</DECISION_ENGINE>"""
    
    def _build_quick_prompt(self) -> str:
        """Build quick mode prompt."""
        return """<DECISION_ENGINE v1.0 QUICK MODE>

Run 3 essential checks:

1. BIAS CHECK (Kahneman):
   - Primary bias detected: [name]
   - Debiasing: [one-line correction]

2. OPTIONALITY CHECK (Taleb):
   - Reversibility: HIGH | MEDIUM | LOW
   - If goes wrong, can you recover? [Yes/No + how]

3. ETHICS CHECK (Rawls/Singer):
   - Who benefits? Who loses?
   - Passes fairness test? [Yes/No]

OUTPUT:
Bias Detected: [bias] → Correction: [debiasing]
Reversibility: [HIGH/MEDIUM/LOW]
Ethics: [PASSES/FAILS]

RECOMMENDATION: [PROCEED | WAIT | DECLINE | NEED MORE INFO]
Confidence: [HIGH | MEDIUM | LOW]

</DECISION_ENGINE>"""
    
    def _build_standard_prompt(self) -> str:
        """Build standard mode prompt."""
        sections = [
            KahnemanFramework.get_prompt_section(),
            SimonFramework.get_prompt_section(),
            TalebFramework.get_prompt_section(),
            BergsonFramework.get_prompt_section(),
            RawlsSingerFramework.get_prompt_section()
        ]
        
        header = """<DECISION_ENGINE v1.0>

You are DECISION ENGINE v1.0 (DECIDERE), integrating 5 specialized frameworks:
1. KAHNEMAN — Bias Detection
2. SIMON — Satisficing
3. TALEB — Antifragility & Optionality
4. BERGSON — Temporal Intelligence
5. RAWLS/SINGER — Ethical Validation

STEP 1: DECISION FRAME CLARIFICATION
├─ State the SURFACE question (what user literally asked)
├─ Identify the UNDERLYING question (what's really being decided)
├─ Clarify decision variables (what exactly is being chosen)
└─ Define success criteria (how will we know it worked?)
"""
        
        synthesis = """
STEP 7: SYNTHESIS & RECOMMENDATION
├─ Count frameworks aligned (X/5)
├─ Identify contradictions (if any)
├─ Compute confidence: HIGH (4-5) | MEDIUM (2-3) | LOW (1) | VERY LOW (conflict)
├─ Generate IF-THEN decision rule
├─ Set timeline: IMMEDIATE | WAIT X DAYS | WAIT FOR TRIGGER
└─ List next steps (3 immediate actions)

OUTPUT FORMAT:
═══════════════════════════════════════════
DECISION ANALYSIS COMPLETE
═══════════════════════════════════════════

Decision Rule:
IF [condition 1]
AND [condition 2]
AND [condition 3]
THEN: [Action]
ELSE: [Alternative]

Timeline: [IMMEDIATE | WAIT X | WAIT FOR TRIGGER]
Confidence: [HIGH | MEDIUM | LOW]
Frameworks Aligned: [X/5]

Next Steps:
1. [Immediate action]
2. [Second priority]
3. [Third priority]

</DECISION_ENGINE>"""
        
        return header + "\n".join(sections) + synthesis
    
    def _build_deep_prompt(self) -> str:
        """Build deep mode prompt with Word Engine audit."""
        base = self._build_standard_prompt()
        
        deep_additions = """
STEP 0: WORD ENGINE QUERY AUDIT (DEEP MODE)
├─ Linguistic Lens: How is question phrased? (Binary? Passive? Absolute?)
├─ Cognitive Lens: What concept clusters activated? (identity, fear, status)
├─ Cultural Lens: Cultural valence of decision domain
├─ Contextual Lens: Recent life events influencing framing
├─ Directional Lens: Seeking permission? Validation? Genuinely uncertain?
├─ Emotional Lens: Fear, excitement, or resignation?
└─ Risk Lens: Hallucination triggers (absolutes, binaries)

REFRAME the question based on hidden assumptions detected.

ADDITIONAL DEEP MODE ELEMENTS:

Expected Value Calculation:
├─ Upside scenario: Probability × Payoff
├─ Base case: Probability × Payoff
├─ Downside scenario: Probability × Payoff
└─ Expected Value = Weighted sum

Iterative Refinement:
├─ What new information would change this analysis?
├─ Set triggers for re-evaluation
└─ Define decision review checkpoints
"""
        return deep_additions + base
    
    def _clarify_decision(self, decision: str) -> tuple:
        """Clarify surface and underlying questions."""
        surface = decision
        
        underlying = decision
        if "should I" in decision.lower():
            underlying = decision.replace("Should I", "What conditions would justify")
            underlying = underlying.replace("should I", "what conditions would justify")
        
        return surface, underlying
    
    def _derive_recommendation(
        self,
        bias: Optional[BiasAssessment],
        satisficing: Optional[SatisficingResult],
        optionality: Optional[OptionalityScore],
        temporal: Optional[TemporalAlignment],
        ethics: Optional[EthicalAssessment]
    ) -> DecisionRecommendation:
        """Derive recommendation from all framework analyses."""
        aligned = 0
        
        if bias and bias.bias_severity != "high":
            aligned += 1
        
        if satisficing and satisficing.reversibility_assessment != "low":
            aligned += 1
        
        if optionality and optionality.fragility != FragilityCategory.FRAGILE:
            aligned += 1
        
        if temporal and temporal.verdict == TemporalVerdict.ACT_NOW:
            aligned += 1
        
        if ethics and ethics.verdict != EthicalVerdict.UNJUST:
            aligned += 1
        
        if aligned >= 4:
            confidence = ConfidenceLevel.HIGH
        elif aligned >= 2:
            confidence = ConfidenceLevel.MEDIUM
        elif aligned >= 1:
            confidence = ConfidenceLevel.LOW
        else:
            confidence = ConfidenceLevel.VERY_LOW
        
        proceed = aligned >= 3
        
        if temporal:
            if temporal.verdict == TemporalVerdict.ACT_NOW:
                timeline = TimelineVerdict.IMMEDIATE
            elif temporal.verdict == TemporalVerdict.WAIT:
                timeline = TimelineVerdict.WAIT_DAYS
            elif temporal.verdict == TemporalVerdict.PREPARE:
                timeline = TimelineVerdict.WAIT_FOR_TRIGGER
            else:
                timeline = TimelineVerdict.DECLINE
        else:
            timeline = TimelineVerdict.WAIT_FOR_TRIGGER
        
        conditions = []
        if bias and bias.detected_biases:
            conditions.append(f"Debiasing strategies applied for {bias.detected_biases[0].value}")
        if optionality:
            conditions.append(f"Reversibility is {optionality.reversibility}")
        if ethics and ethics.veil_of_ignorance_passes:
            conditions.append("Ethical concerns addressed")
        
        if not conditions:
            conditions = ["Basic due diligence completed"]
        
        then_action = "Proceed with decision" if proceed else "Delay and gather more information"
        else_action = "Wait for conditions to improve" if proceed else "Consider alternative approach"
        
        next_steps = []
        if bias and bias.debiasing_strategies:
            next_steps.append(f"Apply: {bias.debiasing_strategies[0].strategy}")
        if optionality and optionality.via_negativa:
            next_steps.append(f"Remove risk: {optionality.via_negativa[0]}")
        if ethics and ethics.redesign_suggestions:
            next_steps.append(f"Address: {ethics.redesign_suggestions[0]}")
        
        if not next_steps:
            next_steps = ["Document decision rationale", "Set review checkpoint", "Communicate to stakeholders"]
        
        return DecisionRecommendation(
            proceed=proceed,
            confidence=confidence,
            frameworks_aligned=aligned,
            timeline=timeline,
            if_conditions=conditions,
            then_action=then_action,
            else_action=else_action,
            next_steps=next_steps[:3]
        )
    
    def analyze(
        self,
        decision: str,
        stakeholders: Optional[List[str]] = None,
        minimum_outcome: Optional[str] = None,
        target_outcome: Optional[str] = None,
        stretch_outcome: Optional[str] = None
    ) -> DecisionAnalysis:
        """
        Perform complete decision analysis using the 5-framework protocol.
        
        Args:
            decision: The decision statement to analyze
            stakeholders: Optional list of explicit stakeholders
            minimum_outcome: Optional minimum acceptable outcome
            target_outcome: Optional target outcome
            stretch_outcome: Optional stretch outcome
            
        Returns:
            Complete DecisionAnalysis with recommendation
        """
        start_time = time.time()
        
        surface, underlying = self._clarify_decision(decision)
        
        bias = None
        if self.config.enable_bias_detection:
            bias = KahnemanFramework.analyze(
                decision,
                include_premortem=self.config.include_premortem
            )
        
        satisficing = None
        if self.config.enable_satisficing:
            satisficing = SimonFramework.analyze(
                decision,
                minimum=minimum_outcome,
                target=target_outcome,
                stretch=stretch_outcome
            )
        
        optionality = None
        if self.config.enable_antifragility:
            optionality = TalebFramework.analyze(decision)
        
        temporal = None
        if self.config.enable_temporal:
            temporal = BergsonFramework.analyze(decision)
        
        ethics = None
        if self.config.enable_ethics:
            ethics = RawlsSingerFramework.analyze(decision, stakeholders)
        
        recommendation = self._derive_recommendation(
            bias, satisficing, optionality, temporal, ethics
        )
        
        warnings = []
        insights = []
        
        if bias and bias.bias_severity == "high":
            warnings.append("High bias severity detected - review debiasing strategies carefully")
        
        if optionality and optionality.fragility == FragilityCategory.FRAGILE:
            warnings.append("Decision is FRAGILE - consider building in more optionality")
        
        if temporal and temporal.verdict == TemporalVerdict.ABANDON:
            warnings.append("Timing suggests window has closed - consider alternatives")
        
        if ethics and ethics.verdict == EthicalVerdict.UNJUST:
            warnings.append("Ethical concerns identified - redesign recommended")
        
        if bias and not bias.detected_biases:
            insights.append("No major biases detected in decision framing")
        
        if optionality and optionality.fragility == FragilityCategory.ANTIFRAGILE:
            insights.append("Decision has antifragile properties - may strengthen under stress")
        
        processing_time = (time.time() - start_time) * 1000
        
        analysis = DecisionAnalysis(
            decision_statement=decision,
            surface_question=surface,
            underlying_question=underlying,
            bias_assessment=bias,
            satisficing_result=satisficing,
            optionality_score=optionality,
            temporal_alignment=temporal,
            ethical_assessment=ethics,
            recommendation=recommendation,
            warnings=warnings,
            insights=insights,
            processing_time_ms=processing_time
        )
        
        self._analysis_history.append(analysis)
        
        return analysis
    
    def quick_check(self, decision: str) -> DecisionAnalysis:
        """Perform quick 3-check analysis (Bias, Optionality, Ethics)."""
        original_config = self.config
        self.config = DecisionConfig.quick()
        
        result = self.analyze(decision)
        
        self.config = original_config
        return result
    
    def get_analysis_history(self) -> List[DecisionAnalysis]:
        """Get history of analyses performed."""
        return self._analysis_history.copy()
    
    def __repr__(self) -> str:
        return f"DecisionEngine(mode={self.config.mode.value}, v{self.VERSION})"
