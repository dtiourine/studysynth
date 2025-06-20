from fastapi import APIRouter, Depends, HTTPException
from .schemas import FlashcardDeckResponse
from .service import FlashcardService

router = APIRouter(prefix="/flashcards", tags=["Flashcards"])

@router.post("/decks", response_model=FlashcardDeckResponse)
async def create_deck(
        deck_data: FlashcardDeckCreate,
        current_user: USer = Depends(get_current_user),
        db: AsyncSession = Depends(get_db)
):
    """Create a new flashcard deck"""
    deck = await FlashcardService.create_deck(db, current_user.user_id, deck_data)
    return FlashcardDeckResponse(
        id=deck.id,
        title=deck.title,
        description=deck.description,
        created_at=deck.created_at,
        updated_at=deck.updated_at
    )