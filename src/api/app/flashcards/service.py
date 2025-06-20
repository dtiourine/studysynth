from src.api.app.flashcards.models import Flashcard
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, or_
from sqlalchemy.orm import selectinload
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
    async def get_deck_by_id(
            db: AsyncSession,
            deck_id: int,
            owner_id: str,
    ) -> Optional[FlashcardDeck]:
        """Get deck by ID (must be owned by user)"""
        result = await db.execute(
            select(FlashcardDeck)
            .where(
                and_(
                    FlashcardDeck.id == deck_id,
                    and_(
                        FlashcardDeck.owner_id == owner_id,
                    )
                )
            )
            .options(selectinload(FlashcardDeck.flashcards))
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_flashcard(db: AsyncSession, user_id: str) -> Optional[Flashcard]:
        result = await db.execute(
            select(Flashcard).where(Flashcard.user_id == user_id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def add_card_to_deck(
        db: AsyncSession,
        deck_id: int,
        owner_id: str,
        flashcard_data: Flashcard,
    ) -> Optional[Flashcard]:
        deck = await FlashcardService.get_deck_by_id(db, deck_id, owner_id)
        if not deck or deck.owner_id != owner_id:
            return None

        db_flashcard = Flashcard(
            deck_id=deck_id,
            **flashcard_data.model_dump()
        )

        db.add(db_flashcard)
        await db.commit()
        await db.refresh(db_flashcard)
        return db_flashcard
