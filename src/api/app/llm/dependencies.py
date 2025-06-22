from functools import lru_cache
from fastapi import Depends

from api.app.llm.client.abstract import AbstractLLMClient
from api.app.llm.client.factory import get_available_providers, create_llm_client
from api.app.llm.config import llm_settings
from api.app.llm.exceptions import LLMConfigurationError
from api.app.llm.service import LLMService


@lru_cache()
def get_llm_client() -> AbstractLLMClient:
    """Factory function to create LLM client based on configuration"""
    provider = llm_settings.LLM_PROVIDER.lower()

    if provider == "anthropic":
        if not llm_settings.ANTHROPIC_API_KEY:
            raise LLMConfigurationError("Anthropic API key not configured")
        api_key = llm_settings.ANTHROPIC_API_KEY
        model = llm_settings.ANTHROPIC_MODEL
    elif provider == "openai":
        if not llm_settings.OPENAI_API_KEY:
            raise LLMConfigurationError("OpenAI API key not configured")
        api_key = llm_settings.OPENAI_API_KEY
        model = llm_settings.OPENAI_MODEL
    else:
        available = ", ".join(get_available_providers())
        raise LLMConfigurationError(
            f"Unsupported LLM provider: {provider}. Available: {available}"
        )

    return create_llm_client(provider, api_key, model)


def get_llm_service(
    llm_client: AbstractLLMClient = Depends(get_llm_client)
) -> LLMService:
    """Dependency to get LLM service instance"""
    return LLMService(llm_client)



