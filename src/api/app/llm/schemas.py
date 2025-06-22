from pydantic import BaseModel, Field
from typing import Optional


class LLMRequest(BaseModel):
    prompt: str = Field(..., min_length=1, description="The input prompt")
    system_prompt: Optional[str] = Field(..., min_length=1, description="System prompt for context")


class LLMResponse(BaseModel):
    text: str = Field(..., description="Generated text")


