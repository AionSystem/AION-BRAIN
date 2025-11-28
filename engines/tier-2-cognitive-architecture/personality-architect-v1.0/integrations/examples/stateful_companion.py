#!/usr/bin/env python3
"""
PERSONALITY ARCHITECT v2.0 - Stateful Companion Example

This example demonstrates the full power of Personality Architect:
- LLM Runtime for conversation
- DIO for state-based adaptation
- CRM for memory and relationship tracking
- Multimodal for voice synthesis (optional)

This creates a companion AI that:
- Remembers user information across conversations
- Adapts its behavior based on emotional context
- Tracks relationship development
- Monitors for unhealthy dependency patterns

Requirements:
    pip install openai anthropic elevenlabs pyyaml

Usage:
    export OPENAI_API_KEY="your-key"
    export ELEVEN_API_KEY="your-key"  # Optional, for voice
    python stateful_companion.py
"""

import os
import sys
import json
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from persona_loader import PersonaLoader
from llm_runtime import LLMRuntime, LLMProvider
from dio_runtime import DIORuntime
from crm_manager import CRMManager, RetentionTier
from multimodal import MultimodalAssets, EmotionalState


class StatefulCompanion:
    """A fully-featured persona companion with memory and state awareness."""
    
    def __init__(
        self,
        persona_name: str,
        user_id: str,
        llm_provider: LLMProvider = LLMProvider.OPENAI,
        enable_voice: bool = False,
    ):
        loader = PersonaLoader()
        self.persona = loader.load_by_name(persona_name)
        self.user_id = user_id
        self.enable_voice = enable_voice
        
        api_key = self._get_api_key(llm_provider)
        
        self.runtime = LLMRuntime(
            persona=self.persona,
            provider=llm_provider,
            api_key=api_key,
        )
        
        self.dio = DIORuntime(self.persona)
        
        self.crm = CRMManager(
            persona=self.persona,
            user_id=user_id,
        )
        
        if enable_voice:
            eleven_key = os.environ.get("ELEVEN_API_KEY")
            if eleven_key:
                self.assets = MultimodalAssets(
                    persona=self.persona,
                    elevenlabs_api_key=eleven_key
                )
            else:
                print("Warning: ELEVEN_API_KEY not set, voice disabled")
                self.enable_voice = False
                self.assets = None
        else:
            self.assets = None
        
        self.session_start = datetime.now()
        self.message_count = 0
    
    def _get_api_key(self, provider: LLMProvider) -> str:
        """Get the appropriate API key for the provider."""
        if provider == LLMProvider.OPENAI:
            key = os.environ.get("OPENAI_API_KEY")
            if not key:
                raise ValueError("OPENAI_API_KEY environment variable not set")
            return key
        elif provider == LLMProvider.ANTHROPIC:
            key = os.environ.get("ANTHROPIC_API_KEY")
            if not key:
                raise ValueError("ANTHROPIC_API_KEY environment variable not set")
            return key
        else:
            raise ValueError(f"Unsupported provider: {provider}")
    
    def setup_consent(self):
        """Handle consent flow for memory storage."""
        print("\n" + "="*50)
        print("MEMORY CONSENT")
        print("="*50)
        print(f"\n{self.persona.name} asks:")
        print(f'"{self.crm.request_consent()}"')
        print("\nThis allows the persona to remember things about you")
        print("across conversations for a more personalized experience.")
        
        choice = input("\nGrant consent? (yes/no): ").strip().lower()
        
        if choice in ['yes', 'y']:
            self.crm.grant_consent()
            print("\nConsent granted. Memory enabled.")
            return True
        else:
            self.crm.deny_consent()
            print("\nConsent denied. Session-only memory.")
            return False
    
    def process_message(self, user_message: str) -> dict:
        """Process a user message and generate a response."""
        
        self.message_count += 1
        self.crm.log_interaction()
        
        new_state, rationale = self.dio.analyze_input(user_message)
        state_changed = False
        
        if new_state:
            old_state = self.dio.get_current_state_name()
            self.dio.transition_to(new_state)
            self.runtime.set_state(new_state)
            state_changed = True
            print(f"\n[State: {old_state} -> {new_state}]")
        
        context = self.crm.get_context_summary()
        
        response = self.runtime.chat(user_message)
        
        drift = self.dio.detect_drift(response.content)
        
        coherence = self.runtime.run_coherence_check(response.content)
        
        audio = None
        if self.enable_voice and self.assets:
            emotion = self.assets.detect_emotional_state(response.content)
            try:
                audio = self.assets.text_to_speech(response.content, emotion)
            except Exception as e:
                print(f"[Voice generation failed: {e}]")
        
        self._update_resonance(user_message, response.content)
        
        return {
            "content": response.content,
            "state": self.dio.get_current_state_name(),
            "state_changed": state_changed,
            "drift": drift.severity.value,
            "coherence": coherence['coherence_status'],
            "audio": audio,
        }
    
    def _update_resonance(self, user_msg: str, response: str):
        """Update resonance scores based on interaction."""
        emotional_words = ['feel', 'feeling', 'felt', 'emotion', 'happy', 
                          'sad', 'angry', 'worried', 'excited', 'love', 'hate']
        emotional_count = sum(1 for w in emotional_words if w in user_msg.lower())
        
        self.crm.update_resonance(
            response_length=len(user_msg),
            user_response_time=5.0,
            emotional_words=emotional_count,
            topic_depth=5,
        )
    
    def remember(self, key: str, value: str, category: str = "context"):
        """Store a memory about the user."""
        success = self.crm.remember(key, value, category=category)
        if success:
            print(f"[Remembered: {key}]")
        else:
            print(f"[Memory denied - consent required]")
        return success
    
    def recall(self, key: str):
        """Recall a stored memory."""
        return self.crm.recall(key)
    
    def get_status(self) -> dict:
        """Get the current status of the companion."""
        relationship = self.crm.get_relationship_stage()
        resonance = self.crm.get_resonance_report()
        dependency = self.crm.assess_dependency_risk()
        
        return {
            "persona": self.persona.name,
            "user_id": self.user_id,
            "current_state": self.dio.get_current_state_name(),
            "available_states": self.dio.get_available_states(),
            "session_messages": self.message_count,
            "relationship": {
                "stage": relationship['stage'],
                "total_interactions": relationship['interaction_count'],
                "sessions": relationship['session_count'],
            },
            "resonance": {
                "overall": resonance['scores']['overall'],
                "assessment": resonance['assessment'],
            },
            "dependency_risk": {
                "level": dependency['risk_level'],
                "indicators": dependency['indicators'],
            },
        }
    
    def show_status(self):
        """Display formatted status."""
        status = self.get_status()
        
        print("\n" + "="*50)
        print("COMPANION STATUS")
        print("="*50)
        print(f"Persona: {status['persona']}")
        print(f"User: {status['user_id']}")
        print(f"Current State: {status['current_state']}")
        print(f"Session Messages: {status['session_messages']}")
        print(f"\nRelationship:")
        print(f"  Stage: {status['relationship']['stage']}")
        print(f"  Total Interactions: {status['relationship']['total_interactions']}")
        print(f"\nResonance:")
        print(f"  Overall: {status['resonance']['overall']:.1f}/100")
        print(f"  Assessment: {status['resonance']['assessment']}")
        print(f"\nDependency Risk: {status['dependency_risk']['level']}")
        if status['dependency_risk']['indicators']:
            for indicator in status['dependency_risk']['indicators']:
                print(f"  - {indicator}")
        print("="*50)


def main():
    print("="*60)
    print("PERSONALITY ARCHITECT v2.0 - Stateful Companion")
    print("="*60)
    
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("\nError: OPENAI_API_KEY environment variable not set")
        print("Set it with: export OPENAI_API_KEY='your-key'")
        return
    
    loader = PersonaLoader()
    available = loader.list_personas()
    
    if not available:
        print("\nNo personas found in the personas/ directory")
        return
    
    print("\nAvailable Personas:")
    for i, p in enumerate(available, 1):
        print(f"  {i}. {p['name']} ({p['category']})")
    
    choice = input("\nSelect persona (number or name): ").strip()
    
    try:
        idx = int(choice) - 1
        persona_name = available[idx]['name']
    except ValueError:
        persona_name = choice
    
    user_id = input("Enter your name/ID: ").strip() or "demo_user"
    
    enable_voice = os.environ.get("ELEVEN_API_KEY") is not None
    if enable_voice:
        voice_choice = input("Enable voice responses? (yes/no): ").strip().lower()
        enable_voice = voice_choice in ['yes', 'y']
    
    print(f"\nInitializing {persona_name}...")
    
    try:
        companion = StatefulCompanion(
            persona_name=persona_name,
            user_id=user_id,
            llm_provider=LLMProvider.OPENAI,
            enable_voice=enable_voice,
        )
    except Exception as e:
        print(f"Error initializing companion: {e}")
        return
    
    companion.setup_consent()
    
    print("\n" + "="*60)
    print(f"Chatting with {companion.persona.name}")
    print("Commands:")
    print("  /status  - Show companion status")
    print("  /remember <key> <value> - Store a memory")
    print("  /recall <key> - Recall a memory")
    print("  /clear   - Clear conversation")
    print("  /quit    - Exit")
    print("="*60 + "\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break
        
        if not user_input:
            continue
        
        if user_input.startswith('/'):
            parts = user_input[1:].split(maxsplit=2)
            cmd = parts[0].lower()
            
            if cmd == 'quit':
                print("Goodbye!")
                break
            elif cmd == 'status':
                companion.show_status()
            elif cmd == 'clear':
                companion.runtime.clear_history()
                print("[Conversation cleared]")
            elif cmd == 'remember' and len(parts) >= 3:
                companion.remember(parts[1], parts[2])
            elif cmd == 'recall' and len(parts) >= 2:
                value = companion.recall(parts[1])
                if value:
                    print(f"[{parts[1]}: {value}]")
                else:
                    print(f"[No memory found for: {parts[1]}]")
            else:
                print("[Unknown command]")
            continue
        
        result = companion.process_message(user_input)
        
        print(f"\n{companion.persona.name}: {result['content']}")
        
        status_info = []
        if result['state_changed']:
            status_info.append(f"State: {result['state']}")
        if result['drift'] != 'none':
            status_info.append(f"Drift: {result['drift']}")
        if result['coherence'] != 'GOOD':
            status_info.append(f"Coherence: {result['coherence']}")
        
        if status_info:
            print(f"[{' | '.join(status_info)}]")
        
        print()


if __name__ == "__main__":
    main()
