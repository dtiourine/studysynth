from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from src.api.app.config import settings
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(settings.database_url)


class Base(DeclarativeBase):
    pass


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Database dependency for FastAPI.
    Creates a new database session for each request and ensures it's closed
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()



