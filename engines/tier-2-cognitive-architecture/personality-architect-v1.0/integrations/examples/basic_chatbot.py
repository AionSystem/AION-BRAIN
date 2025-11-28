#!/usr/bin/env python3
"""
PERSONALITY ARCHITECT v2.0 - Basic Chatbot Example

This example shows the simplest way to deploy a persona to an LLM.
No bells and whistles - just load a persona and start chatting.

Requirements:
    pip install openai pyyaml

Usage:
    export OPENAI_API_KEY="your-key"
    python basic_chatbot.py
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from persona_loader import PersonaLoader
from llm_runtime import LLMRuntime, LLMProvider


def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Set it with: export OPENAI_API_KEY='your-key'")
        return
    
    print("Loading persona...")
    loader = PersonaLoader()
    
    available = loader.list_personas()
    if not available:
        print("No personas found. Using a simple example persona.")
        print("Make sure you have persona YAML files in the personas/ directory.")
        return
    
    print("\nAvailable personas:")
    for i, p in enumerate(available, 1):
        print(f"  {i}. {p['name']} ({p['category']})")
    
    choice = input("\nSelect persona number (or press Enter for first): ").strip()
    if choice:
        try:
            persona_info = available[int(choice) - 1]
        except (ValueError, IndexError):
            persona_info = available[0]
    else:
        persona_info = available[0]
    
    persona = loader.load(persona_info['file'])
    print(f"\nLoaded: {persona.name}")
    
    validation = persona.validate()
    print(f"Persona Coherence Score: {validation['pcs_score']}/100")
    if validation['warnings']:
        for warning in validation['warnings']:
            print(f"  Warning: {warning}")
    
    print("\nConnecting to OpenAI...")
    runtime = LLMRuntime(
        persona=persona,
        provider=LLMProvider.OPENAI,
        api_key=api_key,
    )
    
    print(f"\n{'='*50}")
    print(f"Chatting with {persona.name}")
    print("Type 'quit' to exit, 'clear' to reset conversation")
    print(f"{'='*50}\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break
        
        if not user_input:
            continue
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        if user_input.lower() == 'clear':
            runtime.clear_history()
            print("[Conversation cleared]")
            continue
        
        print(f"\n{persona.name}: ", end="", flush=True)
        
        full_response = ""
        for token in runtime.stream_chat(user_input):
            print(token, end="", flush=True)
            full_response += token
        
        print("\n")
        
        coherence = runtime.run_coherence_check(full_response)
        if coherence['coherence_status'] != 'GOOD':
            print(f"[Coherence: {coherence['coherence_status']}]")


if __name__ == "__main__":
    main()
