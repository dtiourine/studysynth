from fastapi import Depends

from src.api.app.llm.dependencies import get_llm_service
from src.api.app.llm.service import LLMService
from src.api.app.study_materials_generator.service import StudyMaterialsGenerator


def get_study_materials_generator(
        llm_service: LLMService = Depends(get_llm_service)
) -> StudyMaterialsGenerator:
    return StudyMaterialsGenerator(llm=llm_service)
