import json

from pydantic import ValidationError

from api.app.flashcards.schemas import FlashcardCreate
from api.app.llm.exceptions import LLMGenerationError
from api.app.llm.schemas import LLMRequest
from api.app.llm.service import LLMService
from api.app.quizzes.schemas import QuizCreate
from api.app.study_materials_generator.constants import QUIZ_GENERATION_PROMPT, FLASHCARD_GENERATION_PROMPT
from api.app.study_materials_generator.schemas import StudyContent


class StudyMaterialsGenerator:
    def __init__(self, llm: LLMService):
        self._llm = llm

    async def generate_quiz(self, study_content: StudyContent) -> QuizCreate:
        """Generates multiple choice quiz from study content"""
        try:
            prompt = study_content.text
            llm_request = LLMRequest(
                prompt=prompt,
                system_prompt=QUIZ_GENERATION_PROMPT
            )

            llm_response = await self._llm.generate_content(llm_request)

            try:
                quiz_data = json.loads(llm_response.text)

                return QuizCreate(**quiz_data)

            except json.JSONDecodeError as e:
                raise ValueError(f"LLM returned invalid JSON: {e}")
            except ValidationError as e:
                raise ValueError(f"LLM response doesn't match expected format: {e}")

        except Exception as e:
            raise LLMGenerationError(f"Error generating quiz: {e}")

    async def generate_flashcards(self, study_content: StudyContent) -> FlashcardCreate:
        """Generates multiple choice flashcards from study content"""
        try:
            prompt = study_content.text
            llm_request = LLMRequest(
                prompt=prompt,
                system_prompt=FLASHCARD_GENERATION_PROMPT
            )

            llm_response = await self._llm.generate_content(llm_request)

            try:
                flashcard_data = json.loads(llm_response.text)

                return FlashcardCreate(**flashcard_data)

            except json.JSONDecodeError as e:
                raise ValueError(f"LLM returned invalid JSON: {e}")
            except ValidationError as e:
                raise ValueError(f"LLM response doesn't match expected format: {e}")

        except Exception as e:
            raise LLMGenerationError(f"Error generating flashcard: {e}")

