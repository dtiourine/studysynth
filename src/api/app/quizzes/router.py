from fastapi import APIRouter, Depends, HTTPException, status, Security
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.app.auth.service import VerifyToken
from src.api.app.database import get_db
from src.api.app.llm.exceptions import LLMGenerationError
from src.api.app.quizzes.dependencies import get_quiz_service
from src.api.app.quizzes.service import QuizService
from src.api.app.study_materials_generator.dependencies import get_study_materials_generator
from src.api.app.study_materials_generator.schemas import StudyContent
from src.api.app.study_materials_generator.service import StudyMaterialsGenerator
# from src.api.app.auth.dependencies import get_current_user

import logging

logger = logging.getLogger(__name__)

auth = VerifyToken()

router = APIRouter(
    prefix="/quizzes",
    tags=["Quizzes"],
)


@router.get("/")
def get_quizzes():
    return {"Hello": "World"}

@router.get("/test-auth")
def test_auth(auth_result: str = Security(auth.verify)):  # Exact same signature as /api/private
    """Test auth with exact same pattern as /api/private"""
    return {"message": "Auth working in quiz router!", "auth_result": auth_result}


@router.post("/")
async def post_quizzes(
        study_content: StudyContent,
        user_data: dict = Security(auth.verify),
        db: AsyncSession = Depends(get_db),
        study_materials_generator: StudyMaterialsGenerator = Depends(get_study_materials_generator),
        quiz_service: QuizService = Depends(get_quiz_service)
):
    try:
        logger.info("Starting quiz generation")
        quiz_data = await study_materials_generator.generate_quiz(study_content)
        logger.info("Quiz generation successful, creating in database")
        created_quiz = await quiz_service.create_quiz(
            db=db,
            owner_id=user_data["sub"],
            quiz_data=quiz_data
        )
        return created_quiz
    except LLMGenerationError as e:
        logger.error(f"LLM Generation Error: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Failed to generate quiz content. Please try again."
        )
    except ValidationError as e:
        logger.error(f"Validation Error: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid quiz data generated"
        )
    except Exception as e:
        logger.error(f"Unexpected error in post_quizzes: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )


@router.delete("/")
def delete_quizzes():
    return {"Hello": "World"}


@router.put("/")
def update_quizzes():
    return {"Hello": "World"}

