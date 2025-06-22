from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class FlashcardCreate(BaseModel):
    front_text: str = Field(..., min_length=1, max_length=1000)
    back_text: str = Field(..., min_length=1, max_length=1000)


class FlashcardUpdate(BaseModel):
    front_text: Optional[str] = Field(None, min_length=1, max_length=1000)
    back_text: Optional[str] = Field(None, min_length=1, max_length=1000)


class FlashcardResponse(BaseModel):
    id: int
    front_text: str
    back_text: str
    created_at: datetime


class FlashcardDeckCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    flashcards: List[FlashcardCreate] = Field(..., min_items=1, max_items=50)

    description: Optional[str] = Field(None, max_length=1000)


class FlashcardDeckUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)


class FlashcardDeckResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    created_at: datetime
    updated_at: datetime



