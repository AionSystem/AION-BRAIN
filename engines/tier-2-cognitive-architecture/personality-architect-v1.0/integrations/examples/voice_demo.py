#!/usr/bin/env python3
"""
PERSONALITY ARCHITECT v2.0 - Voice Demo

This example demonstrates voice synthesis capabilities using ElevenLabs.
It generates speech for a persona with emotional expression.

Requirements:
    pip install elevenlabs pyyaml

Usage:
    export ELEVEN_API_KEY="your-key"
    python voice_demo.py
"""

import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from persona_loader import PersonaLoader
from multimodal import MultimodalAssets, EmotionalState


def main():
    eleven_key = os.environ.get("ELEVEN_API_KEY")
    if not eleven_key:
        print("Error: ELEVEN_API_KEY environment variable not set")
        print("Set it with: export ELEVEN_API_KEY='your-key'")
        print("\nGet your API key at: https://elevenlabs.io/")
        return
    
    print("="*60)
    print("PERSONALITY ARCHITECT v2.0 - Voice Demo")
    print("="*60)
    
    loader = PersonaLoader()
    available = loader.list_personas()
    
    if not available:
        print("\nNo personas found. Creating demo with default settings.")
        from persona_loader import PersonaCard
        persona = PersonaCard(
            name="Demo Persona",
            version="2.0",
            classification="demo",
        )
    else:
        print("\nAvailable Personas:")
        for i, p in enumerate(available, 1):
            print(f"  {i}. {p['name']} ({p['category']})")
        
        choice = input("\nSelect persona (number): ").strip()
        try:
            idx = int(choice) - 1
            persona_info = available[idx]
        except (ValueError, IndexError):
            persona_info = available[0]
        
        persona = loader.load(persona_info['file'])
    
    print(f"\nLoaded: {persona.name}")
    
    assets = MultimodalAssets(
        persona=persona,
        elevenlabs_api_key=eleven_key
    )
    
    voice = assets.get_voice_profile()
    print(f"\nVoice Profile:")
    print(f"  Pitch: {voice.pitch.value}")
    print(f"  Speed: {voice.speed.value}")
    print(f"  Tone: {voice.tone_color.value}")
    print(f"  Voice ID: {voice.voice_id or 'default'}")
    
    print("\nAvailable Emotional States:")
    for state in EmotionalState:
        expr = assets.get_expression(state)
        print(f"  - {state.value}: {', '.join(expr.visual_cues[:2])}")
    
    print("\n" + "="*60)
    print("Enter text to convert to speech.")
    print("Prefix with emotion tag for different expressions:")
    print("  [happy] Your text here")
    print("  [excited] Your text here")
    print("  [thoughtful] Your text here")
    print("Type 'quit' to exit, 'voices' to list available voices")
    print("="*60 + "\n")
    
    output_dir = Path("voice_output")
    output_dir.mkdir(exist_ok=True)
    
    while True:
        try:
            user_input = input("Text: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break
        
        if not user_input:
            continue
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        if user_input.lower() == 'voices':
            print("\nFetching available voices...")
            try:
                voices = assets.list_available_voices()
                print("\nAvailable ElevenLabs Voices:")
                for v in voices[:20]:
                    print(f"  {v['name']} ({v['voice_id']})")
                if len(voices) > 20:
                    print(f"  ... and {len(voices) - 20} more")
            except Exception as e:
                print(f"Error listing voices: {e}")
            continue
        
        emotion = EmotionalState.NEUTRAL
        text = user_input
        
        if user_input.startswith('['):
            end = user_input.find(']')
            if end > 0:
                emotion_str = user_input[1:end].lower()
                text = user_input[end+1:].strip()
                
                for state in EmotionalState:
                    if state.value == emotion_str:
                        emotion = state
                        break
        
        if not text:
            text = user_input
        
        print(f"\nGenerating speech with emotion: {emotion.value}")
        print("Processing...")
        
        try:
            filename = f"output_{len(list(output_dir.glob('*.mp3'))) + 1}.mp3"
            filepath = output_dir / filename
            
            assets.save_speech(text, str(filepath), emotional_state=emotion)
            
            print(f"Saved to: {filepath}")
            print(f"File size: {filepath.stat().st_size / 1024:.1f} KB")
            
            expression = assets.get_expression(emotion)
            print(f"Visual cues for animation: {', '.join(expression.visual_cues)}")
            
        except Exception as e:
            print(f"Error generating speech: {e}")
        
        print()


if __name__ == "__main__":
    main()
