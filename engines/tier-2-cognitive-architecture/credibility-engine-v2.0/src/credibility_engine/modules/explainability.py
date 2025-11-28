"""
CREDIBILITY ENGINE v2.0 - Module 3: Score Explainability
=========================================================

Rationale generation and attribution analysis.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from ..scoring import CredibilityScore, CompositeScore, CredibilityHealth


@dataclass
class ScoreExplanation:
    """Explanation for a credibility score."""
    headline: str
    factors: List[str]
    primary_driver: str
    recommendations: List[str]


@dataclass
class AttributionAnalysis:
    """Analysis of score attribution."""
    component: str
    contribution: float
    impact_direction: str
    root_causes: List[str]


class ExplainabilityEngine:
    """
    Module 3: Score Explainability Engine
    
    Provides:
    - Rationale generation for score changes
    - Shapley-style contribution analysis
    - Root cause identification
    """
    
    EXPLANATIONS = {
        "proof_freshness_low": {
            "headline": "Proof assets are aging",
            "causes": [
                "Major demo is over 90 days old",
                "No new case studies in 90+ days",
                "Latest testimonial is stale"
            ],
            "recommendations": [
                "Schedule 48-hour demo refresh sprint",
                "Reach out to recent customers for testimonials",
                "Update case study with current metrics"
            ]
        },
        "social_momentum_low": {
            "headline": "Social proof velocity declining",
            "causes": [
                "Mention velocity dropped significantly",
                "Competitor launched similar content",
                "Amplification rate below threshold"
            ],
            "recommendations": [
                "Execute testimonial solicitation sequence",
                "Launch mini case study campaign",
                "Schedule amplifier engagement outreach"
            ]
        },
        "relevance_declining": {
            "headline": "Market relevance is decreasing",
            "causes": [
                "Market focus shifted to new technologies",
                "Search volume for your domain decreased",
                "Competitor messaging evolved faster"
            ],
            "recommendations": [
                "Update positioning to reflect market trends",
                "Publish thought leadership on emerging topics",
                "Refresh SEO and content strategy"
            ]
        }
    }
    
    @classmethod
    def explain_score(
        cls,
        score: CredibilityScore,
        composite: Optional[CompositeScore] = None
    ) -> ScoreExplanation:
        """Generate explanation for a credibility score."""
        factors = []
        recommendations = []
        primary_driver = "General decay over time"
        
        if score.health == CredibilityHealth.HEALTHY:
            headline = "Credibility is strong and healthy"
            factors.append(f"Score of {score.current_score:.1f} is above healthy threshold")
            recommendations.append("Continue maintenance mode")
        
        elif score.health == CredibilityHealth.ATTENTION:
            headline = "Credibility needs attention soon"
            factors.append(f"Score of {score.current_score:.1f} is declining")
            factors.append(f"{score.days_since_refresh:.0f} days since last refresh")
            recommendations.append("Schedule refresh within 30 days")
        
        elif score.health in [CredibilityHealth.WARNING, CredibilityHealth.CRITICAL]:
            headline = "Immediate action required"
            factors.append(f"Score critically low at {score.current_score:.1f}")
            factors.append(f"Decayed {score.decay_percentage:.1f}% from initial")
            recommendations.append("Execute emergency refresh protocol")
            recommendations.append("Reach out for fresh testimonials")
        
        else:
            headline = "Asset requires complete rebuild"
            factors.append("Score has expired below usable threshold")
            recommendations.append("Create entirely new proof asset")
        
        if composite:
            components = [
                ("Proof Freshness", composite.proof_freshness),
                ("Social Momentum", composite.social_momentum),
                ("Relevance", composite.relevance_index),
                ("Endorsement", composite.endorsement_quality),
                ("Trust (inv. fraud)", composite.fraud_score)
            ]
            sorted_components = sorted(components, key=lambda x: x[1])
            weakest = sorted_components[0]
            primary_driver = f"{weakest[0]} is the weakest factor at {weakest[1]:.1f}"
            factors.append(f"Lowest component: {weakest[0]} ({weakest[1]:.1f})")
        
        return ScoreExplanation(
            headline=headline,
            factors=factors,
            primary_driver=primary_driver,
            recommendations=recommendations[:3]
        )
    
    @classmethod
    def attribution_breakdown(
        cls,
        composite: CompositeScore
    ) -> List[AttributionAnalysis]:
        """Generate Shapley-style attribution analysis."""
        attributions = []
        
        components = [
            ("Proof Freshness", composite.proof_freshness, composite.weights.get("proof_freshness", 0.3)),
            ("Social Momentum", composite.social_momentum, composite.weights.get("social_momentum", 0.25)),
            ("Relevance Index", composite.relevance_index, composite.weights.get("relevance_index", 0.2)),
            ("Endorsement Quality", composite.endorsement_quality, composite.weights.get("endorsement_quality", 0.15)),
            ("Fraud Score", composite.fraud_score, composite.weights.get("fraud_score", 0.1))
        ]
        
        for name, value, weight in components:
            contribution = value * weight
            
            if value >= 70:
                direction = "positive"
                causes = ["Component is healthy", "No immediate action needed"]
            elif value >= 40:
                direction = "neutral"
                causes = ["Component needs attention", "Schedule refresh soon"]
            else:
                direction = "negative"
                causes = ["Component is dragging score down", "Immediate intervention needed"]
            
            attributions.append(AttributionAnalysis(
                component=name,
                contribution=contribution,
                impact_direction=direction,
                root_causes=causes
            ))
        
        return sorted(attributions, key=lambda a: a.contribution, reverse=True)
