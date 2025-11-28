"""
PERSONALITY ARCHITECT v2.0 - Integration Package
Enterprise-grade API integrations for persona deployment

This package provides:
- PersonaLoader: Load and validate YAML persona cards
- LLMRuntime: Deploy personas to OpenAI, Anthropic, or custom LLMs
- DIORuntime: Dynamic Identity Orchestrator for state-based adaptation
- CRMManager: Continuity & Resonance Matrix for memory management
- MultimodalAssets: Voice synthesis and avatar integration

Author: Sheldon K. Salmon (Mr. AION)
License: MIT
"""

from .persona_loader import PersonaLoader, PersonaCard
from .llm_runtime import LLMRuntime, LLMProvider
from .dio_runtime import DIORuntime, PersonaState
from .crm_manager import CRMManager, MemoryVault
from .multimodal import MultimodalAssets, VoiceProfile

__version__ = "2.0.0"
__all__ = [
    "PersonaLoader",
    "PersonaCard",
    "LLMRuntime",
    "LLMProvider",
    "DIORuntime",
    "PersonaState",
    "CRMManager",
    "MemoryVault",
    "MultimodalAssets",
    "VoiceProfile",
]
