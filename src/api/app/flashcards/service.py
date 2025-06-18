from src.api.app.flashcards.models import Flashcard
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
from .models import FlashcardDeck, Flashcard
from .schemas import FlashcardDeckCreate, FlashcardDeckUpdate, FlashcardCreate, FlashcardUpdate


class FlashcardService:

    @staticmethod
    async def create_deck(db: AsyncSession, owner_id: str, deck_data: FlashcardDeck) -> FlashcardDeck:
        """Create a new flashcard deck"""
        db_deck = FlashcardDeck(
            owner_id=owner_id,
            **deck_data.model_dump()
        )
        db.add(db_deck)
        await db.commit()
        await db.refresh(db_deck)
        return db_deck

    @staticmethod
    async def get_flashcard(db: AsyncSession, user_id: str) -> Optional[Flashcard]:
        result = await db.execute(
            select(Flashcard).where(Flashcard.user_id == user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def create_flashcard(
        db: AsyncSession,
        user_id: str,
        flashcard: Fl
    ):

