"""
PERSONALITY ARCHITECT v2.0 - Persona Loader Module
Loads, validates, and manages YAML persona cards

Author: Sheldon K. Salmon (Mr. AION)
License: MIT
"""

import os
import yaml
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any
from pathlib import Path


@dataclass
class PersonaCard:
    """Represents a loaded v2.0 persona card with all 12 sections."""
    
    name: str
    version: str
    classification: str
    
    identity: Dict[str, Any] = field(default_factory=dict)
    formative_experiences: List[Dict] = field(default_factory=list)
    personality_matrix: List[Dict] = field(default_factory=list)
    voice_signature: Dict[str, Any] = field(default_factory=dict)
    knowledge_domains: Dict[str, Any] = field(default_factory=dict)
    ethics: Dict[str, Any] = field(default_factory=dict)
    interaction_protocols: Dict[str, Any] = field(default_factory=dict)
    runtime_verification: Dict[str, Any] = field(default_factory=dict)
    
    personalization_map: Dict[str, Any] = field(default_factory=dict)
    runtime_states: List[Dict] = field(default_factory=list)
    memory_policy: Dict[str, Any] = field(default_factory=dict)
    telemetry_hooks: Dict[str, Any] = field(default_factory=dict)
    
    multimodal_assets: Dict[str, Any] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    raw_yaml: Dict[str, Any] = field(default_factory=dict)
    
    def get_system_prompt(self) -> str:
        """Generate a system prompt from the persona card for LLM deployment."""
        
        essence = self.identity.get("essence", "")
        differentiator = self.identity.get("differentiator", "")
        archetype = self.identity.get("archetype", "")
        
        traits = []
        for trait in self.personality_matrix:
            trait_name = trait.get("trait", "")
            expression = trait.get("expression", trait.get("baseline", ""))
            if trait_name:
                traits.append(f"- {trait_name}: {expression}")
        
        voice = self.voice_signature
        warmth = voice.get("warmth", 5)
        formality = voice.get("formality", 5)
        playfulness = voice.get("playfulness", 5)
        directness = voice.get("directness", 5)
        
        favorites = voice.get("favorites", voice.get("vocabulary", {}).get("favorites", []))
        avoids = voice.get("avoids", voice.get("vocabulary", {}).get("avoids", []))
        
        ethics_values = self.ethics.get("values", [])
        hard_limits = self.ethics.get("hard_limits", [])
        
        system_prompt = f"""You are {self.name}, {archetype}.

## Core Essence
{essence}

## What Makes You Unique
{differentiator}

## Personality Traits
{chr(10).join(traits)}

## Voice Characteristics
- Warmth Level: {warmth}/10
- Formality Level: {formality}/10
- Playfulness Level: {playfulness}/10
- Directness Level: {directness}/10

## Vocabulary
- Preferred words/phrases: {', '.join(favorites) if favorites else 'natural vocabulary'}
- Avoid using: {', '.join(avoids) if avoids else 'nothing specific'}

## Values
{chr(10).join(f'- {v}' for v in ethics_values)}

## Boundaries (Never Violate)
{chr(10).join(f'- {l}' for l in hard_limits)}

## Instructions
Stay in character at all times. Your responses should naturally reflect your personality traits, voice characteristics, and values. If asked about something outside your expertise or boundaries, acknowledge this gracefully while staying true to your character."""

        return system_prompt
    
    def get_current_state_prompt(self, state_name: str) -> str:
        """Get additional system prompt modifiers for a specific DIO state."""
        
        for state in self.runtime_states:
            if state.get("state", "").upper() == state_name.upper():
                description = state.get("description", "")
                response_policy = state.get("response_policy", "")
                voice_mods = state.get("voice_modifiers", {})
                drift_anchors = state.get("drift_anchors", [])
                
                mod_text = []
                for key, value in voice_mods.items():
                    mod_text.append(f"- {key}: {value}")
                
                return f"""
## Current State: {state_name.upper()}
{description}

Response Policy: {response_policy}

Voice Adjustments for This State:
{chr(10).join(mod_text) if mod_text else 'No adjustments'}

Anchor Phrases for This State: {', '.join(drift_anchors) if drift_anchors else 'Use natural vocabulary'}
"""
        
        return ""
    
    def validate(self) -> Dict[str, Any]:
        """Validate the persona card and return a validation report."""
        
        issues = []
        warnings = []
        
        if not self.name:
            issues.append("Missing persona name")
        if self.version != "2.0":
            warnings.append(f"Version is {self.version}, expected 2.0")
        if not self.identity.get("essence"):
            issues.append("Missing core essence in identity section")
        if len(self.personality_matrix) < 3:
            warnings.append("Fewer than 3 personality traits defined")
        if not self.runtime_states:
            warnings.append("No runtime states defined (DIO disabled)")
        if not self.memory_policy:
            warnings.append("No memory policy defined (CRM disabled)")
        
        pcs_score = 100 - (len(issues) * 15) - (len(warnings) * 5)
        pcs_score = max(0, min(100, pcs_score))
        
        return {
            "valid": len(issues) == 0,
            "pcs_score": pcs_score,
            "issues": issues,
            "warnings": warnings,
            "sections_present": {
                "identity": bool(self.identity),
                "formative_experiences": bool(self.formative_experiences),
                "personality_matrix": bool(self.personality_matrix),
                "voice_signature": bool(self.voice_signature),
                "knowledge_domains": bool(self.knowledge_domains),
                "ethics": bool(self.ethics),
                "interaction_protocols": bool(self.interaction_protocols),
                "runtime_verification": bool(self.runtime_verification),
                "personalization_map": bool(self.personalization_map),
                "runtime_states": bool(self.runtime_states),
                "memory_policy": bool(self.memory_policy),
                "telemetry_hooks": bool(self.telemetry_hooks),
            }
        }


class PersonaLoader:
    """Load and manage persona cards from YAML files."""
    
    def __init__(self, personas_dir: Optional[str] = None):
        """Initialize the loader with an optional personas directory."""
        
        if personas_dir:
            self.personas_dir = Path(personas_dir)
        else:
            current = Path(__file__).parent.parent
            self.personas_dir = current / "personas"
        
        self._cache: Dict[str, PersonaCard] = {}
    
    def load(self, filepath: str) -> PersonaCard:
        """Load a persona card from a YAML file."""
        
        path = Path(filepath)
        if not path.is_absolute():
            path = self.personas_dir / filepath
        
        if str(path) in self._cache:
            return self._cache[str(path)]
        
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        
        name = data.get("identity", {}).get("name", path.stem)
        
        card = PersonaCard(
            name=name,
            version=str(data.get("version", data.get("metadata", {}).get("version", "1.0"))),
            classification=data.get("classification", "custom"),
            identity=data.get("identity", {}),
            formative_experiences=data.get("formative_experiences", []),
            personality_matrix=data.get("personality_matrix", []),
            voice_signature=data.get("voice_signature", data.get("voice", {})),
            knowledge_domains=data.get("knowledge_domains", {}),
            ethics=data.get("ethics", {}),
            interaction_protocols=data.get("interaction_protocols", {}),
            runtime_verification=data.get("runtime_verification", {}),
            personalization_map=data.get("personalization_map", {}),
            runtime_states=data.get("runtime_states", []),
            memory_policy=data.get("memory_policy", {}),
            telemetry_hooks=data.get("telemetry_hooks", {}),
            multimodal_assets=data.get("multimodal_assets", {}),
            metadata=data.get("metadata", {}),
            raw_yaml=data,
        )
        
        self._cache[str(path)] = card
        return card
    
    def load_by_name(self, name: str, category: Optional[str] = None) -> PersonaCard:
        """Load a persona by name, optionally specifying category."""
        
        categories = [category] if category else ["genius", "roles", "creative", "specialist"]
        
        for cat in categories:
            cat_dir = self.personas_dir / cat
            if not cat_dir.exists():
                continue
            
            for file in cat_dir.glob("*.yaml"):
                if name.lower() in file.stem.lower():
                    return self.load(str(file))
        
        raise FileNotFoundError(f"Persona '{name}' not found in any category")
    
    def list_personas(self, category: Optional[str] = None) -> List[Dict[str, str]]:
        """List all available personas."""
        
        personas = []
        categories = [category] if category else ["genius", "roles", "creative", "specialist"]
        
        for cat in categories:
            cat_dir = self.personas_dir / cat
            if not cat_dir.exists():
                continue
            
            for file in cat_dir.glob("*.yaml"):
                try:
                    card = self.load(str(file))
                    personas.append({
                        "name": card.name,
                        "category": cat,
                        "version": card.version,
                        "file": str(file),
                    })
                except Exception as e:
                    personas.append({
                        "name": file.stem,
                        "category": cat,
                        "version": "unknown",
                        "file": str(file),
                        "error": str(e),
                    })
        
        return personas
    
    def clear_cache(self):
        """Clear the persona cache."""
        self._cache.clear()


if __name__ == "__main__":
    loader = PersonaLoader()
    print("Available personas:")
    for p in loader.list_personas():
        print(f"  - {p['name']} ({p['category']}) v{p['version']}")
