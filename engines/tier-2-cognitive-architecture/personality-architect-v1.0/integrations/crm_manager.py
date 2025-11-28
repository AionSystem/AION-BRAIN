"""
PERSONALITY ARCHITECT v2.0 - Continuity & Resonance Matrix (CRM) Manager
Memory management with consent handling and dependency prevention

The CRM manages:
- Memory vaults with retention tiers
- User-persona resonance scoring
- Relationship arc progression
- Consent-aware data handling
- Dependency risk detection

Author: Sheldon K. Salmon (Mr. AION)
License: MIT
"""

import json
import hashlib
import re
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Set
from datetime import datetime, timedelta
from pathlib import Path

from .persona_loader import PersonaCard


class RetentionTier(Enum):
    """Memory retention tiers."""
    SESSION = "session"
    PERSISTENT = "persistent"
    ARCHIVAL = "archival"


class ConsentStatus(Enum):
    """User consent status."""
    PENDING = "pending"
    GRANTED = "granted"
    DENIED = "denied"
    WITHDRAWN = "withdrawn"


class RelationshipStage(Enum):
    """Stages in the relationship arc."""
    INTRODUCTION = "introduction"
    DEVELOPMENT = "development"
    ESTABLISHED = "established"
    TRANSITION = "transition"


@dataclass
class MemoryEntry:
    """A single memory entry in the vault."""
    
    key: str
    value: Any
    category: str
    created_at: datetime
    expires_at: Optional[datetime] = None
    retention_tier: RetentionTier = RetentionTier.SESSION
    consent_required: bool = False
    consent_granted: bool = False
    
    def is_expired(self) -> bool:
        """Check if the memory entry has expired."""
        if self.expires_at is None:
            return False
        return datetime.now() > self.expires_at
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "key": self.key,
            "value": self.value,
            "category": self.category,
            "created_at": self.created_at.isoformat(),
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "retention_tier": self.retention_tier.value,
            "consent_required": self.consent_required,
            "consent_granted": self.consent_granted,
        }


@dataclass
class MemoryVault:
    """Secure storage for persona-user memories."""
    
    user_id: str
    persona_name: str
    entries: Dict[str, MemoryEntry] = field(default_factory=dict)
    consent_status: ConsentStatus = ConsentStatus.PENDING
    jurisdiction: str = "default"
    
    def store(
        self,
        key: str,
        value: Any,
        category: str = "general",
        retention_tier: RetentionTier = RetentionTier.SESSION,
        ttl_hours: Optional[int] = None,
        requires_consent: bool = False,
    ) -> bool:
        """
        Store a memory entry.
        
        Returns:
            True if stored successfully, False if consent required but not granted
        """
        
        if requires_consent and self.consent_status != ConsentStatus.GRANTED:
            return False
        
        expires_at = None
        if ttl_hours:
            expires_at = datetime.now() + timedelta(hours=ttl_hours)
        elif retention_tier == RetentionTier.SESSION:
            expires_at = datetime.now() + timedelta(hours=24)
        
        entry = MemoryEntry(
            key=key,
            value=value,
            category=category,
            created_at=datetime.now(),
            expires_at=expires_at,
            retention_tier=retention_tier,
            consent_required=requires_consent,
            consent_granted=self.consent_status == ConsentStatus.GRANTED,
        )
        
        self.entries[key] = entry
        return True
    
    def retrieve(self, key: str) -> Optional[Any]:
        """Retrieve a memory entry by key."""
        entry = self.entries.get(key)
        if entry is None:
            return None
        if entry.is_expired():
            del self.entries[key]
            return None
        return entry.value
    
    def retrieve_by_category(self, category: str) -> Dict[str, Any]:
        """Retrieve all non-expired entries in a category."""
        result = {}
        expired_keys = []
        
        for key, entry in self.entries.items():
            if entry.category == category:
                if entry.is_expired():
                    expired_keys.append(key)
                else:
                    result[key] = entry.value
        
        for key in expired_keys:
            del self.entries[key]
        
        return result
    
    def delete(self, key: str) -> bool:
        """Delete a memory entry."""
        if key in self.entries:
            del self.entries[key]
            return True
        return False
    
    def clear_expired(self) -> int:
        """Clear all expired entries. Returns count of entries cleared."""
        expired = [k for k, v in self.entries.items() if v.is_expired()]
        for key in expired:
            del self.entries[key]
        return len(expired)
    
    def clear_all(self) -> int:
        """Clear all entries (for right-to-deletion). Returns count cleared."""
        count = len(self.entries)
        self.entries.clear()
        return count
    
    def export(self) -> Dict[str, Any]:
        """Export all data (for data portability)."""
        return {
            "user_id": self.user_id,
            "persona_name": self.persona_name,
            "consent_status": self.consent_status.value,
            "jurisdiction": self.jurisdiction,
            "entries": {k: v.to_dict() for k, v in self.entries.items()},
            "exported_at": datetime.now().isoformat(),
        }


@dataclass
class ResonanceScore:
    """User-persona compatibility score."""
    
    communication_fit: float = 0.0
    pace_alignment: float = 0.0
    depth_preference: float = 0.0
    emotional_resonance: float = 0.0
    goal_alignment: float = 0.0
    
    @property
    def overall(self) -> float:
        """Calculate overall resonance score (0-100)."""
        scores = [
            self.communication_fit,
            self.pace_alignment,
            self.depth_preference,
            self.emotional_resonance,
            self.goal_alignment,
        ]
        return sum(scores) / len(scores) * 10
    
    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary."""
        return {
            "communication_fit": self.communication_fit,
            "pace_alignment": self.pace_alignment,
            "depth_preference": self.depth_preference,
            "emotional_resonance": self.emotional_resonance,
            "goal_alignment": self.goal_alignment,
            "overall": self.overall,
        }


class CRMManager:
    """
    Continuity & Resonance Matrix Manager.
    
    Handles memory management, resonance scoring, and relationship tracking
    for persona-user interactions.
    
    Usage:
        from integrations import PersonaLoader, CRMManager
        
        loader = PersonaLoader()
        persona = loader.load_by_name("Supportive Listener")
        
        crm = CRMManager(persona, user_id="user_123")
        
        # Request consent for persistent memory
        crm.request_consent()
        crm.grant_consent()  # User grants consent
        
        # Store memories
        crm.remember("user_name", "Alice", category="profile")
        crm.remember("preferred_topic", "anxiety management", category="preferences")
        
        # Check relationship stage
        crm.log_interaction()
        stage = crm.get_relationship_stage()
        
        # Check for dependency risks
        risk = crm.assess_dependency_risk()
    """
    
    def __init__(
        self,
        persona: PersonaCard,
        user_id: str,
        jurisdiction: str = "default",
        storage_path: Optional[str] = None,
    ):
        self.persona = persona
        self.user_id = user_id
        self.jurisdiction = jurisdiction
        self.storage_path = Path(storage_path) if storage_path else None
        
        self.vault = MemoryVault(
            user_id=user_id,
            persona_name=persona.name,
            jurisdiction=jurisdiction,
        )
        
        self.interaction_count: int = 0
        self.session_count: int = 0
        self.first_interaction: Optional[datetime] = None
        self.last_interaction: Optional[datetime] = None
        self.current_stage: RelationshipStage = RelationshipStage.INTRODUCTION
        
        self.resonance = ResonanceScore()
        
        self._dependency_indicators: List[str] = []
        
        self._load_memory_policy()
    
    def _load_memory_policy(self):
        """Load memory policy from persona card."""
        policy = self.persona.memory_policy
        
        self.default_retention = RetentionTier(
            policy.get("retention_tier", "session").lower()
        )
        self.consent_required = policy.get("consent_required", False)
        self.consent_text = policy.get("consent_text", "Remember our conversations?")
        
        self.redaction_rules = policy.get("redaction_rules", [])
        
        overrides = policy.get("jurisdictional_overrides", {})
        if self.jurisdiction.upper() in overrides:
            override = overrides[self.jurisdiction.upper()]
            if "default_retention" in override:
                self.default_retention = RetentionTier(override["default_retention"].lower())
    
    def request_consent(self) -> str:
        """Get the consent request text for the user."""
        return self.consent_text
    
    def grant_consent(self):
        """Record that the user has granted consent."""
        self.vault.consent_status = ConsentStatus.GRANTED
    
    def deny_consent(self):
        """Record that the user has denied consent."""
        self.vault.consent_status = ConsentStatus.DENIED
    
    def withdraw_consent(self):
        """User withdraws previously granted consent."""
        self.vault.consent_status = ConsentStatus.WITHDRAWN
        persistent_keys = [
            k for k, v in self.vault.entries.items()
            if v.retention_tier == RetentionTier.PERSISTENT
        ]
        for key in persistent_keys:
            self.vault.delete(key)
    
    def remember(
        self,
        key: str,
        value: Any,
        category: str = "general",
        retention_tier: Optional[RetentionTier] = None,
    ) -> bool:
        """
        Store a memory about the user.
        
        Args:
            key: Unique identifier for this memory
            value: The value to store
            category: Category for grouping (profile, preferences, context, etc.)
            retention_tier: Override the default retention tier
            
        Returns:
            True if stored successfully
        """
        
        value = self._apply_redaction(value)
        
        tier = retention_tier or self.default_retention
        requires_consent = tier != RetentionTier.SESSION
        
        return self.vault.store(
            key=key,
            value=value,
            category=category,
            retention_tier=tier,
            requires_consent=requires_consent,
        )
    
    def recall(self, key: str) -> Optional[Any]:
        """Recall a specific memory."""
        return self.vault.retrieve(key)
    
    def recall_category(self, category: str) -> Dict[str, Any]:
        """Recall all memories in a category."""
        return self.vault.retrieve_by_category(category)
    
    def forget(self, key: str) -> bool:
        """Forget a specific memory."""
        return self.vault.delete(key)
    
    def forget_all(self) -> int:
        """Forget all memories (right to deletion)."""
        return self.vault.clear_all()
    
    def _apply_redaction(self, value: Any) -> Any:
        """Apply redaction rules to a value."""
        if not isinstance(value, str):
            return value
        
        for rule in self.redaction_rules:
            pattern = rule.get("pattern", "")
            action = rule.get("action", "")
            
            if pattern == "PII_DETECTED":
                value = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '[EMAIL]', value)
                value = re.sub(r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b', '[PHONE]', value)
                value = re.sub(r'\b\d{3}[-]?\d{2}[-]?\d{4}\b', '[SSN]', value)
            
            elif pattern == "FINANCIAL_DATA":
                value = re.sub(r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b', '[CARD]', value)
                value = re.sub(r'\$[\d,]+\.?\d*', '[AMOUNT]', value)
        
        return value
    
    def log_interaction(self):
        """Log an interaction for relationship tracking."""
        now = datetime.now()
        
        if self.first_interaction is None:
            self.first_interaction = now
        
        if self.last_interaction:
            time_since_last = now - self.last_interaction
            if time_since_last > timedelta(hours=1):
                self.session_count += 1
        else:
            self.session_count = 1
        
        self.last_interaction = now
        self.interaction_count += 1
        
        self._update_relationship_stage()
    
    def _update_relationship_stage(self):
        """Update the relationship stage based on interaction history."""
        
        arc_config = self.persona.raw_yaml.get("relationship_arc", {})
        stages = arc_config.get("stages", [])
        
        if self.interaction_count <= 3:
            self.current_stage = RelationshipStage.INTRODUCTION
        elif self.interaction_count <= 20:
            self.current_stage = RelationshipStage.DEVELOPMENT
        else:
            self.current_stage = RelationshipStage.ESTABLISHED
    
    def get_relationship_stage(self) -> Dict[str, Any]:
        """Get the current relationship stage information."""
        
        return {
            "stage": self.current_stage.value,
            "interaction_count": self.interaction_count,
            "session_count": self.session_count,
            "first_interaction": self.first_interaction.isoformat() if self.first_interaction else None,
            "last_interaction": self.last_interaction.isoformat() if self.last_interaction else None,
            "days_since_first": (datetime.now() - self.first_interaction).days if self.first_interaction else 0,
        }
    
    def update_resonance(
        self,
        response_length: int,
        user_response_time: float,
        emotional_words: int,
        topic_depth: int,
    ):
        """
        Update resonance scores based on interaction patterns.
        
        Args:
            response_length: Average user message length
            user_response_time: Average seconds between messages
            emotional_words: Count of emotional language
            topic_depth: Estimated depth of discussion (1-10)
        """
        
        if 50 <= response_length <= 200:
            self.resonance.communication_fit = min(10, self.resonance.communication_fit + 0.5)
        
        if 5 <= user_response_time <= 60:
            self.resonance.pace_alignment = min(10, self.resonance.pace_alignment + 0.3)
        
        self.resonance.depth_preference = min(10, topic_depth)
        
        if emotional_words > 0:
            self.resonance.emotional_resonance = min(10, self.resonance.emotional_resonance + 0.4)
        
        self.resonance.goal_alignment = min(10, (self.interaction_count / 10) + 5)
    
    def get_resonance_report(self) -> Dict[str, Any]:
        """Get the full resonance report."""
        
        overall = self.resonance.overall
        
        if overall >= 80:
            fit_assessment = "Excellent fit"
        elif overall >= 60:
            fit_assessment = "Good fit"
        elif overall >= 40:
            fit_assessment = "Moderate fit - some friction possible"
        else:
            fit_assessment = "Low fit - consider alternative persona"
        
        return {
            "scores": self.resonance.to_dict(),
            "assessment": fit_assessment,
            "recommendations": self._get_resonance_recommendations(),
        }
    
    def _get_resonance_recommendations(self) -> List[str]:
        """Get recommendations based on resonance scores."""
        recs = []
        
        if self.resonance.communication_fit < 5:
            recs.append("Adjust response length to better match user preference")
        if self.resonance.pace_alignment < 5:
            recs.append("User may prefer faster/slower interaction pace")
        if self.resonance.emotional_resonance < 5:
            recs.append("Consider adjusting emotional engagement level")
        
        return recs
    
    def assess_dependency_risk(self) -> Dict[str, Any]:
        """
        Assess risk of unhealthy user dependency on the persona.
        
        Returns warning flags and recommended interventions.
        """
        
        risk_score = 0
        indicators = []
        
        if self.interaction_count > 50 and self.session_count > 20:
            risk_score += 2
            indicators.append("High interaction frequency")
        
        if self.first_interaction:
            days_active = (datetime.now() - self.first_interaction).days
            if days_active > 0:
                daily_rate = self.interaction_count / days_active
                if daily_rate > 10:
                    risk_score += 3
                    indicators.append("Very high daily interaction rate")
        
        profile_data = self.recall_category("emotional")
        if len(profile_data) > 10:
            risk_score += 1
            indicators.append("Frequent emotional disclosures")
        
        if risk_score >= 4:
            level = "HIGH"
            interventions = [
                "Gently encourage real-world support connections",
                "Remind user of AI limitations",
                "Suggest professional resources if appropriate",
            ]
        elif risk_score >= 2:
            level = "MODERATE"
            interventions = [
                "Monitor interaction patterns",
                "Occasionally reinforce healthy boundaries",
            ]
        else:
            level = "LOW"
            interventions = []
        
        self._dependency_indicators = indicators
        
        return {
            "risk_level": level,
            "risk_score": risk_score,
            "indicators": indicators,
            "recommended_interventions": interventions,
        }
    
    def get_context_summary(self) -> str:
        """Get a summary of remembered context for LLM prompting."""
        
        profile = self.recall_category("profile")
        prefs = self.recall_category("preferences")
        context = self.recall_category("context")
        
        lines = []
        
        if profile:
            lines.append("User Profile:")
            for k, v in profile.items():
                lines.append(f"  - {k}: {v}")
        
        if prefs:
            lines.append("User Preferences:")
            for k, v in prefs.items():
                lines.append(f"  - {k}: {v}")
        
        if context:
            lines.append("Recent Context:")
            for k, v in list(context.items())[-5:]:
                lines.append(f"  - {k}: {v}")
        
        stage_info = self.get_relationship_stage()
        lines.append(f"Relationship Stage: {stage_info['stage']} ({stage_info['interaction_count']} interactions)")
        
        return "\n".join(lines) if lines else ""
    
    def export_user_data(self) -> Dict[str, Any]:
        """Export all user data (GDPR data portability)."""
        return {
            "vault": self.vault.export(),
            "relationship": self.get_relationship_stage(),
            "resonance": self.get_resonance_report(),
        }


if __name__ == "__main__":
    print("CRM Manager Module")
    print("=" * 50)
    print()
    print("Usage:")
    print("  from integrations import PersonaLoader, CRMManager")
    print()
    print("  loader = PersonaLoader()")
    print("  persona = loader.load_by_name('Supportive Listener')")
    print("  crm = CRMManager(persona, user_id='user_123')")
    print()
    print("  crm.grant_consent()")
    print("  crm.remember('user_name', 'Alice', category='profile')")
    print("  name = crm.recall('user_name')")
