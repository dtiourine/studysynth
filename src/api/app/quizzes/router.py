from fastapi import APIRouter, Depends
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
def post_quizzes():
    return {"Hello": "World"}


@router.delete("/")
def delete_quizzes():
    return {"Hello": "World"}


@router.put("/")
def update_quizzes():
    return {"Hello": "World"}

