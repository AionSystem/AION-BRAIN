"""
PERSONALITY ARCHITECT v2.0 - LLM Runtime Module
Deploy personas to OpenAI, Anthropic Claude, or custom LLM APIs

Supports:
- OpenAI GPT-4/GPT-4o
- Anthropic Claude 3/3.5
- Any OpenAI-compatible API endpoint

Author: Sheldon K. Salmon (Mr. AION)
License: MIT
"""

import os
import json
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Generator, Callable
from abc import ABC, abstractmethod

from .persona_loader import PersonaCard


class LLMProvider(Enum):
    """Supported LLM providers."""
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    CUSTOM = "custom"


@dataclass
class Message:
    """A conversation message."""
    role: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class LLMResponse:
    """Response from an LLM call."""
    content: str
    model: str
    usage: Dict[str, int] = field(default_factory=dict)
    finish_reason: str = "stop"
    raw_response: Any = None


class BaseLLMClient(ABC):
    """Abstract base class for LLM clients."""
    
    @abstractmethod
    def chat(
        self,
        messages: List[Message],
        system_prompt: str,
        **kwargs
    ) -> LLMResponse:
        """Send messages and get a response."""
        pass
    
    @abstractmethod
    def stream(
        self,
        messages: List[Message],
        system_prompt: str,
        **kwargs
    ) -> Generator[str, None, None]:
        """Stream responses token by token."""
        pass


class OpenAIClient(BaseLLMClient):
    """OpenAI API client."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: str = "gpt-4o",
        max_tokens: int = 4096,
    ):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.base_url = base_url or "https://api.openai.com/v1"
        self.model = model
        self.max_tokens = max_tokens
        
        self._client = None
    
    def _get_client(self):
        """Lazily initialize the OpenAI client."""
        if self._client is None:
            try:
                from openai import OpenAI
                self._client = OpenAI(
                    api_key=self.api_key,
                    base_url=self.base_url,
                )
            except ImportError:
                raise ImportError("openai package required. Install with: pip install openai")
        return self._client
    
    def chat(
        self,
        messages: List[Message],
        system_prompt: str,
        **kwargs
    ) -> LLMResponse:
        """Send messages and get a response."""
        
        client = self._get_client()
        
        api_messages = [{"role": "system", "content": system_prompt}]
        for msg in messages:
            api_messages.append({"role": msg.role, "content": msg.content})
        
        response = client.chat.completions.create(
            model=kwargs.get("model", self.model),
            messages=api_messages,
            max_tokens=kwargs.get("max_tokens", self.max_tokens),
            temperature=kwargs.get("temperature", 0.7),
        )
        
        return LLMResponse(
            content=response.choices[0].message.content or "",
            model=response.model,
            usage={
                "prompt_tokens": response.usage.prompt_tokens if response.usage else 0,
                "completion_tokens": response.usage.completion_tokens if response.usage else 0,
            },
            finish_reason=response.choices[0].finish_reason or "stop",
            raw_response=response,
        )
    
    def stream(
        self,
        messages: List[Message],
        system_prompt: str,
        **kwargs
    ) -> Generator[str, None, None]:
        """Stream responses token by token."""
        
        client = self._get_client()
        
        api_messages = [{"role": "system", "content": system_prompt}]
        for msg in messages:
            api_messages.append({"role": msg.role, "content": msg.content})
        
        stream = client.chat.completions.create(
            model=kwargs.get("model", self.model),
            messages=api_messages,
            max_tokens=kwargs.get("max_tokens", self.max_tokens),
            temperature=kwargs.get("temperature", 0.7),
            stream=True,
        )
        
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content


class AnthropicClient(BaseLLMClient):
    """Anthropic Claude API client."""
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-5-sonnet-20241022",
        max_tokens: int = 4096,
    ):
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        self.model = model
        self.max_tokens = max_tokens
        
        self._client = None
    
    def _get_client(self):
        """Lazily initialize the Anthropic client."""
        if self._client is None:
            try:
                from anthropic import Anthropic
                self._client = Anthropic(api_key=self.api_key)
            except ImportError:
                raise ImportError("anthropic package required. Install with: pip install anthropic")
        return self._client
    
    def chat(
        self,
        messages: List[Message],
        system_prompt: str,
        **kwargs
    ) -> LLMResponse:
        """Send messages and get a response."""
        
        client = self._get_client()
        
        api_messages = []
        for msg in messages:
            api_messages.append({"role": msg.role, "content": msg.content})
        
        response = client.messages.create(
            model=kwargs.get("model", self.model),
            max_tokens=kwargs.get("max_tokens", self.max_tokens),
            system=system_prompt,
            messages=api_messages,
        )
        
        content = ""
        for block in response.content:
            if hasattr(block, "text"):
                content += block.text
        
        return LLMResponse(
            content=content,
            model=response.model,
            usage={
                "prompt_tokens": response.usage.input_tokens if response.usage else 0,
                "completion_tokens": response.usage.output_tokens if response.usage else 0,
            },
            finish_reason=response.stop_reason or "end_turn",
            raw_response=response,
        )
    
    def stream(
        self,
        messages: List[Message],
        system_prompt: str,
        **kwargs
    ) -> Generator[str, None, None]:
        """Stream responses token by token."""
        
        client = self._get_client()
        
        api_messages = []
        for msg in messages:
            api_messages.append({"role": msg.role, "content": msg.content})
        
        with client.messages.stream(
            model=kwargs.get("model", self.model),
            max_tokens=kwargs.get("max_tokens", self.max_tokens),
            system=system_prompt,
            messages=api_messages,
        ) as stream:
            for text in stream.text_stream:
                yield text


class LLMRuntime:
    """
    Deploy Personality Architect personas to LLM APIs.
    
    This is the main interface for running personas with LLMs.
    It handles:
    - System prompt generation from persona cards
    - Conversation management
    - State-aware prompting (via DIO integration)
    - Response processing
    
    Usage:
        from integrations import PersonaLoader, LLMRuntime, LLMProvider
        
        loader = PersonaLoader()
        persona = loader.load_by_name("Tesla")
        
        runtime = LLMRuntime(
            persona=persona,
            provider=LLMProvider.OPENAI,
            api_key="your-api-key"
        )
        
        response = runtime.chat("Tell me about renewable energy")
        print(response.content)
    """
    
    def __init__(
        self,
        persona: PersonaCard,
        provider: LLMProvider = LLMProvider.OPENAI,
        api_key: Optional[str] = None,
        model: Optional[str] = None,
        base_url: Optional[str] = None,
        current_state: Optional[str] = None,
        **kwargs
    ):
        self.persona = persona
        self.provider = provider
        self.current_state = current_state
        self.conversation_history: List[Message] = []
        
        self._build_client(provider, api_key, model, base_url, **kwargs)
        self._build_system_prompt()
    
    def _build_client(
        self,
        provider: LLMProvider,
        api_key: Optional[str],
        model: Optional[str],
        base_url: Optional[str],
        **kwargs
    ):
        """Build the appropriate LLM client."""
        
        if provider == LLMProvider.OPENAI:
            self.client = OpenAIClient(
                api_key=api_key,
                base_url=base_url,
                model=model or "gpt-4o",
                **kwargs
            )
        elif provider == LLMProvider.ANTHROPIC:
            self.client = AnthropicClient(
                api_key=api_key,
                model=model or "claude-3-5-sonnet-20241022",
                **kwargs
            )
        elif provider == LLMProvider.CUSTOM:
            self.client = OpenAIClient(
                api_key=api_key,
                base_url=base_url,
                model=model or "gpt-4o",
                **kwargs
            )
        else:
            raise ValueError(f"Unknown provider: {provider}")
    
    def _build_system_prompt(self):
        """Build the system prompt from the persona."""
        
        self.system_prompt = self.persona.get_system_prompt()
        
        if self.current_state:
            state_prompt = self.persona.get_current_state_prompt(self.current_state)
            self.system_prompt += state_prompt
    
    def set_state(self, state_name: str):
        """Set the current DIO state and rebuild the system prompt."""
        self.current_state = state_name
        self._build_system_prompt()
    
    def chat(self, user_message: str, **kwargs) -> LLMResponse:
        """
        Send a message and get a response in character.
        
        Args:
            user_message: The user's message
            **kwargs: Additional parameters to pass to the LLM
            
        Returns:
            LLMResponse with the persona's response
        """
        
        self.conversation_history.append(Message(role="user", content=user_message))
        
        response = self.client.chat(
            messages=self.conversation_history,
            system_prompt=self.system_prompt,
            **kwargs
        )
        
        self.conversation_history.append(Message(role="assistant", content=response.content))
        
        return response
    
    def stream_chat(self, user_message: str, **kwargs) -> Generator[str, None, None]:
        """
        Stream a response token by token.
        
        Args:
            user_message: The user's message
            **kwargs: Additional parameters to pass to the LLM
            
        Yields:
            Response tokens as they are generated
        """
        
        self.conversation_history.append(Message(role="user", content=user_message))
        
        full_response = ""
        for token in self.client.stream(
            messages=self.conversation_history,
            system_prompt=self.system_prompt,
            **kwargs
        ):
            full_response += token
            yield token
        
        self.conversation_history.append(Message(role="assistant", content=full_response))
    
    def clear_history(self):
        """Clear the conversation history."""
        self.conversation_history = []
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get the conversation history as a list of dicts."""
        return [{"role": m.role, "content": m.content} for m in self.conversation_history]
    
    def run_coherence_check(self, last_response: str) -> Dict[str, Any]:
        """
        Run a basic coherence check on the last response.
        
        Checks:
        - Vocabulary alignment (are signature words being used?)
        - Tone consistency (rough estimate based on response length and style)
        - Boundary adherence (did we stay in scope?)
        
        Returns:
            Dict with coherence metrics
        """
        
        voice = self.persona.voice_signature
        favorites = voice.get("favorites", voice.get("vocabulary", {}).get("favorites", []))
        avoids = voice.get("avoids", voice.get("vocabulary", {}).get("avoids", []))
        
        response_lower = last_response.lower()
        
        favorite_hits = sum(1 for word in favorites if word.lower() in response_lower)
        avoid_hits = sum(1 for word in avoids if word.lower() in response_lower)
        
        vocab_score = min(100, (favorite_hits * 20) - (avoid_hits * 30) + 50)
        
        return {
            "vocabulary_score": max(0, vocab_score),
            "favorite_words_used": favorite_hits,
            "avoided_words_used": avoid_hits,
            "response_length": len(last_response),
            "coherence_status": "GOOD" if vocab_score >= 60 else "CHECK" if vocab_score >= 40 else "DRIFT_DETECTED",
        }


def create_runtime(
    persona_name: str,
    provider: str = "openai",
    api_key: Optional[str] = None,
    **kwargs
) -> LLMRuntime:
    """
    Convenience function to create an LLMRuntime from a persona name.
    
    Usage:
        runtime = create_runtime("Tesla", provider="openai", api_key="...")
        response = runtime.chat("What inspired your work on AC power?")
    """
    
    from .persona_loader import PersonaLoader
    
    loader = PersonaLoader()
    persona = loader.load_by_name(persona_name)
    
    provider_enum = LLMProvider(provider.lower())
    
    return LLMRuntime(
        persona=persona,
        provider=provider_enum,
        api_key=api_key,
        **kwargs
    )


if __name__ == "__main__":
    print("LLM Runtime Module")
    print("=" * 50)
    print()
    print("Usage:")
    print("  from integrations import create_runtime")
    print()
    print("  runtime = create_runtime('Tesla', provider='openai', api_key='...')")
    print("  response = runtime.chat('Tell me about alternating current')")
    print("  print(response.content)")
