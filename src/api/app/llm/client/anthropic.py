from api.app.llm.client.abstract import AbstractLLMClient
from anthropic import AsyncAnthropic

from api.app.llm.exceptions import LLMGenerationError
from api.app.llm.schemas import LLMRequest, LLMResponse


class AnthropicLLMClient(AbstractLLMClient):
    def __init__(self, api_key: str, model: str):
        super().__init__(api_key, model)
        self._client = AsyncAnthropic(api_key=api_key)

    async def generate_text(self, request: LLMRequest) -> LLMResponse:
        try:
            messages = []
            if request.system_prompt:
                messages.append({"role": "system", "content": request.system_prompt})
            messages.append({"role": "user", "content": request.prompt})

            res = await self._client.messages.create(
                model=self.model,
                messages=messages
            )

            return LLMResponse(text=res.content[0].text)

        except Exception as e:
            raise LLMGenerationError(f"Anthropic API error: {str(e)}")

