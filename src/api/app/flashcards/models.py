from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class FlashcardDeck(Base):
    __tablename__ = 'flashcard_decks'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)

    owner_id = Column(String(255), ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    flashcards = relationship("Flashcard", back_populates="deck", cascade="all, delete-orphan")


class Flashcard(Base):
    __tablename__ = 'flashcards'

    id = Column(Integer, primary_key=True)
    deck_id = Column(Integer, ForeignKey("flashcard_decks.id"), nullable=False)

    front_text = Column(Text, nullable=False)
    back_text = Column(Text, nullable=False)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    deck = relationship("FlashcardDeck", back_populates="flashcards")



