from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, func
from sqlalchemy.orm import selectinload
from api.app.quizzes.models import Quiz, MultipleChoiceQuestion, AnswerChoices
from api.app.quizzes.schemas import QuizCreate


class QuizService:
    @staticmethod
    async def create_quiz(db: AsyncSession, owner_id: str, quiz_data: QuizCreate) -> Quiz:
        """Create a new quiz with questions"""
        try:
            quiz = Quiz(
                title=quiz_data.title,
                description=quiz_data.description,
                owner_id=owner_id
            )

            db.add(quiz)
            await db.flush()

            questions = []
            for i, question_data in enumerate(quiz_data.questions):
                question = MultipleChoiceQuestion(
                    quiz_id=quiz.id,
                    question_text=question_data.question_text,
                    choice_a=question_data.choice_a,
                    choice_b=question_data.choice_b,
                    choice_c=question_data.choice_c,
                    choice_d=question_data.choice_d,
                    correct_answer=AnswerChoices(question_data.correct_answer.value)
                )
                questions.append(question)

            db.add_all(questions)
            await db.commit()
            await db.refresh(quiz)

            return quiz

        except Exception as e:
            await db.rollback()
            raise e

    @staticmethod
    async def get_user_quizzes(db: AsyncSession, owner_id: str, skip: int = 0, limit: int = 100) -> tuple[List[Quiz], int]:
        """Get all quizzes for a user"""
        count_stmt = select(func.count(Quiz.id)).filter(Quiz.owner_id == owner_id)
        count_result = await db.execute(count_stmt)
        total = count_result.scalar()

        stmt = (
            select(Quiz)
            .filter(Quiz.owner_id == owner_id)
            .options(selectinload(Quiz.questions))  # Eagerly load questions
            .offset(skip)
            .limit(limit)
            .order_by(Quiz.created_at.desc())
        )

        result = await db.execute(stmt)
        quizzes = result.scalars().all()

        return quizzes, total










