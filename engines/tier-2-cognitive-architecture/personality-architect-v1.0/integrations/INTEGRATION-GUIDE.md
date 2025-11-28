# Personality Architect v2.0 - Integration Guide

**Enterprise-Grade API Integrations for Persona Deployment**

This guide provides comprehensive documentation for integrating Personality Architect personas with LLM APIs, voice synthesis, and multimodal systems.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [LLM Runtime Integration](#llm-runtime-integration)
4. [Dynamic Identity Orchestrator (DIO)](#dynamic-identity-orchestrator)
5. [Continuity & Resonance Matrix (CRM)](#continuity-resonance-matrix)
6. [Multimodal Assets](#multimodal-assets)
7. [Complete Example: Building a Persona Chatbot](#complete-example)
8. [API Reference](#api-reference)
9. [Best Practices](#best-practices)

---

## Quick Start

```python
from integrations import PersonaLoader, LLMRuntime, LLMProvider

# Load a persona
loader = PersonaLoader()
persona = loader.load_by_name("Tesla")

# Deploy to OpenAI
runtime = LLMRuntime(
    persona=persona,
    provider=LLMProvider.OPENAI,
    api_key="your-openai-api-key"
)

# Chat in character
response = runtime.chat("What inspired your work on alternating current?")
print(response.content)
```

---

## Installation

### Required Dependencies

```bash
# Core requirements (for LLM integration)
pip install pyyaml

# For OpenAI integration
pip install openai

# For Anthropic Claude integration
pip install anthropic

# For voice synthesis (ElevenLabs)
pip install elevenlabs
```

### Environment Variables

Set up your API keys:

```bash
# OpenAI
export OPENAI_API_KEY="sk-..."

# Anthropic Claude
export ANTHROPIC_API_KEY="sk-ant-..."

# ElevenLabs (for voice)
export ELEVEN_API_KEY="..."
```

---

## LLM Runtime Integration

The `LLMRuntime` class deploys personas to LLM APIs, handling system prompt generation and conversation management.

### Supported Providers

| Provider | LLMProvider Value | Default Model |
|----------|-------------------|---------------|
| OpenAI | `LLMProvider.OPENAI` | gpt-4o |
| Anthropic | `LLMProvider.ANTHROPIC` | claude-3-5-sonnet-20241022 |
| Custom | `LLMProvider.CUSTOM` | Configurable |

### Basic Usage

```python
from integrations import PersonaLoader, LLMRuntime, LLMProvider

# Load persona
loader = PersonaLoader()
persona = loader.load_by_name("Executive Coach")

# Create runtime with OpenAI
runtime = LLMRuntime(
    persona=persona,
    provider=LLMProvider.OPENAI,
    api_key="your-api-key",
    model="gpt-4o",  # Optional: specify model
)

# Single message
response = runtime.chat("I'm struggling with delegation")
print(response.content)

# Continue conversation (history is maintained)
response = runtime.chat("What about with remote teams?")
print(response.content)

# Clear history for new conversation
runtime.clear_history()
```

### Streaming Responses

```python
# Stream tokens as they're generated
for token in runtime.stream_chat("Tell me about leadership"):
    print(token, end="", flush=True)
```

### Using Anthropic Claude

```python
runtime = LLMRuntime(
    persona=persona,
    provider=LLMProvider.ANTHROPIC,
    api_key="your-anthropic-key",
    model="claude-3-5-sonnet-20241022"
)

response = runtime.chat("What's your coaching philosophy?")
```

### Custom/Self-Hosted LLMs

```python
# For any OpenAI-compatible API
runtime = LLMRuntime(
    persona=persona,
    provider=LLMProvider.CUSTOM,
    api_key="your-key",
    base_url="https://your-llm-endpoint.com/v1",
    model="your-model-name"
)
```

### Coherence Checking

```python
response = runtime.chat("Tell me about innovation")

# Check if the response maintains persona coherence
coherence = runtime.run_coherence_check(response.content)
print(f"Vocabulary Score: {coherence['vocabulary_score']}")
print(f"Status: {coherence['coherence_status']}")  # GOOD, CHECK, or DRIFT_DETECTED
```

---

## Dynamic Identity Orchestrator

The DIO manages runtime state transitions, allowing personas to adapt their behavior based on conversation context.

### State Machine Basics

```python
from integrations import PersonaLoader, DIORuntime

loader = PersonaLoader()
persona = loader.load_by_name("Supportive Listener")

# Initialize DIO
dio = DIORuntime(persona)

# See available states
print(dio.get_available_states())
# ['LISTEN', 'ENGAGE', 'SUPPORT', 'CRISIS']

# Analyze input for state changes
new_state, rationale = dio.analyze_input("I'm feeling really overwhelmed lately")
if new_state:
    print(f"Recommended transition: {new_state}")
    print(f"Reason: {rationale}")
    dio.transition_to(new_state)

# Get current state modifiers for prompting
modifiers = dio.get_current_modifiers()
print(modifiers)
```

### Integrating DIO with LLM Runtime

```python
from integrations import PersonaLoader, LLMRuntime, DIORuntime, LLMProvider

loader = PersonaLoader()
persona = loader.load_by_name("Executive Coach")

# Create runtime with initial state
runtime = LLMRuntime(
    persona=persona,
    provider=LLMProvider.OPENAI,
    api_key="your-key",
    current_state="COACHING"  # Start in coaching state
)

# Create DIO for state management
dio = DIORuntime(persona, initial_state="COACHING")

# Chat loop with state awareness
user_input = "I'm frustrated with my team's performance"

# Check for state transition
new_state, rationale = dio.analyze_input(user_input)
if new_state:
    dio.transition_to(new_state)
    runtime.set_state(new_state)  # Update runtime's state

# Get response
response = runtime.chat(user_input)
print(response.content)

# Check for drift in the response
drift_report = dio.detect_drift(response.content)
if drift_report.severity.value != "none":
    print(f"Warning: {drift_report.dimension} drift detected")
    print(f"Correction: {drift_report.correction_actions}")
```

### Analyzing Conversation History

```python
from integrations import run_dio_analysis

# Analyze an existing conversation
conversation = [
    {"role": "user", "content": "I need help with my anxiety"},
    {"role": "assistant", "content": "I hear you. Tell me more about what you're experiencing."},
    {"role": "user", "content": "I can't sleep and I feel panicked"},
    {"role": "assistant", "content": "That sounds really challenging..."},
]

analysis = run_dio_analysis(persona, conversation)
print(f"Final State: {analysis['final_state']}")
print(f"Transitions: {analysis['transitions']}")
print(f"Drift Status: {analysis['drift_summary']['status']}")
```

---

## Continuity & Resonance Matrix

The CRM manages memory, consent, and relationship tracking for persona-user interactions.

### Memory Management

```python
from integrations import PersonaLoader, CRMManager

loader = PersonaLoader()
persona = loader.load_by_name("Supportive Listener")

# Initialize CRM for a specific user
crm = CRMManager(
    persona=persona,
    user_id="user_12345",
    jurisdiction="US"  # Affects data retention policies
)

# Request and grant consent for persistent memory
consent_text = crm.request_consent()
print(f"Consent Request: {consent_text}")
crm.grant_consent()  # User clicks "Yes"

# Store memories
crm.remember("user_name", "Alice", category="profile")
crm.remember("preferred_topic", "stress management", category="preferences")
crm.remember("last_mood", "anxious", category="context")

# Recall memories
name = crm.recall("user_name")  # Returns "Alice"
all_prefs = crm.recall_category("preferences")  # Returns dict of preferences

# Get context summary for LLM prompting
context = crm.get_context_summary()
print(context)
# User Profile:
#   - user_name: Alice
# User Preferences:
#   - preferred_topic: stress management
# Relationship Stage: development (5 interactions)
```

### Relationship Tracking

```python
# Log each interaction
crm.log_interaction()

# Check relationship stage
stage = crm.get_relationship_stage()
print(f"Stage: {stage['stage']}")  # introduction, development, established
print(f"Interactions: {stage['interaction_count']}")
print(f"Sessions: {stage['session_count']}")
```

### Resonance Scoring

```python
# Update resonance based on interaction patterns
crm.update_resonance(
    response_length=150,      # Average message length
    user_response_time=30.0,  # Seconds between messages
    emotional_words=5,        # Count of emotional language
    topic_depth=7             # Estimated depth (1-10)
)

# Get resonance report
report = crm.get_resonance_report()
print(f"Overall Score: {report['scores']['overall']}")
print(f"Assessment: {report['assessment']}")
print(f"Recommendations: {report['recommendations']}")
```

### Dependency Risk Detection

```python
# Assess risk of unhealthy dependency
risk = crm.assess_dependency_risk()
print(f"Risk Level: {risk['risk_level']}")  # LOW, MODERATE, HIGH
print(f"Indicators: {risk['indicators']}")
print(f"Interventions: {risk['recommended_interventions']}")
```

### Data Privacy (GDPR Compliance)

```python
# User withdraws consent - deletes persistent data
crm.withdraw_consent()

# User requests data deletion
crm.forget_all()

# User requests data export
export = crm.export_user_data()
# Returns all stored data in portable format
```

---

## Multimodal Assets

The multimodal module handles voice synthesis via ElevenLabs and avatar specifications.

### Voice Profile

```python
from integrations import PersonaLoader, MultimodalAssets

loader = PersonaLoader()
persona = loader.load_by_name("Tesla")

# Initialize with ElevenLabs API key
assets = MultimodalAssets(
    persona=persona,
    elevenlabs_api_key="your-eleven-api-key"  # Or use ELEVEN_API_KEY env var
)

# Get voice profile
voice = assets.get_voice_profile()
print(f"Pitch: {voice.pitch.value}")
print(f"Speed: {voice.speed.value}")
print(f"Tone: {voice.tone_color.value}")
```

### Text-to-Speech

```python
# Generate speech
audio_bytes = assets.text_to_speech(
    text="Imagination is the beginning of creation.",
    emotional_state=EmotionalState.THOUGHTFUL
)

# Save to file
assets.save_speech(
    text="The present is theirs; the future is mine.",
    output_path="tesla_quote.mp3",
    emotional_state=EmotionalState.SERIOUS
)

# Stream for real-time playback
for chunk in assets.text_to_speech_stream("Hello, I am Nikola Tesla"):
    # Process audio chunks in real-time
    audio_player.play(chunk)
```

### Emotional Expressions

```python
from integrations import EmotionalState

# Get expression modifiers for emotional state
expression = assets.get_expression(EmotionalState.EXCITED)
print(f"Voice Modifiers: {expression.voice_modifiers}")
print(f"Visual Cues: {expression.visual_cues}")

# Automatic emotion detection
text = "This is absolutely amazing! I'm thrilled!"
detected_state = assets.detect_emotional_state(text)
print(f"Detected Emotion: {detected_state.value}")  # "excited"

# Generate speech with detected emotion
audio = assets.text_to_speech(text, emotional_state=detected_state)
```

### Avatar Generation

```python
# Get avatar specification
avatar = assets.get_avatar_spec()
print(f"Style: {avatar.style}")
print(f"Colors: {avatar.primary_colors}")

# Get prompt for image generation
prompt = assets.get_generation_prompt()
# Use with DALL-E, Midjourney, or other image generators
```

### Listing Available Voices

```python
# List all ElevenLabs voices
voices = assets.list_available_voices()
for voice in voices:
    print(f"{voice['name']} ({voice['voice_id']})")
```

---

## Complete Example

Here's a complete example building a persona-powered chatbot with all features:

```python
"""
Complete Persona Chatbot Example
Uses LLM Runtime + DIO + CRM + Voice
"""

import os
from integrations import (
    PersonaLoader,
    LLMRuntime,
    LLMProvider,
    DIORuntime,
    CRMManager,
    MultimodalAssets,
    EmotionalState,
)

class PersonaChatbot:
    def __init__(
        self,
        persona_name: str,
        user_id: str,
        openai_key: str,
        elevenlabs_key: str = None,
    ):
        # Load persona
        loader = PersonaLoader()
        self.persona = loader.load_by_name(persona_name)
        
        # Initialize components
        self.runtime = LLMRuntime(
            persona=self.persona,
            provider=LLMProvider.OPENAI,
            api_key=openai_key,
        )
        
        self.dio = DIORuntime(self.persona)
        self.crm = CRMManager(self.persona, user_id=user_id)
        
        if elevenlabs_key:
            self.assets = MultimodalAssets(
                self.persona,
                elevenlabs_api_key=elevenlabs_key
            )
        else:
            self.assets = None
        
        # Request consent on first use
        print(f"Consent: {self.crm.request_consent()}")
    
    def set_consent(self, granted: bool):
        if granted:
            self.crm.grant_consent()
        else:
            self.crm.deny_consent()
    
    def chat(self, user_message: str, with_voice: bool = False):
        # Log interaction
        self.crm.log_interaction()
        
        # Check for state transition
        new_state, rationale = self.dio.analyze_input(user_message)
        if new_state:
            self.dio.transition_to(new_state)
            self.runtime.set_state(new_state)
        
        # Add memory context to system prompt
        context = self.crm.get_context_summary()
        
        # Get response
        response = self.runtime.chat(user_message)
        
        # Check for drift
        drift = self.dio.detect_drift(response.content)
        if drift.severity.value not in ["none", "minor"]:
            print(f"[Drift Warning: {drift.dimension}]")
        
        # Generate voice if requested
        audio = None
        if with_voice and self.assets:
            emotion = self.assets.detect_emotional_state(response.content)
            audio = self.assets.text_to_speech(response.content, emotion)
        
        return {
            "text": response.content,
            "state": self.dio.get_current_state_name(),
            "audio": audio,
        }
    
    def remember(self, key: str, value: str, category: str = "context"):
        return self.crm.remember(key, value, category=category)
    
    def get_status(self):
        return {
            "persona": self.persona.name,
            "state": self.dio.get_current_state_name(),
            "relationship": self.crm.get_relationship_stage(),
            "resonance": self.crm.get_resonance_report(),
            "dependency_risk": self.crm.assess_dependency_risk(),
        }


# Usage
if __name__ == "__main__":
    bot = PersonaChatbot(
        persona_name="Executive Coach",
        user_id="demo_user",
        openai_key=os.environ["OPENAI_API_KEY"],
        elevenlabs_key=os.environ.get("ELEVEN_API_KEY"),
    )
    
    bot.set_consent(True)
    bot.remember("user_name", "Demo User", category="profile")
    
    # Chat loop
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        
        result = bot.chat(user_input)
        print(f"\n{bot.persona.name}: {result['text']}\n")
        print(f"[State: {result['state']}]")
```

---

## API Reference

### PersonaLoader

| Method | Description |
|--------|-------------|
| `load(filepath)` | Load persona from YAML file |
| `load_by_name(name, category)` | Load by name, optionally filter by category |
| `list_personas(category)` | List all available personas |

### LLMRuntime

| Method | Description |
|--------|-------------|
| `chat(message)` | Send message, get response |
| `stream_chat(message)` | Stream response tokens |
| `set_state(state_name)` | Set DIO state |
| `clear_history()` | Clear conversation history |
| `run_coherence_check(response)` | Check response coherence |

### DIORuntime

| Method | Description |
|--------|-------------|
| `analyze_input(text)` | Analyze for state transitions |
| `transition_to(state)` | Transition to new state |
| `detect_drift(response)` | Detect persona drift |
| `get_current_modifiers()` | Get state voice modifiers |

### CRMManager

| Method | Description |
|--------|-------------|
| `remember(key, value, category)` | Store memory |
| `recall(key)` | Retrieve memory |
| `forget(key)` | Delete memory |
| `log_interaction()` | Log interaction for tracking |
| `get_relationship_stage()` | Get relationship info |
| `assess_dependency_risk()` | Check dependency indicators |

### MultimodalAssets

| Method | Description |
|--------|-------------|
| `text_to_speech(text, emotion)` | Generate speech audio |
| `save_speech(text, path, emotion)` | Save speech to file |
| `get_voice_profile()` | Get voice settings |
| `detect_emotional_state(text)` | Detect emotion from text |

---

## Best Practices

### 1. Always Check Coherence

```python
response = runtime.chat(user_input)
coherence = runtime.run_coherence_check(response.content)

if coherence['coherence_status'] == 'DRIFT_DETECTED':
    # Consider regenerating or adjusting
    pass
```

### 2. Use State Transitions Thoughtfully

Don't over-transition. Let conversations develop naturally. Only trigger state changes for significant emotional or contextual shifts.

### 3. Respect User Privacy

```python
# Always request consent before persistent storage
crm.request_consent()

# Honor withdrawal requests immediately
crm.withdraw_consent()

# Apply redaction for sensitive data
crm.remember("note", "Email is user@example.com")  # Auto-redacted to [EMAIL]
```

### 4. Monitor Dependency Risk

```python
risk = crm.assess_dependency_risk()
if risk['risk_level'] == 'HIGH':
    # Implement intervention
    for action in risk['recommended_interventions']:
        print(f"Recommended: {action}")
```

### 5. Match Voice to Emotion

```python
# Detect emotion from LLM response
emotion = assets.detect_emotional_state(response.content)

# Generate voice with matching emotion
audio = assets.text_to_speech(response.content, emotional_state=emotion)
```

---

## Support

For questions or issues:
- GitHub: [AION-BRAIN Repository]
- Documentation: [Full Engine Documentation]

**Author:** Sheldon K. Salmon (Mr. AION)  
**Version:** 2.0.0  
**License:** MIT
