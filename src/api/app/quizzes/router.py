from fastapi import APIRouter, HTTPException, Security
from pydantic import BaseModel
from typing import List, Optional

from src.api.app.auth.service import VerifyToken

router = APIRouter(prefix="/quizzes", tags=["Quizzes"])

auth = VerifyToken()

@router.get("/quizzes")
def get_quizzes(auth_result: str = Security(auth.verify):
    return {"Hello": "World"}


@router.post("/quizzes")
def post_quizzes(auth_result: str = Security(auth.verify):
    return {"Hello": "World"}


@router.delete("/quizzes")
def delete_quizzes(auth_result: str = Security(auth.verify):
    return {"Hello": "World"}


@router.put("/quizzes")
def update_quizzes(auth_result: str = Security(auth.verify):
    return {"Hello": "World"}

