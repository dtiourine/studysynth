from sqlalchemy import create_engine, text, Column, Integer, String
from src.api.app.config import settings
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(settings.database_url)

Session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


