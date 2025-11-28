"""
PERSONALITY ARCHITECT v2.0 - Multimodal Assets Module
Voice synthesis and avatar integration

Supports:
- ElevenLabs text-to-speech
- Voice profile management
- Emotional expression mapping
- Avatar asset specifications

Author: Sheldon K. Salmon (Mr. AION)
License: MIT
"""

import os
import json
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Tuple
from pathlib import Path

from .persona_loader import PersonaCard


class VoicePitch(Enum):
    """Voice pitch levels."""
    VERY_LOW = "very_low"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    VERY_HIGH = "very_high"


class VoiceSpeed(Enum):
    """Voice speed levels."""
    VERY_SLOW = "very_slow"
    SLOW = "slow"
    MODERATE = "moderate"
    FAST = "fast"
    VERY_FAST = "very_fast"


class ToneColor(Enum):
    """Voice tone color."""
    WARM = "warm"
    NEUTRAL = "neutral"
    BRIGHT = "bright"
    DEEP = "deep"
    SOFT = "soft"


class EmotionalState(Enum):
    """Emotional states for expression mapping."""
    NEUTRAL = "neutral"
    HAPPY = "happy"
    EXCITED = "excited"
    THOUGHTFUL = "thoughtful"
    CONCERNED = "concerned"
    ENCOURAGING = "encouraging"
    SERIOUS = "serious"
    PLAYFUL = "playful"


@dataclass
class VoiceProfile:
    """Voice synthesis profile for a persona."""
    
    voice_id: str = ""
    provider: str = "elevenlabs"
    pitch: VoicePitch = VoicePitch.MEDIUM
    speed: VoiceSpeed = VoiceSpeed.MODERATE
    tone_color: ToneColor = ToneColor.NEUTRAL
    accent: str = "neutral"
    stability: float = 0.5
    similarity_boost: float = 0.75
    style: float = 0.0
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "VoiceProfile":
        """Create a VoiceProfile from a dictionary."""
        return cls(
            voice_id=data.get("voice_id", ""),
            provider=data.get("provider", "elevenlabs"),
            pitch=VoicePitch(data.get("pitch", "medium").lower()),
            speed=VoiceSpeed(data.get("speed", "moderate").lower()),
            tone_color=ToneColor(data.get("tone_color", "neutral").lower()),
            accent=data.get("accent", "neutral"),
            stability=data.get("stability", 0.5),
            similarity_boost=data.get("similarity_boost", 0.75),
            style=data.get("style", 0.0),
        )
    
    def to_elevenlabs_settings(self) -> Dict[str, Any]:
        """Convert to ElevenLabs voice settings."""
        return {
            "stability": self.stability,
            "similarity_boost": self.similarity_boost,
            "style": self.style,
            "use_speaker_boost": True,
        }


@dataclass
class EmotionalExpression:
    """Mapping of emotional states to voice/visual modifiers."""
    
    state: EmotionalState
    voice_modifiers: Dict[str, float] = field(default_factory=dict)
    visual_cues: List[str] = field(default_factory=list)
    ssml_tags: str = ""
    
    @classmethod
    def default_expressions(cls) -> Dict[EmotionalState, "EmotionalExpression"]:
        """Get default emotional expressions."""
        return {
            EmotionalState.NEUTRAL: cls(
                state=EmotionalState.NEUTRAL,
                voice_modifiers={"pitch": 0, "speed": 0, "volume": 0},
                visual_cues=["relaxed posture", "neutral expression"],
            ),
            EmotionalState.HAPPY: cls(
                state=EmotionalState.HAPPY,
                voice_modifiers={"pitch": 0.1, "speed": 0.05, "volume": 0.05},
                visual_cues=["smile", "bright eyes", "open posture"],
                ssml_tags='<prosody rate="105%" pitch="+5%">',
            ),
            EmotionalState.EXCITED: cls(
                state=EmotionalState.EXCITED,
                voice_modifiers={"pitch": 0.15, "speed": 0.1, "volume": 0.1},
                visual_cues=["wide smile", "animated gestures", "leaning forward"],
                ssml_tags='<prosody rate="115%" pitch="+10%">',
            ),
            EmotionalState.THOUGHTFUL: cls(
                state=EmotionalState.THOUGHTFUL,
                voice_modifiers={"pitch": -0.05, "speed": -0.1, "volume": -0.05},
                visual_cues=["slight head tilt", "contemplative expression", "slower blinks"],
                ssml_tags='<prosody rate="90%" pitch="-3%">',
            ),
            EmotionalState.CONCERNED: cls(
                state=EmotionalState.CONCERNED,
                voice_modifiers={"pitch": -0.05, "speed": -0.05, "volume": -0.05},
                visual_cues=["furrowed brow", "leaning in", "soft eyes"],
                ssml_tags='<prosody rate="95%" pitch="-2%">',
            ),
            EmotionalState.ENCOURAGING: cls(
                state=EmotionalState.ENCOURAGING,
                voice_modifiers={"pitch": 0.05, "speed": 0, "volume": 0.05},
                visual_cues=["warm smile", "nodding", "open gestures"],
                ssml_tags='<prosody rate="100%" pitch="+3%">',
            ),
            EmotionalState.SERIOUS: cls(
                state=EmotionalState.SERIOUS,
                voice_modifiers={"pitch": -0.1, "speed": -0.05, "volume": 0},
                visual_cues=["steady gaze", "still posture", "measured expression"],
                ssml_tags='<prosody rate="95%" pitch="-5%">',
            ),
            EmotionalState.PLAYFUL: cls(
                state=EmotionalState.PLAYFUL,
                voice_modifiers={"pitch": 0.1, "speed": 0.05, "volume": 0.05},
                visual_cues=["grin", "raised eyebrow", "playful gestures"],
                ssml_tags='<prosody rate="105%" pitch="+5%">',
            ),
        }


@dataclass
class AvatarSpec:
    """Specification for a persona's visual avatar."""
    
    style: str = "realistic"
    description: str = ""
    primary_colors: List[str] = field(default_factory=list)
    accessories: List[str] = field(default_factory=list)
    background: str = "neutral"
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AvatarSpec":
        """Create an AvatarSpec from a dictionary."""
        return cls(
            style=data.get("style", "realistic"),
            description=data.get("description", ""),
            primary_colors=data.get("primary_colors", []),
            accessories=data.get("accessories", []),
            background=data.get("background", "neutral"),
        )


class MultimodalAssets:
    """
    Multimodal asset manager for personas.
    
    Handles voice synthesis, avatar specifications, and emotional expressions.
    
    Usage:
        from integrations import PersonaLoader, MultimodalAssets
        
        loader = PersonaLoader()
        persona = loader.load_by_name("Tesla")
        
        assets = MultimodalAssets(persona)
        
        # Get voice profile
        voice = assets.get_voice_profile()
        
        # Generate speech (requires ElevenLabs API key)
        audio = assets.text_to_speech("Imagination is the beginning of creation.")
        
        # Get emotional expression modifiers
        expression = assets.get_expression(EmotionalState.EXCITED)
    """
    
    def __init__(
        self,
        persona: PersonaCard,
        elevenlabs_api_key: Optional[str] = None,
    ):
        self.persona = persona
        self.elevenlabs_api_key = elevenlabs_api_key or os.environ.get("ELEVEN_API_KEY")
        
        self.voice_profile = self._load_voice_profile()
        self.avatar_spec = self._load_avatar_spec()
        self.expressions = EmotionalExpression.default_expressions()
        
        self._load_custom_expressions()
        
        self._elevenlabs_client = None
    
    def _load_voice_profile(self) -> VoiceProfile:
        """Load voice profile from persona card."""
        assets = self.persona.multimodal_assets
        voice_data = assets.get("voice_profile", {})
        
        if voice_data:
            return VoiceProfile.from_dict(voice_data)
        
        voice_sig = self.persona.voice_signature
        warmth = voice_sig.get("warmth", 5)
        formality = voice_sig.get("formality", 5)
        
        if warmth >= 7:
            tone = ToneColor.WARM
        elif warmth <= 3:
            tone = ToneColor.NEUTRAL
        else:
            tone = ToneColor.NEUTRAL
        
        if formality >= 7:
            speed = VoiceSpeed.SLOW
        elif formality <= 3:
            speed = VoiceSpeed.FAST
        else:
            speed = VoiceSpeed.MODERATE
        
        return VoiceProfile(
            tone_color=tone,
            speed=speed,
        )
    
    def _load_avatar_spec(self) -> AvatarSpec:
        """Load avatar specification from persona card."""
        assets = self.persona.multimodal_assets
        avatar_data = assets.get("avatar_brief", assets.get("avatar", {}))
        
        if avatar_data:
            return AvatarSpec.from_dict(avatar_data)
        
        return AvatarSpec(description=f"Avatar for {self.persona.name}")
    
    def _load_custom_expressions(self):
        """Load custom emotional expressions from persona card."""
        assets = self.persona.multimodal_assets
        custom = assets.get("emotional_expressions", assets.get("expressions", []))
        
        for expr_data in custom:
            state_name = expr_data.get("state", "").upper()
            try:
                state = EmotionalState(state_name.lower())
                self.expressions[state] = EmotionalExpression(
                    state=state,
                    voice_modifiers=expr_data.get("voice_modifiers", {}),
                    visual_cues=expr_data.get("visual_cues", []),
                    ssml_tags=expr_data.get("ssml_tags", ""),
                )
            except ValueError:
                pass
    
    def get_voice_profile(self) -> VoiceProfile:
        """Get the voice profile for this persona."""
        return self.voice_profile
    
    def get_avatar_spec(self) -> AvatarSpec:
        """Get the avatar specification for this persona."""
        return self.avatar_spec
    
    def get_expression(self, state: EmotionalState) -> EmotionalExpression:
        """Get the emotional expression for a given state."""
        return self.expressions.get(state, self.expressions[EmotionalState.NEUTRAL])
    
    def _get_elevenlabs_client(self):
        """Lazily initialize the ElevenLabs client."""
        if self._elevenlabs_client is None:
            if not self.elevenlabs_api_key:
                raise ValueError("ElevenLabs API key required. Set ELEVEN_API_KEY environment variable.")
            
            try:
                from elevenlabs.client import ElevenLabs
                self._elevenlabs_client = ElevenLabs(api_key=self.elevenlabs_api_key)
            except ImportError:
                raise ImportError("elevenlabs package required. Install with: pip install elevenlabs")
        
        return self._elevenlabs_client
    
    def text_to_speech(
        self,
        text: str,
        emotional_state: EmotionalState = EmotionalState.NEUTRAL,
        output_format: str = "mp3_44100_128",
    ) -> bytes:
        """
        Convert text to speech using the persona's voice profile.
        
        Args:
            text: The text to convert
            emotional_state: The emotional state to apply
            output_format: Audio output format
            
        Returns:
            Audio bytes
        """
        
        client = self._get_elevenlabs_client()
        
        voice_id = self.voice_profile.voice_id
        if not voice_id:
            voice_id = "JBFqnCBsd6RMkjVDRZzb"
        
        expression = self.get_expression(emotional_state)
        if expression.ssml_tags:
            text = f"{expression.ssml_tags}{text}</prosody>"
        
        audio = client.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id="eleven_multilingual_v2",
            output_format=output_format,
            voice_settings=self.voice_profile.to_elevenlabs_settings(),
        )
        
        audio_bytes = b""
        for chunk in audio:
            if chunk:
                audio_bytes += chunk
        
        return audio_bytes
    
    def text_to_speech_stream(
        self,
        text: str,
        emotional_state: EmotionalState = EmotionalState.NEUTRAL,
    ):
        """
        Stream text to speech for real-time playback.
        
        Args:
            text: The text to convert
            emotional_state: The emotional state to apply
            
        Yields:
            Audio chunks
        """
        
        client = self._get_elevenlabs_client()
        
        voice_id = self.voice_profile.voice_id
        if not voice_id:
            voice_id = "JBFqnCBsd6RMkjVDRZzb"
        
        audio_stream = client.text_to_speech.stream(
            text=text,
            voice_id=voice_id,
            model_id="eleven_multilingual_v2",
            voice_settings=self.voice_profile.to_elevenlabs_settings(),
        )
        
        for chunk in audio_stream:
            if isinstance(chunk, bytes):
                yield chunk
    
    def save_speech(
        self,
        text: str,
        output_path: str,
        emotional_state: EmotionalState = EmotionalState.NEUTRAL,
    ) -> str:
        """
        Generate speech and save to a file.
        
        Args:
            text: The text to convert
            output_path: Path to save the audio file
            emotional_state: The emotional state to apply
            
        Returns:
            The output file path
        """
        
        audio_bytes = self.text_to_speech(text, emotional_state)
        
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(path, "wb") as f:
            f.write(audio_bytes)
        
        return str(path)
    
    def list_available_voices(self) -> List[Dict[str, str]]:
        """List available voices from ElevenLabs."""
        
        client = self._get_elevenlabs_client()
        
        response = client.voices.get_all()
        
        voices = []
        for voice in response.voices:
            voices.append({
                "voice_id": voice.voice_id,
                "name": voice.name,
                "category": voice.category or "unknown",
            })
        
        return voices
    
    def detect_emotional_state(self, text: str) -> EmotionalState:
        """
        Detect the appropriate emotional state from text content.
        
        This is a simple rule-based detector. For production use,
        consider integrating a sentiment analysis model.
        """
        
        text_lower = text.lower()
        
        excited_words = ["amazing", "incredible", "wonderful", "fantastic", "brilliant", "!"]
        happy_words = ["glad", "happy", "pleased", "delighted", "joy", "love"]
        concerned_words = ["worried", "concerned", "sorry", "unfortunately", "difficult"]
        thoughtful_words = ["consider", "perhaps", "think", "wonder", "reflect", "hmm"]
        encouraging_words = ["great", "well done", "excellent", "proud", "impressive", "keep"]
        serious_words = ["important", "critical", "serious", "must", "essential", "warning"]
        playful_words = ["haha", "fun", "joke", "silly", "imagine", "what if"]
        
        if any(word in text_lower for word in excited_words):
            return EmotionalState.EXCITED
        elif any(word in text_lower for word in happy_words):
            return EmotionalState.HAPPY
        elif any(word in text_lower for word in concerned_words):
            return EmotionalState.CONCERNED
        elif any(word in text_lower for word in encouraging_words):
            return EmotionalState.ENCOURAGING
        elif any(word in text_lower for word in serious_words):
            return EmotionalState.SERIOUS
        elif any(word in text_lower for word in playful_words):
            return EmotionalState.PLAYFUL
        elif any(word in text_lower for word in thoughtful_words):
            return EmotionalState.THOUGHTFUL
        
        return EmotionalState.NEUTRAL
    
    def get_generation_prompt(self) -> str:
        """Get a prompt for generating an avatar image."""
        
        spec = self.avatar_spec
        persona_name = self.persona.name
        archetype = self.persona.identity.get("archetype", "")
        
        colors = ", ".join(spec.primary_colors) if spec.primary_colors else "natural colors"
        accessories = ", ".join(spec.accessories) if spec.accessories else "no specific accessories"
        
        return f"""Generate a {spec.style} avatar for a persona named "{persona_name}".

Character Description: {spec.description or archetype}
Style: {spec.style}
Color Palette: {colors}
Accessories: {accessories}
Background: {spec.background}

The avatar should convey professionalism and approachability while matching the persona's character."""
    
    def export_asset_pack(self) -> Dict[str, Any]:
        """Export all multimodal asset specifications."""
        
        return {
            "persona_name": self.persona.name,
            "voice_profile": {
                "voice_id": self.voice_profile.voice_id,
                "provider": self.voice_profile.provider,
                "pitch": self.voice_profile.pitch.value,
                "speed": self.voice_profile.speed.value,
                "tone_color": self.voice_profile.tone_color.value,
                "accent": self.voice_profile.accent,
                "settings": self.voice_profile.to_elevenlabs_settings(),
            },
            "avatar": {
                "style": self.avatar_spec.style,
                "description": self.avatar_spec.description,
                "primary_colors": self.avatar_spec.primary_colors,
                "accessories": self.avatar_spec.accessories,
                "background": self.avatar_spec.background,
                "generation_prompt": self.get_generation_prompt(),
            },
            "expressions": {
                state.value: {
                    "voice_modifiers": expr.voice_modifiers,
                    "visual_cues": expr.visual_cues,
                    "ssml_tags": expr.ssml_tags,
                }
                for state, expr in self.expressions.items()
            },
        }


if __name__ == "__main__":
    print("Multimodal Assets Module")
    print("=" * 50)
    print()
    print("Usage:")
    print("  from integrations import PersonaLoader, MultimodalAssets")
    print()
    print("  loader = PersonaLoader()")
    print("  persona = loader.load_by_name('Tesla')")
    print("  assets = MultimodalAssets(persona)")
    print()
    print("  # Get voice profile")
    print("  voice = assets.get_voice_profile()")
    print()
    print("  # Generate speech (requires ELEVEN_API_KEY)")
    print("  audio = assets.text_to_speech('Hello world')")
    print("  assets.save_speech('Hello', 'output.mp3')")
