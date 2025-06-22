from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.app.database import get_db
from src.api.app.llm.exceptions import LLMGenerationError
from src.api.app.quizzes.dependencies import get_quiz_service
from src.api.app.quizzes.service import QuizService
from src.api.app.study_materials_generator.dependencies import get_study_materials_generator
from src.api.app.study_materials_generator.schemas import StudyContent
from src.api.app.study_materials_generator.service import StudyMaterialsGenerator
from src.api.app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/quizzes",
    tags=["Quizzes"],
    dependencies=[Depends(get_current_user)],
)


@router.get("/")
def get_quizzes():
    return {"Hello": "World"}


@router.post("/")
async def post_quizzes(
        study_content: StudyContent,
        user_data = Depends(get_current_user),
        db: AsyncSession = Depends(get_db),
        study_materials_generator: StudyMaterialsGenerator = Depends(get_study_materials_generator),
        quiz_service: QuizService = Depends(get_quiz_service)
):
    try:
        quiz_data = await study_materials_generator.generate_quiz(study_content)
        created_quiz = await quiz_service.create_quiz(
            db=db,
            owner_id=user_data["sub"],
            quiz_data=quiz_data
        )
        return created_quiz
    except LLMGenerationError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Failed to generate quiz content. Please try again."
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid quiz data generated"
        )
    except Exception as e:
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

