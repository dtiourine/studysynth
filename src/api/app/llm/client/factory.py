from typing import Dict, Type

from api.app.llm.client.abstract import AbstractLLMClient
from api.app.llm.client.anthropic import AnthropicLLMClient
from api.app.llm.client.openai import OpenAILLMClient
from api.app.llm.exceptions import LLMConfigurationError

LLM_PROVIDERS: Dict[str, Type[AbstractLLMClient]] = {
    "anthropic": AnthropicLLMClient,
    "openai": OpenAILLMClient
}


def create_llm_client(
    provider: str,
    api_key: str,
    model: str
) -> AbstractLLMClient:
    """Factory function to create LLM client instances"""
    provider = provider.lower()

    if provider not in LLM_PROVIDERS:
        available_providers = ", ".join(LLM_PROVIDERS.keys())
        raise LLMConfigurationError(
            f"Unsupported LLM provider: {provider}. "
            f"Available providers: {available_providers}"
        )

    client_class = LLM_PROVIDERS[provider]
    return client_class(api_key, model)


def register_llm_provider(name: str, client_class: Type[AbstractLLMClient]) -> None:
    """Register a new LLM provider (useful for plugins/extensions)"""
    LLM_PROVIDERS[name] = client_class


def get_available_providers() -> list[str]:
    """Get all available LLM providers"""
    return list(LLM_PROVIDERS.keys())