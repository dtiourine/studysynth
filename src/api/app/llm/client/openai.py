import openai
from src.api.app.llm.client.abstract import AbstractLLMClient
from src.api.app.llm.exceptions import LLMGenerationError
from src.api.app.llm.schemas import LLMRequest, LLMResponse


class OpenAILLMClient(AbstractLLMClient):
    def __init__(self, api_key: str, model: str):
        super().__init__(api_key, model)
        openai.api_key = api_key

    async def generate_text(self, request: LLMRequest) -> LLMResponse:
        try:
            messages = []
            if request.system_prompt:
                messages.append({
                    "role": "system",
                    "content": request.system_prompt
                })
            messages.append({
                "role": "user",
                "content": request.prompt
            })

            res = await openai.ChatCompletion.acreate(
                model=self.model,
                messages=messages
            )

            generated = res.choices[0].message.content

            return LLMResponse(text=generated)

        except Exception as e:
            raise LLMGenerationError(f"OpenAI API error: {str(e)}")

