"""
STRATEGY ENGINE v1.1 - Core Engine
===================================

The main Strategy Engine class.

Codename: The Strategist's Edge
Author: Sheldon K. Salmon
License: Apache 2.0
"""

import time
from dataclasses import dataclass
from typing import Optional, List, Dict, Any, Tuple

from .config import (
    StrategyConfig, AnalysisMode, OrganizationContext,
    StrategicPosition
)
from .scoring import (
    MoatDurabilityIndex, MoatStrength, CompetitorProfile,
    ResponseProbability, PayoffMatrix, EthicsAssessment, EthicsFlag
)
from .analysis import (
    StrategicAnalysis, CompetitiveResponse, StrategicSynthesis
)
from .prompts import PromptBuilder
from .frameworks.sun_tzu import SunTzuFramework, TerrainAnalysis
from .frameworks.meadows import MeadowsFramework, LeverageAnalysis
from .frameworks.barabasi import BarabasiFramework, NetworkDynamics
from .frameworks.pearl import PearlFramework, CausalModel
from .frameworks.ostrom import OstromFramework, ResourceGovernance


class StrategyEngine:
    """
    STRATEGY ENGINE v1.1 - The Strategist's Edge
    
    A 5-framework strategic analysis system for competitive strategy,
    market positioning, and sustainable advantage creation.
    
    Features:
    - 5 integrated strategic frameworks (Sun Tzu, Meadows, Barabási, Pearl, Ostrom)
    - 6-step strategic analysis protocol
    - Competitive Response Simulator with game theory
    - Moat Durability Index for advantage longevity
    - Ethical guardrails (GREEN/YELLOW/RED flags)
    
    Usage:
        # Generate prompts for AI systems
        engine = StrategyEngine()
        prompt = engine.generate_system_prompt()
        
        # Analyze strategy programmatically
        engine = StrategyEngine(config=StrategyConfig.full())
        analysis = engine.analyze(
            organization="Acme Corp",
            industry="SaaS",
            strategic_question="How do we compete against incumbents?"
        )
    
    Author: Sheldon K. Salmon
    Codename: The Strategist's Edge
    """
    
    VERSION = "1.1.0"
    CODENAME = "The Strategist's Edge"
    
    RESPONSE_PROBABILITIES = {
        ("aggressive", "abundant"): [
            ("price_war", 65, "Differentiate on value, avoid head-on price competition"),
            ("feature_copy", 25, "Accelerate innovation, maintain lead"),
            ("acquisition_attempt", 10, "Strengthen IP, consider poison pill defenses")
        ],
        ("aggressive", "adequate"): [
            ("targeted_attack", 50, "Shore up defenses in key segments"),
            ("price_war", 30, "Maintain margins, emphasize quality"),
            ("partnership", 20, "Consider counter-partnerships")
        ],
        ("aggressive", "constrained"): [
            ("guerrilla_tactics", 55, "Ignore distractions, focus on core growth"),
            ("bluster", 30, "Call their bluff, continue execution"),
            ("niche_retreat", 15, "Pursue their abandoned segments")
        ],
        ("defensive", "abundant"): [
            ("wait_and_see", 50, "Press advantage while they hesitate"),
            ("incremental_response", 30, "Accelerate before they fully respond"),
            ("acquisition_defense", 20, "Build scale quickly")
        ],
        ("defensive", "adequate"): [
            ("wait_and_see", 60, "Capture market share rapidly"),
            ("slow_follow", 25, "Maintain innovation lead"),
            ("ignore", 15, "Maximum aggression window")
        ],
        ("defensive", "constrained"): [
            ("retreat", 45, "Pursue their abandoned territory"),
            ("ignore", 35, "Rapid expansion opportunity"),
            ("desperation_move", 20, "Prepare for unpredictable response")
        ],
        ("opportunistic", "abundant"): [
            ("fast_follow", 45, "Stay ahead with continuous innovation"),
            ("partnership_offer", 30, "Evaluate carefully for strategic fit"),
            ("undercutting", 25, "Strengthen customer lock-in")
        ],
        ("opportunistic", "adequate"): [
            ("selective_copy", 50, "Focus on hard-to-copy advantages"),
            ("niche_attack", 30, "Defend core, cede periphery if needed"),
            ("wait_for_weakness", 20, "Maintain strong position")
        ],
        ("opportunistic", "constrained"): [
            ("cherry_picking", 40, "Protect high-value segments"),
            ("partnership_seek", 35, "Consider co-opetition"),
            ("wait", 25, "Continue building moat")
        ],
        ("inert", "abundant"): [
            ("ignore", 70, "Maximum opportunity - move fast"),
            ("delayed_awakening", 20, "Build position before they react"),
            ("eventual_response", 10, "Prepare for future competition")
        ],
        ("inert", "adequate"): [
            ("ignore", 75, "Aggressive expansion opportunity"),
            ("slow_response", 15, "Lock in customers quickly"),
            ("eventual_copy", 10, "Innovate continuously")
        ],
        ("inert", "constrained"): [
            ("ignore", 80, "Excellent window - capture market"),
            ("decline", 15, "Consider acquisition of assets"),
            ("exit", 5, "Prepare for their exit")
        ]
    }
    
    def __init__(
        self,
        config: Optional[StrategyConfig] = None
    ):
        """
        Initialize Strategy Engine.
        
        Args:
            config: Engine configuration (defaults to full mode)
        """
        self.config = config or StrategyConfig.full()
        self._analysis_history: List[StrategicAnalysis] = []
    
    def generate_system_prompt(self, compact: bool = False) -> str:
        """
        Generate Strategy Engine prompt for AI systems.
        
        Args:
            compact: If True, generate minimal prompt
            
        Returns:
            Formatted prompt string
        """
        if compact:
            return PromptBuilder.build_compact_prompt()
        
        if self.config.mode == AnalysisMode.QUICK:
            return PromptBuilder.build_quick_prompt()
        elif self.config.mode == AnalysisMode.MOAT:
            return PromptBuilder.build_moat_prompt()
        elif self.config.mode == AnalysisMode.RESPONSE:
            return PromptBuilder.build_response_prompt()
        
        return PromptBuilder.build_full_prompt(self.config)
    
    def calculate_moat(
        self,
        imitation: float = 5.0,
        switching: float = 5.0,
        network: float = 5.0,
        scale: float = 5.0,
        brand: float = 5.0,
        regulatory: float = 5.0
    ) -> MoatDurabilityIndex:
        """
        Calculate Moat Durability Index.
        
        Args:
            imitation: Imitation difficulty score (0-10)
            switching: Switching costs score (0-10)
            network: Network effects score (0-10)
            scale: Scale advantages score (0-10)
            brand: Brand/trust capital score (0-10)
            regulatory: Regulatory moat score (0-10)
            
        Returns:
            MoatDurabilityIndex object
        """
        return MoatDurabilityIndex(
            imitation_difficulty=imitation,
            switching_costs=switching,
            network_effects=network,
            scale_advantages=scale,
            brand_trust=brand,
            regulatory_moat=regulatory
        )
    
    def _compute_payoff_matrix(
        self,
        your_move: str,
        competitors: List[CompetitorProfile]
    ) -> PayoffMatrix:
        """
        Compute payoff matrix based on move and competitor profiles.
        
        Game theory logic:
        - Aggressive vs Aggressive: mutual destruction (-2, -2)
        - Aggressive vs Passive: aggressor gains (+3, -1) 
        - Passive vs Aggressive: defender loses (-1, +3)
        - Passive vs Passive: stable growth (+1, +1)
        
        Adjustments based on:
        - Resource asymmetry
        - Move aggressiveness
        """
        base_aa = (-2, -2)
        base_ap = (3, -1)
        base_pa = (-1, 3)
        base_pp = (1, 1)
        
        aggressive_keywords = ["aggressive", "attack", "undercut", "war", "disrupt", "steal"]
        move_is_aggressive = any(kw in your_move.lower() for kw in aggressive_keywords)
        
        avg_resource_level = 0
        for comp in competitors:
            if comp.resources == "abundant":
                avg_resource_level += 3
            elif comp.resources == "adequate":
                avg_resource_level += 2
            else:
                avg_resource_level += 1
        
        if competitors:
            avg_resource_level /= len(competitors)
        else:
            avg_resource_level = 2
        
        resource_modifier = int(2 - avg_resource_level)
        
        if move_is_aggressive:
            aa = (base_aa[0] - 1, base_aa[1] - 1)
            ap = (base_ap[0] + 1, base_ap[1])
            pa = (base_pa[0], base_pa[1] + 1)
            pp = base_pp
        else:
            aa = base_aa
            ap = (base_ap[0] + resource_modifier, base_ap[1])
            pa = base_pa
            pp = (base_pp[0] + 1, base_pp[1] + 1)
        
        return PayoffMatrix(
            aggressive_aggressive=aa,
            aggressive_passive=ap,
            passive_aggressive=pa,
            passive_passive=pp
        )
    
    def simulate_response(
        self,
        your_move: str,
        competitors: List[CompetitorProfile],
        responses: Optional[List[ResponseProbability]] = None
    ) -> CompetitiveResponse:
        """
        Simulate competitive responses to a strategic move using game theory.
        
        Args:
            your_move: Description of your planned move
            competitors: List of competitor profiles
            responses: Optional list of response probabilities (auto-generated if None)
            
        Returns:
            CompetitiveResponse analysis with payoff matrix and Nash equilibrium
        """
        if responses is None:
            responses = []
            for comp in competitors:
                key = (comp.posture, comp.resources)
                if key in self.RESPONSE_PROBABILITIES:
                    resp_options = self.RESPONSE_PROBABILITIES[key]
                else:
                    key = ("defensive", "adequate")
                    resp_options = self.RESPONSE_PROBABILITIES[key]
                
                for resp_type, prob, counter in resp_options:
                    responses.append(ResponseProbability(
                        competitor=comp.name,
                        response_type=resp_type,
                        probability=prob,
                        your_counter=counter
                    ))
        
        payoff = self._compute_payoff_matrix(your_move, competitors)
        nash = payoff.find_nash_equilibrium()
        optimal = payoff.recommend_strategy()
        
        second_order = []
        
        aggressive_count = sum(1 for c in competitors if c.posture == "aggressive")
        defensive_count = sum(1 for c in competitors if c.posture in ("defensive", "inert"))
        
        if aggressive_count > len(competitors) / 2:
            second_order.append("High competitive intensity - expect price pressure and rapid counter-moves")
            second_order.append("Market may consolidate as weaker players exit")
        elif defensive_count > len(competitors) / 2:
            second_order.append("Favorable competitive window - low resistance to market share gains")
            second_order.append("Incumbent awakening possible after you prove the opportunity")
        
        abundant_count = sum(1 for c in competitors if c.resources == "abundant")
        if abundant_count > 0:
            second_order.append(f"{abundant_count} well-resourced competitor(s) may escalate if threatened")
        
        constrained_count = sum(1 for c in competitors if c.resources == "constrained")
        if constrained_count > 0:
            second_order.append(f"{constrained_count} resource-constrained competitor(s) may exit or seek acquisition")
        
        if not second_order:
            second_order.append("Balanced competitive environment - steady execution recommended")
        
        commitment = []
        
        if "aggressive" in optimal.lower():
            commitment.extend([
                "Public announcement to signal commitment and deter half-measures",
                "Sunk cost investment in capability to make reversal costly",
                "Customer contracts with volume commitments"
            ])
        else:
            commitment.extend([
                "Maintain strategic flexibility for opportunistic moves",
                "Build optionality through modular investments",
                "Monitor competitor moves for response triggers"
            ])
        
        return CompetitiveResponse(
            your_move=your_move,
            competitor_profiles=competitors,
            response_matrix=responses,
            second_order_effects=second_order,
            payoff_matrix=payoff,
            nash_equilibrium=nash,
            optimal_strategy=optimal,
            commitment_devices=commitment
        )
    
    def check_ethics(self, strategy_elements: List[str]) -> EthicsAssessment:
        """Check strategy against ethical guardrails."""
        return EthicsAssessment.assess(strategy_elements)
    
    def _derive_phase_actions(
        self,
        terrain: TerrainAnalysis,
        leverage: LeverageAnalysis,
        network: NetworkDynamics,
        causal: CausalModel,
        governance: ResourceGovernance,
        moat: Optional[MoatDurabilityIndex],
        strategic_question: str
    ) -> Tuple[List[str], List[str], List[str], List[str]]:
        """
        Derive phased implementation roadmap from analysis results.
        
        Phase 1 (0-90 days): Quick wins, momentum
        Phase 2 (90-180 days): Core execution
        Phase 3 (180-365 days): Moat deepening
        Phase 4 (1-3 years): Ecosystem dominance
        """
        phase_1 = []
        phase_2 = []
        phase_3 = []
        phase_4 = []
        
        if terrain.terrain_type == "pure_blue":
            phase_1.append("Establish category definition and thought leadership")
            phase_2.append("Build first-mover advantages before competition arrives")
        elif terrain.terrain_type == "pure_red":
            phase_1.append("Identify differentiation wedge to avoid commoditization")
            phase_2.append("Focus on underserved segment to build beachhead")
        else:
            phase_1.append("Map competitive gaps and quick win opportunities")
            phase_2.append("Execute on highest-impact differentiators")
        
        if leverage.highest_leverage_points:
            top_leverage = leverage.highest_leverage_points[0]
            phase_1.append(f"Target {top_leverage.name} for maximum impact")
        
        if network.tipping_point and network.tipping_point.distance_to_tipping < 15:
            phase_2.append("Accelerate to tipping point with focused acquisition")
        
        if network.key_hubs:
            phase_1.append(f"Win key hub(s): {', '.join(network.key_hubs[:2])}")
        
        if network.preferential_attachment:
            phase_3.append("Amplify network effects through user-generated growth")
        
        for assumption in causal.what_must_be_true[:2]:
            phase_1.append(f"Validate assumption: {assumption[:50]}...")
        
        if moat:
            weakest = moat.get_weakest_dimensions(2)
            for dim, score in weakest:
                if score < 4:
                    phase_3.append(f"Strengthen {dim} (currently {score}/10)")
            
            if moat.strength in (MoatStrength.WEAK, MoatStrength.NONE):
                phase_2.append("Prioritize moat building before expansion")
        
        if governance.ecosystem_health.value in ("stressed", "declining"):
            phase_3.append("Address ecosystem health to ensure sustainability")
        
        phase_4.extend([
            "Expand to adjacent markets leveraging core advantages",
            "Build ecosystem lock-in and platform dynamics",
            "Establish industry standard position"
        ])
        
        return (
            phase_1[:3] if phase_1 else ["Identify and execute quick wins"],
            phase_2[:3] if phase_2 else ["Core strategy execution"],
            phase_3[:3] if phase_3 else ["Deepen moat and sustainability"],
            phase_4[:3]
        )
    
    def analyze(
        self,
        organization: str,
        industry: str,
        strategic_question: str,
        competitors: Optional[List[str]] = None,
        current_advantages: Optional[List[str]] = None,
        planned_move: Optional[str] = None,
        moat_scores: Optional[Dict[str, float]] = None
    ) -> StrategicAnalysis:
        """
        Perform complete strategic analysis using the 6-step protocol.
        
        This method executes all 5 frameworks in sequence:
        1. Sun Tzu (Terrain Analysis)
        2. Meadows (Leverage Points)
        3. Barabási (Network Dynamics)
        4. Pearl (Causal Model)
        5. Ostrom (Resource Governance)
        6. Synthesis (Integration)
        
        Args:
            organization: Organization name
            industry: Industry/market
            strategic_question: The strategic question to answer
            competitors: List of competitor names
            current_advantages: Current competitive advantages
            planned_move: Planned strategic move (for response simulation)
            moat_scores: Optional manual moat dimension scores
            
        Returns:
            Complete StrategicAnalysis with integrated results
        """
        start_time = time.time()
        
        if competitors is None:
            competitors = []
        if current_advantages is None:
            current_advantages = []
        
        terrain = SunTzuFramework.analyze_terrain(
            industry=industry,
            competitors=competitors
        )
        terrain.position_advantages = current_advantages
        
        leverage = MeadowsFramework.identify_leverage_points(
            system_description=f"{organization} in {industry}: {strategic_question}",
            focus_areas=current_advantages
        )
        
        network = BarabasiFramework.analyze_network(
            market_description=f"{industry} market",
            current_adoption=5.0 if not current_advantages else 10.0,
            key_players=competitors[:5]
        )
        
        causal = PearlFramework.build_causal_model(
            strategy_description=strategic_question,
            key_variables=["market_position", "differentiation", "growth", "profitability"],
            assumptions=[f"Advantage: {adv}" for adv in current_advantages[:3]]
        )
        
        governance = OstromFramework.assess_governance(
            organization_description=f"{organization} competing in {industry}",
            current_advantages=current_advantages
        )
        
        moat = None
        if self.config.enable_moat_assessment:
            if moat_scores:
                moat = self.calculate_moat(**moat_scores)
            else:
                base_scores = {
                    "imitation": 5.0,
                    "switching": 4.0,
                    "network": 3.0,
                    "scale": 4.0,
                    "brand": 3.0,
                    "regulatory": 2.0
                }
                
                if current_advantages:
                    advantage_text = " ".join(current_advantages).lower()
                    if "patent" in advantage_text or "proprietary" in advantage_text:
                        base_scores["imitation"] += 2
                    if "network" in advantage_text or "platform" in advantage_text:
                        base_scores["network"] += 2
                    if "brand" in advantage_text or "trust" in advantage_text:
                        base_scores["brand"] += 2
                    if "scale" in advantage_text or "cost" in advantage_text:
                        base_scores["scale"] += 2
                    if "integrat" in advantage_text or "lock" in advantage_text:
                        base_scores["switching"] += 2
                
                for key in base_scores:
                    base_scores[key] = min(10.0, max(0.0, base_scores[key]))
                
                moat = self.calculate_moat(**base_scores)
        
        response = None
        if self.config.enable_response_simulator and planned_move and competitors:
            comp_profiles = []
            for i, c in enumerate(competitors[:3]):
                postures = ["aggressive", "defensive", "opportunistic", "inert"]
                resources = ["abundant", "adequate", "constrained"]
                comp_profiles.append(CompetitorProfile(
                    name=c,
                    posture=postures[i % len(postures)],
                    resources=resources[i % len(resources)]
                ))
            response = self.simulate_response(planned_move, comp_profiles)
        
        ethics = None
        if self.config.enable_ethics_check:
            elements_to_check = [strategic_question] + current_advantages
            if planned_move:
                elements_to_check.append(planned_move)
            ethics = self.check_ethics(elements_to_check)
        
        if terrain.terrain_type == "pure_blue":
            position = StrategicPosition.BLUE_OCEAN
        elif terrain.terrain_type == "pure_red":
            position = StrategicPosition.RED_OCEAN
        else:
            position = StrategicPosition.HYBRID
        
        interventions = []
        for lp in leverage.highest_leverage_points[:3]:
            interventions.append(f"L{lp.level}: {lp.name} - {lp.description}")
        if not interventions:
            interventions = ["Focus on highest-leverage system changes"]
        
        phase_1, phase_2, phase_3, phase_4 = self._derive_phase_actions(
            terrain, leverage, network, causal, governance, moat, strategic_question
        )
        
        synthesis = StrategicSynthesis(
            strategic_position=position,
            highest_leverage_interventions=interventions,
            network_strategy=network.hub_strategy,
            causal_assumptions=causal.what_must_be_true,
            sustainability_score=governance.sustainability_score,
            ethics_flag=ethics.flag if ethics else EthicsFlag.GREEN,
            phase_1_actions=phase_1,
            phase_2_actions=phase_2,
            phase_3_actions=phase_3,
            phase_4_actions=phase_4
        )
        
        recommendations = []
        
        if moat and moat.strength in (MoatStrength.WEAK, MoatStrength.NONE):
            weak_dims = moat.get_weakest_dimensions(2)
            recommendations.append(
                f"URGENT: Strengthen {weak_dims[0][0]} (current: {weak_dims[0][1]}/10) - moat is {moat.strength.value}"
            )
        
        for intervention in interventions[:2]:
            recommendations.append(f"HIGH LEVERAGE: {intervention}")
        
        if network.tipping_point and network.tipping_point.distance_to_tipping < 10:
            recommendations.append(
                f"OPPORTUNITY: Only {network.tipping_point.distance_to_tipping:.0f}% from tipping point"
            )
        
        if governance.moat_erosion_risks:
            recommendations.append(f"RISK MONITOR: {governance.moat_erosion_risks[0]}")
        
        if response and "aggressive" in response.optimal_strategy.lower():
            recommendations.append("COMPETITIVE: Aggressive posture recommended - competitors vulnerable")
        elif response:
            recommendations.append("COMPETITIVE: Measured approach recommended - maintain flexibility")
        
        processing_time = (time.time() - start_time) * 1000
        
        warnings = []
        if ethics and ethics.flag != EthicsFlag.GREEN:
            warnings.append(f"Ethics flag: {ethics.flag.value} - {ethics.concerns}")
        if moat and moat.strength == MoatStrength.NONE:
            warnings.append("No competitive moat detected - prioritize moat building")
        if governance.ecosystem_health.value == "declining":
            warnings.append("Ecosystem health declining - sustainability at risk")
        
        analysis = StrategicAnalysis(
            organization=organization,
            industry=industry,
            strategic_question=strategic_question,
            terrain_analysis=terrain.to_dict(),
            leverage_analysis=leverage.to_dict(),
            network_analysis=network.to_dict(),
            causal_model=causal.to_dict(),
            governance_analysis=governance.to_dict(),
            competitive_response=response,
            moat_durability=moat,
            synthesis=synthesis,
            ethics_assessment=ethics,
            warnings=warnings,
            recommendations=recommendations,
            processing_time_ms=processing_time
        )
        
        self._analysis_history.append(analysis)
        
        return analysis
    
    def get_analysis_history(self) -> List[StrategicAnalysis]:
        """Get history of analyses performed."""
        return self._analysis_history.copy()
    
    def __repr__(self) -> str:
        return f"StrategyEngine(mode={self.config.mode.value}, v{self.VERSION})"
