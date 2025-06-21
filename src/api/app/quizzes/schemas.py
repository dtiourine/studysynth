from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum
from datetime import datetime

class AnswerChoicesSchema(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"


# Question schemas
class QuestionCreate(BaseModel):
    question_text: str = Field(..., min_length=1, max_length=1000)
    choice_a: str = Field(..., min_length=1, max_length=500)
    choice_b: str = Field(..., min_length=1, max_length=500)
    choice_c: str = Field(..., min_length=1, max_length=500)
    choice_d: str = Field(..., min_length=1, max_length=500)
    correct_answer: AnswerChoicesSchema


class QuestionUpdate(BaseModel):
    question_text: Optional[str] = Field(None, min_length=1, max_length=1000)
    choice_a: Optional[str] = Field(None, min_length=1, max_length=500)
    choice_b: Optional[str] = Field(None, min_length=1, max_length=500)
    choice_c: Optional[str] = Field(None, min_length=1, max_length=500)
    choice_d: Optional[str] = Field(None, min_length=1, max_length=500)
    correct_answer: Optional[AnswerChoicesSchema] = None


class QuestionResponse(BaseModel):
    id: int
    question_text: str
    choice_a: str
    choice_b: str
    choice_c: str
    choice_d: str
    correct_answer: AnswerChoicesSchema

    class Config:
        from_attributes = True


# Quiz schemas
class QuizCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    questions: List[QuestionCreate] = Field(..., min_items=1, max_items=50)


class QuizUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)


class QuizResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = Field(None, max_length=1000)
    created_at: datetime
    updated_at: Optional[datetime]
    question_count: int

    class Config:
        from_attributes = True


class QuizDetailResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]
    questions: List[QuestionResponse]

    class Config:
        from_attributes = True


class QuizListResponse(BaseModel):
    quizzes: List[QuizResponse]


