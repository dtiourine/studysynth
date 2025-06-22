from api.app.llm.client.abstract import AbstractLLMClient
from api.app.llm.exceptions import LLMGenerationError
from api.app.llm.schemas import LLMRequest, LLMResponse


class LLMService:
    """Business logic layer for LLM operations"""

    def __init__(self, llm_client: AbstractLLMClient):
        self.llm_client = llm_client

    async def generate_content(self, request: LLMRequest) -> LLMResponse:
        """Generate content with business logic validation"""
        try:
            res = await self.llm_client.generate_text(request)
            return res
        except Exception as e:
            raise LLMGenerationError(f"Content generation failed: {str(e)}")

