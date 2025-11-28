"""
EXPLANATION ENGINE v1.0 - Multi-Level Generator
=================================================

Generates explanations at multiple levels of abstraction.
"""

from typing import List, Dict, Any, Optional
from ..types import (
    ExplanationLayer, LayerType, AudienceProfile
)
from ..config import ExplanationDepth


class MultiLevelGenerator:
    """
    Multi-Level Explanation Generator
    
    Creates explanations with progressive depth:
    1. Headline - One-sentence summary
    2. Summary - Key points overview
    3. Key Factors - Main drivers and influences
    4. Evidence - Supporting data and sources
    5. Methodology - How conclusions were reached
    6. Limitations - Caveats and uncertainties
    """
    
    LAYER_TEMPLATES = {
        LayerType.HEADLINE: "Single-sentence summary of the main finding or recommendation",
        LayerType.SUMMARY: "2-3 paragraph overview of the analysis and conclusions",
        LayerType.KEY_FACTORS: "Bulleted list of main factors influencing the outcome",
        LayerType.EVIDENCE: "Supporting data, statistics, and sources",
        LayerType.METHODOLOGY: "How the analysis was conducted",
        LayerType.LIMITATIONS: "Known limitations, caveats, and uncertainties",
        LayerType.RECOMMENDATIONS: "Actionable next steps based on the analysis"
    }
    
    DEPTH_LAYERS = {
        ExplanationDepth.SUMMARY: [LayerType.HEADLINE, LayerType.SUMMARY],
        ExplanationDepth.STANDARD: [
            LayerType.HEADLINE, LayerType.SUMMARY,
            LayerType.KEY_FACTORS, LayerType.RECOMMENDATIONS
        ],
        ExplanationDepth.DETAILED: [
            LayerType.HEADLINE, LayerType.SUMMARY,
            LayerType.KEY_FACTORS, LayerType.EVIDENCE,
            LayerType.LIMITATIONS, LayerType.RECOMMENDATIONS
        ],
        ExplanationDepth.COMPREHENSIVE: [
            LayerType.HEADLINE, LayerType.SUMMARY,
            LayerType.KEY_FACTORS, LayerType.EVIDENCE,
            LayerType.METHODOLOGY, LayerType.LIMITATIONS,
            LayerType.RECOMMENDATIONS
        ]
    }
    
    @classmethod
    def get_layers_for_depth(cls, depth: ExplanationDepth) -> List[LayerType]:
        """Get appropriate layer types for depth level."""
        return cls.DEPTH_LAYERS.get(depth, cls.DEPTH_LAYERS[ExplanationDepth.STANDARD])
    
    @classmethod
    def generate_headline(
        cls,
        topic: str,
        conclusion: str,
        confidence: float = 0.8
    ) -> ExplanationLayer:
        """Generate headline layer."""
        content = f"{topic}: {conclusion}"
        
        if confidence < 0.5:
            content += " (with significant uncertainty)"
        elif confidence < 0.7:
            content += " (with moderate confidence)"
        
        return ExplanationLayer(
            layer_type=LayerType.HEADLINE,
            content=content,
            confidence=confidence
        )
    
    @classmethod
    def generate_summary(
        cls,
        findings: List[str],
        conclusion: str,
        audience: AudienceProfile
    ) -> ExplanationLayer:
        """Generate summary layer."""
        if audience.level == "executive":
            content = f"Bottom Line: {conclusion}\n\n"
            content += "Key Points:\n"
            for i, finding in enumerate(findings[:3], 1):
                content += f"• {finding}\n"
        else:
            content = "Analysis Overview:\n\n"
            for finding in findings:
                content += f"• {finding}\n"
            content += f"\nConclusion: {conclusion}"
        
        return ExplanationLayer(
            layer_type=LayerType.SUMMARY,
            content=content,
            confidence=0.9
        )
    
    @classmethod
    def generate_key_factors(
        cls,
        factors: List[Dict[str, Any]],
        audience: AudienceProfile
    ) -> ExplanationLayer:
        """Generate key factors layer."""
        content = "Key Factors Influencing This Outcome:\n\n"
        
        for factor in factors[:5]:
            name = factor.get("name", "Unknown factor")
            impact = factor.get("impact", "moderate")
            direction = factor.get("direction", "positive")
            
            symbol = "↑" if direction == "positive" else "↓"
            content += f"• {name} [{symbol} {impact} impact]\n"
            
            if audience.level == "technical" and "details" in factor:
                content += f"  └─ {factor['details']}\n"
        
        return ExplanationLayer(
            layer_type=LayerType.KEY_FACTORS,
            content=content,
            confidence=0.85,
            supporting_data={"factors": factors}
        )
    
    @classmethod
    def generate_evidence(
        cls,
        evidence_items: List[Dict[str, str]]
    ) -> ExplanationLayer:
        """Generate evidence layer."""
        content = "Supporting Evidence:\n\n"
        
        for item in evidence_items[:5]:
            source = item.get("source", "Analysis")
            data = item.get("data", "N/A")
            content += f"• {source}: {data}\n"
        
        return ExplanationLayer(
            layer_type=LayerType.EVIDENCE,
            content=content,
            confidence=0.95,
            supporting_data={"evidence": evidence_items}
        )
    
    @classmethod
    def generate_methodology(
        cls,
        steps: List[str],
        frameworks_used: List[str]
    ) -> ExplanationLayer:
        """Generate methodology layer."""
        content = "How This Conclusion Was Reached:\n\n"
        
        content += "Frameworks Applied:\n"
        for framework in frameworks_used:
            content += f"• {framework}\n"
        
        content += "\nAnalysis Steps:\n"
        for i, step in enumerate(steps, 1):
            content += f"{i}. {step}\n"
        
        return ExplanationLayer(
            layer_type=LayerType.METHODOLOGY,
            content=content,
            confidence=1.0
        )
    
    @classmethod
    def generate_limitations(
        cls,
        limitations: List[str],
        uncertainties: List[str]
    ) -> ExplanationLayer:
        """Generate limitations layer."""
        content = "Known Limitations:\n\n"
        
        for limitation in limitations[:3]:
            content += f"• {limitation}\n"
        
        if uncertainties:
            content += "\nKey Uncertainties:\n"
            for uncertainty in uncertainties[:3]:
                content += f"• {uncertainty}\n"
        
        return ExplanationLayer(
            layer_type=LayerType.LIMITATIONS,
            content=content,
            confidence=1.0
        )
    
    @classmethod
    def generate_recommendations(
        cls,
        recommendations: List[str],
        timeline: str = "immediate"
    ) -> ExplanationLayer:
        """Generate recommendations layer."""
        content = f"Recommended Actions ({timeline}):\n\n"
        
        for i, rec in enumerate(recommendations[:5], 1):
            content += f"{i}. {rec}\n"
        
        return ExplanationLayer(
            layer_type=LayerType.RECOMMENDATIONS,
            content=content,
            confidence=0.8
        )
    
    @classmethod
    def generate_all_layers(
        cls,
        topic: str,
        conclusion: str,
        findings: List[str],
        factors: List[Dict],
        evidence: List[Dict],
        recommendations: List[str],
        audience: AudienceProfile,
        depth: ExplanationDepth
    ) -> List[ExplanationLayer]:
        """Generate all appropriate layers for given depth."""
        layers = []
        layer_types = cls.get_layers_for_depth(depth)
        
        if LayerType.HEADLINE in layer_types:
            layers.append(cls.generate_headline(topic, conclusion))
        
        if LayerType.SUMMARY in layer_types:
            layers.append(cls.generate_summary(findings, conclusion, audience))
        
        if LayerType.KEY_FACTORS in layer_types:
            layers.append(cls.generate_key_factors(factors, audience))
        
        if LayerType.EVIDENCE in layer_types:
            layers.append(cls.generate_evidence(evidence))
        
        if LayerType.METHODOLOGY in layer_types:
            layers.append(cls.generate_methodology(
                steps=["Data collection", "Framework application", "Synthesis"],
                frameworks_used=["Multi-factor analysis"]
            ))
        
        if LayerType.LIMITATIONS in layer_types:
            layers.append(cls.generate_limitations(
                limitations=["Based on available data only"],
                uncertainties=["External factors may change outcomes"]
            ))
        
        if LayerType.RECOMMENDATIONS in layer_types:
            layers.append(cls.generate_recommendations(recommendations))
        
        return layers
