from abc import ABC, abstractmethod

from api.app.llm.schemas import LLMRequest, LLMResponse


class AbstractLLMClient(ABC):
    def __init__(self, api_key, model):
        self.api_key = api_key
        self.model = model

    @abstractmethod
    async def generate_text(self, request: LLMRequest) -> LLMResponse:
        pass



