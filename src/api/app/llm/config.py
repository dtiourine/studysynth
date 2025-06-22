from pydantic_settings import BaseSettings
from typing import Literal


class LLMConfig(BaseSettings):
    LLM_PROVIDER: Literal["anthropic", "openai"] = "anthropic"

    ANTHROPIC_API_KEY: str = ""
    OPENAI_API_KEY: str = ""

    ANTHROPIC_MODEL: str = "claude-3-sonnet-20240229"
    OPENAI_MODEL: str = "gpt-3.5-turbo"

    class Config:
        env_prefix = "LLM_"


llm_settings = LLMConfig()

