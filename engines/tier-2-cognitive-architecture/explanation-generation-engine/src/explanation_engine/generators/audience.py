"""
EXPLANATION ENGINE v1.0 - Audience Adapter
============================================

Adapts explanations for different audience types.
"""

from typing import List, Dict, Optional
from ..types import (
    Explanation, ExplanationLayer, AudienceProfile, LayerType
)
from ..config import AudienceLevel


class AudienceAdapter:
    """
    Audience Adaptation Engine
    
    Adapts explanations for different audiences:
    - Executive: High-level, action-oriented
    - Technical: Detailed, methodology-focused
    - Domain Expert: Domain-specific language
    - General Public: Simplified, no jargon
    - Stakeholder: Balanced, impact-focused
    """
    
    VOCABULARY_MAPPINGS = {
        AudienceLevel.GENERAL_PUBLIC: {
            "multivariate analysis": "looking at multiple factors together",
            "correlation": "relationship between things",
            "statistical significance": "reliable enough to trust",
            "optimization": "making something work better",
            "latency": "delay or slowness",
            "algorithm": "set of rules or steps",
            "infrastructure": "underlying systems",
            "scalability": "ability to grow",
            "leverage": "use effectively",
            "synergy": "working together well"
        }
    }
    
    FORMAT_PREFERENCES = {
        AudienceLevel.EXECUTIVE: {
            "max_paragraphs": 2,
            "max_bullets": 5,
            "emphasis": "bottom_line",
            "tone": "decisive"
        },
        AudienceLevel.TECHNICAL: {
            "max_paragraphs": None,
            "max_bullets": None,
            "emphasis": "methodology",
            "tone": "precise"
        },
        AudienceLevel.DOMAIN_EXPERT: {
            "max_paragraphs": 5,
            "max_bullets": 7,
            "emphasis": "implications",
            "tone": "professional"
        },
        AudienceLevel.GENERAL_PUBLIC: {
            "max_paragraphs": 3,
            "max_bullets": 5,
            "emphasis": "accessibility",
            "tone": "friendly"
        },
        AudienceLevel.STAKEHOLDER: {
            "max_paragraphs": 4,
            "max_bullets": 6,
            "emphasis": "impact",
            "tone": "balanced"
        }
    }
    
    @classmethod
    def get_audience_profile(cls, level: AudienceLevel) -> AudienceProfile:
        """Get profile for audience level."""
        profiles = {
            AudienceLevel.EXECUTIVE: AudienceProfile.executive(),
            AudienceLevel.TECHNICAL: AudienceProfile(
                level="technical",
                domain_knowledge="deep",
                preferred_format="detailed",
                attention_span="extended",
                decision_authority=False
            ),
            AudienceLevel.DOMAIN_EXPERT: AudienceProfile(
                level="domain_expert",
                domain_knowledge="specialized",
                preferred_format="professional",
                attention_span="focused",
                decision_authority=True
            ),
            AudienceLevel.GENERAL_PUBLIC: AudienceProfile.general(),
            AudienceLevel.STAKEHOLDER: AudienceProfile(
                level="stakeholder",
                domain_knowledge="moderate",
                preferred_format="structured",
                attention_span="medium",
                decision_authority=True
            )
        }
        return profiles.get(level, AudienceProfile.general())
    
    @classmethod
    def simplify_text(
        cls,
        text: str,
        audience_level: AudienceLevel
    ) -> str:
        """Simplify text for audience."""
        if audience_level != AudienceLevel.GENERAL_PUBLIC:
            return text
        
        result = text
        mappings = cls.VOCABULARY_MAPPINGS.get(audience_level, {})
        
        for jargon, simple in mappings.items():
            result = result.replace(jargon, simple)
            result = result.replace(jargon.capitalize(), simple.capitalize())
        
        return result
    
    @classmethod
    def adjust_length(
        cls,
        content: str,
        audience_level: AudienceLevel
    ) -> str:
        """Adjust content length for audience."""
        prefs = cls.FORMAT_PREFERENCES.get(audience_level, {})
        max_paragraphs = prefs.get("max_paragraphs")
        
        if max_paragraphs is None:
            return content
        
        paragraphs = content.split("\n\n")
        if len(paragraphs) > max_paragraphs:
            return "\n\n".join(paragraphs[:max_paragraphs])
        
        return content
    
    @classmethod
    def add_emphasis(
        cls,
        content: str,
        audience_level: AudienceLevel
    ) -> str:
        """Add appropriate emphasis for audience."""
        prefs = cls.FORMAT_PREFERENCES.get(audience_level, {})
        emphasis = prefs.get("emphasis", "none")
        
        if emphasis == "bottom_line":
            return f"BOTTOM LINE: {content}"
        elif emphasis == "methodology":
            return f"[Technical Analysis]\n\n{content}"
        elif emphasis == "impact":
            return f"Key Impact:\n{content}"
        
        return content
    
    @classmethod
    def adapt_layer(
        cls,
        layer: ExplanationLayer,
        audience_level: AudienceLevel
    ) -> ExplanationLayer:
        """Adapt a single layer for audience."""
        content = layer.content
        content = cls.simplify_text(content, audience_level)
        content = cls.adjust_length(content, audience_level)
        
        if layer.layer_type == LayerType.HEADLINE:
            content = cls.add_emphasis(content, audience_level)
        
        return ExplanationLayer(
            layer_type=layer.layer_type,
            content=content,
            confidence=layer.confidence,
            supporting_data=layer.supporting_data
        )
    
    @classmethod
    def adapt_explanation(
        cls,
        explanation: Explanation,
        target_audience: AudienceLevel
    ) -> Explanation:
        """Adapt entire explanation for target audience."""
        new_profile = cls.get_audience_profile(target_audience)
        
        adapted_layers = [
            cls.adapt_layer(layer, target_audience)
            for layer in explanation.layers
        ]
        
        return Explanation(
            topic=explanation.topic,
            audience=new_profile,
            layers=adapted_layers,
            counterfactuals=explanation.counterfactuals,
            quality=explanation.quality,
            verification=explanation.verification
        )
    
    @classmethod
    def get_prompt_section(cls) -> str:
        """Generate prompt section for audience adaptation."""
        return """
AUDIENCE ADAPTATION:
├─ EXECUTIVE: Bottom-line first, 2 paragraphs max, decisive tone
├─ TECHNICAL: Full detail, methodology focus, precise language
├─ DOMAIN EXPERT: Professional, implication-focused
├─ GENERAL PUBLIC: Simplified, no jargon, friendly tone
└─ STAKEHOLDER: Balanced, impact-focused, structured

Vocabulary Simplification (for general public):
├─ "multivariate analysis" → "looking at multiple factors"
├─ "correlation" → "relationship between things"
├─ "statistical significance" → "reliable enough to trust"
└─ "algorithm" → "set of rules or steps"
"""
