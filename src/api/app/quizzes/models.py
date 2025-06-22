from sqlalchemy import Column, String, Integer, Text, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum

from src.api.app.database import Base


class AnswerChoices(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"


class Quiz(Base):
    __tablename__ = 'quizzes'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text)

    owner_id = Column(String(255), nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    questions = relationship("MultipleChoiceQuestion", back_populates="quiz", cascade="all, delete-orphan")


class MultipleChoiceQuestion(Base):
    __tablename__ = 'multiple_choice_questions'

    id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.id'), nullable=False)
    question_text = Column(String(255), nullable=False)
    choice_a = Column(String(255), nullable=False)
    choice_b = Column(String(255), nullable=False)
    choice_c = Column(String(255), nullable=False)
    choice_d = Column(String(255), nullable=False)
    correct_answer = Column(SQLEnum(AnswerChoices), nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    quiz = relationship("Quiz", back_populates="questions")

    def get_choice_text(self, choice: AnswerChoices) -> str:
        """Helper method to get the text for a specific choice"""
        choice_map = {
            AnswerChoices.A: self.choice_a,
            AnswerChoices.B: self.choice_b,
            AnswerChoices.C: self.choice_c,
            AnswerChoices.D: self.choice_d,
        }
        return choice_map[choice]


