"""
EXPLANATION ENGINE v1.0 - Verification
========================================

Verifies explanation quality and accuracy.
"""

from typing import List, Dict, Optional
from ..types import (
    Explanation, ExplanationLayer, VerificationResult,
    ExplanationQuality, QualityLevel, LayerType
)


class ExplanationVerifier:
    """
    Explanation Verification Engine
    
    Verifies:
    - Factual accuracy against source data
    - Logical consistency across layers
    - Completeness of explanation
    - Audience appropriateness
    """
    
    QUALITY_THRESHOLDS = {
        QualityLevel.EXCELLENT: 0.90,
        QualityLevel.GOOD: 0.75,
        QualityLevel.ACCEPTABLE: 0.60,
        QualityLevel.NEEDS_IMPROVEMENT: 0.40,
        QualityLevel.POOR: 0.0
    }
    
    REQUIRED_ELEMENTS = {
        "summary": ["headline", "conclusion"],
        "standard": ["headline", "summary", "factors", "recommendations"],
        "detailed": ["headline", "summary", "factors", "evidence", "recommendations"],
        "comprehensive": ["headline", "summary", "factors", "evidence", "methodology", "limitations", "recommendations"]
    }
    
    @classmethod
    def check_factual_accuracy(
        cls,
        explanation: Explanation,
        source_data: Optional[Dict] = None
    ) -> float:
        """Check factual accuracy against source data."""
        if source_data is None:
            return 0.85
        
        accuracy = 1.0
        
        for layer in explanation.layers:
            if layer.supporting_data:
                for key, value in layer.supporting_data.items():
                    if key in source_data and source_data[key] != value:
                        accuracy -= 0.1
        
        return max(0.0, accuracy)
    
    @classmethod
    def check_logical_consistency(cls, explanation: Explanation) -> float:
        """Check logical consistency across layers."""
        score = 1.0
        
        headline = explanation.get_layer(LayerType.HEADLINE)
        summary = explanation.get_layer(LayerType.SUMMARY)
        recommendations = explanation.get_layer(LayerType.RECOMMENDATIONS)
        
        if headline and summary:
            if len(headline.content) > len(summary.content):
                score -= 0.2
        
        if recommendations:
            if len(recommendations.content) < 20:
                score -= 0.1
        
        confidence_values = [layer.confidence for layer in explanation.layers]
        if confidence_values:
            variance = sum((c - sum(confidence_values)/len(confidence_values))**2 for c in confidence_values)
            if variance > 0.2:
                score -= 0.1
        
        return max(0.0, score)
    
    @classmethod
    def check_completeness(
        cls,
        explanation: Explanation,
        level: str = "standard"
    ) -> float:
        """Check completeness of explanation."""
        required = cls.REQUIRED_ELEMENTS.get(level, cls.REQUIRED_ELEMENTS["standard"])
        
        present_types = [layer.layer_type.value for layer in explanation.layers]
        
        matched = 0
        for req in required:
            for present in present_types:
                if req in present:
                    matched += 1
                    break
        
        return matched / len(required) if required else 1.0
    
    @classmethod
    def check_audience_fit(
        cls,
        explanation: Explanation
    ) -> float:
        """Check if explanation fits target audience."""
        score = 1.0
        
        audience = explanation.audience
        
        for layer in explanation.layers:
            content_length = len(layer.content)
            
            if audience.attention_span == "short" and content_length > 500:
                score -= 0.1
            
            if audience.level == "executive" and content_length > 300:
                score -= 0.05
            
            if audience.level == "technical" and content_length < 100:
                score -= 0.05
        
        return max(0.0, score)
    
    @classmethod
    def identify_issues(cls, explanation: Explanation) -> List[str]:
        """Identify issues with the explanation."""
        issues = []
        
        if not explanation.layers:
            issues.append("No explanation layers present")
        
        headline = explanation.get_layer(LayerType.HEADLINE)
        if not headline:
            issues.append("Missing headline layer")
        
        summary = explanation.get_layer(LayerType.SUMMARY)
        if not summary:
            issues.append("Missing summary layer")
        
        for layer in explanation.layers:
            if layer.confidence < 0.5:
                issues.append(f"Low confidence in {layer.layer_type.value} layer")
        
        return issues
    
    @classmethod
    def generate_suggestions(
        cls,
        explanation: Explanation,
        issues: List[str]
    ) -> List[str]:
        """Generate improvement suggestions."""
        suggestions = []
        
        if "Missing headline" in str(issues):
            suggestions.append("Add a clear, one-sentence headline")
        
        if "Missing summary" in str(issues):
            suggestions.append("Add a summary of key points")
        
        if "Low confidence" in str(issues):
            suggestions.append("Strengthen evidence for low-confidence claims")
        
        if not explanation.counterfactuals:
            suggestions.append("Consider adding 'what if' scenarios")
        
        if len(explanation.layers) < 3:
            suggestions.append("Expand explanation with more detail layers")
        
        return suggestions
    
    @classmethod
    def determine_quality_level(cls, scores: Dict[str, float]) -> QualityLevel:
        """Determine overall quality level from scores."""
        avg_score = sum(scores.values()) / len(scores) if scores else 0.0
        
        for level, threshold in cls.QUALITY_THRESHOLDS.items():
            if avg_score >= threshold:
                return level
        
        return QualityLevel.POOR
    
    @classmethod
    def verify(
        cls,
        explanation: Explanation,
        source_data: Optional[Dict] = None
    ) -> VerificationResult:
        """Verify explanation factual accuracy and consistency."""
        factual = cls.check_factual_accuracy(explanation, source_data)
        logical = cls.check_logical_consistency(explanation)
        completeness = cls.check_completeness(explanation)
        issues = cls.identify_issues(explanation)
        
        is_valid = factual >= 0.7 and logical >= 0.7 and len(issues) < 3
        
        return VerificationResult(
            is_valid=is_valid,
            factual_accuracy=factual,
            logical_consistency=logical,
            source_coverage=completeness,
            issues=issues
        )
    
    @classmethod
    def assess_quality(
        cls,
        explanation: Explanation,
        source_data: Optional[Dict] = None
    ) -> ExplanationQuality:
        """Assess overall quality of explanation."""
        clarity = cls.check_logical_consistency(explanation)
        completeness = cls.check_completeness(explanation)
        accuracy = cls.check_factual_accuracy(explanation, source_data)
        audience_fit = cls.check_audience_fit(explanation)
        
        scores = {
            "clarity": clarity,
            "completeness": completeness,
            "accuracy": accuracy,
            "audience_fit": audience_fit
        }
        
        overall = cls.determine_quality_level(scores)
        issues = cls.identify_issues(explanation)
        suggestions = cls.generate_suggestions(explanation, issues)
        
        return ExplanationQuality(
            overall_level=overall,
            clarity_score=clarity,
            completeness_score=completeness,
            accuracy_score=accuracy,
            audience_fit_score=audience_fit,
            issues=issues,
            suggestions=suggestions
        )
