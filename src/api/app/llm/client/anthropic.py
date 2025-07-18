from src.api.app.llm.client.abstract import AbstractLLMClient
from anthropic import AsyncAnthropic

from src.api.app.llm.exceptions import LLMGenerationError
from src.api.app.llm.schemas import LLMRequest, LLMResponse


class AnthropicLLMClient(AbstractLLMClient):
    def __init__(self, api_key: str, model: str):
        super().__init__(api_key, model)
        self._client = AsyncAnthropic(api_key=api_key)

    async def generate_text(self, request: LLMRequest) -> LLMResponse:
        try:
            messages = [{"role": "user", "content": request.prompt}]

            res = await self._client.messages.create(
                model=self.model,
                max_tokens=4000,
                messages=messages,
                system=request.system_prompt,
            )

            return LLMResponse(text=res.content[0].text)

        except Exception as e:
            raise LLMGenerationError(f"Anthropic API error: {str(e)}")

