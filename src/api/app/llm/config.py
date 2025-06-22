from pydantic_settings import BaseSettings
from pathlib import Path
from typing import Literal


class LLMConfig(BaseSettings):
    LLM_PROVIDER: Literal["anthropic", "openai"] = "anthropic"

    ANTHROPIC_API_KEY: str = ""
    OPENAI_API_KEY: str = ""

    ANTHROPIC_MODEL: str = "claude-3-7-sonnet-latest"
    OPENAI_MODEL: str = "gpt-3.5-turbo"

    class Config:
        env_file = Path(__file__).parent / ".env"


llm_settings = LLMConfig()

