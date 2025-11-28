"""
Oracle Layer AI Providers
=========================

Platform-agnostic interface for different AI providers.
Allows Oracle Layer to work with OpenAI, Anthropic, Google, or any other AI.
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
import os


@dataclass
class AIResponse:
    """Standardized response from any AI provider."""
    content: str
    model: str
    provider: str
    usage: Optional[Dict[str, int]] = None
    raw_response: Optional[Any] = None


class AIProvider(ABC):
    """
    Abstract base class for AI providers.
    
    Implement this to add support for new AI platforms.
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        """Provider name (e.g., 'openai', 'anthropic')."""
        pass
    
    @abstractmethod
    def complete(self, prompt: str, system_prompt: Optional[str] = None,
                 temperature: float = 0.7, max_tokens: int = 4096) -> AIResponse:
        """
        Send a prompt to the AI and get a response.
        
        Args:
            prompt: The user prompt to send
            system_prompt: Optional system/context prompt
            temperature: Creativity level (0.0-1.0)
            max_tokens: Maximum response length
            
        Returns:
            AIResponse with the AI's response
        """
        pass
    
    def is_available(self) -> bool:
        """Check if this provider is configured and available."""
        return True


class OpenAIProvider(AIProvider):
    """
    OpenAI provider (GPT-4, GPT-3.5, etc.)
    
    Requires: OPENAI_API_KEY environment variable
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        self._client = None
    
    @property
    def name(self) -> str:
        return "openai"
    
    def is_available(self) -> bool:
        return self.api_key is not None
    
    def _get_client(self):
        if self._client is None:
            try:
                from openai import OpenAI
                self._client = OpenAI(api_key=self.api_key)
            except ImportError:
                raise ImportError("OpenAI package not installed. Run: pip install openai")
        return self._client
    
    def complete(self, prompt: str, system_prompt: Optional[str] = None,
                 temperature: float = 0.7, max_tokens: int = 4096) -> AIResponse:
        client = self._get_client()
        
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        
        response = client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return AIResponse(
            content=response.choices[0].message.content,
            model=self.model,
            provider=self.name,
            usage={
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            },
            raw_response=response
        )


class AnthropicProvider(AIProvider):
    """
    Anthropic provider (Claude)
    
    Requires: ANTHROPIC_API_KEY environment variable
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-5-sonnet-20241022"):
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.model = model
        self._client = None
    
    @property
    def name(self) -> str:
        return "anthropic"
    
    def is_available(self) -> bool:
        return self.api_key is not None
    
    def _get_client(self):
        if self._client is None:
            try:
                from anthropic import Anthropic
                self._client = Anthropic(api_key=self.api_key)
            except ImportError:
                raise ImportError("Anthropic package not installed. Run: pip install anthropic")
        return self._client
    
    def complete(self, prompt: str, system_prompt: Optional[str] = None,
                 temperature: float = 0.7, max_tokens: int = 4096) -> AIResponse:
        client = self._get_client()
        
        kwargs = {
            "model": self.model,
            "max_tokens": max_tokens,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        if system_prompt:
            kwargs["system"] = system_prompt
        
        response = client.messages.create(**kwargs)
        
        return AIResponse(
            content=response.content[0].text,
            model=self.model,
            provider=self.name,
            usage={
                "prompt_tokens": response.usage.input_tokens,
                "completion_tokens": response.usage.output_tokens,
                "total_tokens": response.usage.input_tokens + response.usage.output_tokens
            },
            raw_response=response
        )


class GoogleProvider(AIProvider):
    """
    Google provider (Gemini)
    
    Requires: GOOGLE_API_KEY environment variable
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gemini-pro"):
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self.model = model
        self._client = None
    
    @property
    def name(self) -> str:
        return "google"
    
    def is_available(self) -> bool:
        return self.api_key is not None
    
    def _get_client(self):
        if self._client is None:
            try:
                import google.generativeai as genai
                genai.configure(api_key=self.api_key)
                self._client = genai.GenerativeModel(self.model)
            except ImportError:
                raise ImportError("Google AI package not installed. Run: pip install google-generativeai")
        return self._client
    
    def complete(self, prompt: str, system_prompt: Optional[str] = None,
                 temperature: float = 0.7, max_tokens: int = 4096) -> AIResponse:
        client = self._get_client()
        
        full_prompt = prompt
        if system_prompt:
            full_prompt = f"{system_prompt}\n\n{prompt}"
        
        response = client.generate_content(
            full_prompt,
            generation_config={
                "temperature": temperature,
                "max_output_tokens": max_tokens
            }
        )
        
        return AIResponse(
            content=response.text,
            model=self.model,
            provider=self.name,
            raw_response=response
        )


class GenericProvider(AIProvider):
    """
    Generic provider for testing or custom implementations.
    
    Can be used with any API that follows a simple interface,
    or for testing without an actual AI connection.
    """
    
    def __init__(self, name: str = "generic", 
                 complete_fn: Optional[callable] = None):
        self._name = name
        self._complete_fn = complete_fn
    
    @property
    def name(self) -> str:
        return self._name
    
    def complete(self, prompt: str, system_prompt: Optional[str] = None,
                 temperature: float = 0.7, max_tokens: int = 4096) -> AIResponse:
        if self._complete_fn:
            result = self._complete_fn(prompt, system_prompt)
            if isinstance(result, str):
                return AIResponse(content=result, model="custom", provider=self.name)
            return result
        
        return AIResponse(
            content=f"[GenericProvider] Received prompt of {len(prompt)} characters",
            model="mock",
            provider=self.name
        )


class ProviderFactory:
    """Factory for creating AI providers."""
    
    _providers = {
        "openai": OpenAIProvider,
        "anthropic": AnthropicProvider,
        "google": GoogleProvider,
        "generic": GenericProvider,
    }
    
    @classmethod
    def create(cls, provider_name: str, **kwargs) -> AIProvider:
        """
        Create a provider by name.
        
        Args:
            provider_name: One of 'openai', 'anthropic', 'google', 'generic'
            **kwargs: Provider-specific arguments
            
        Returns:
            Configured AIProvider instance
        """
        if provider_name not in cls._providers:
            raise ValueError(f"Unknown provider: {provider_name}. "
                           f"Available: {list(cls._providers.keys())}")
        return cls._providers[provider_name](**kwargs)
    
    @classmethod
    def auto_detect(cls) -> Optional[AIProvider]:
        """
        Auto-detect available provider based on environment variables.
        
        Returns:
            First available provider, or None
        """
        for name, provider_class in cls._providers.items():
            if name == "generic":
                continue
            provider = provider_class()
            if provider.is_available():
                return provider
        return None
    
    @classmethod
    def register(cls, name: str, provider_class: type) -> None:
        """Register a custom provider."""
        cls._providers[name] = provider_class
