from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import List
from pathlib import Path


class AuthConfig(BaseSettings):
    auth0_domain: str
    auth0_api_audience: str
    auth0_issuer: str
    auth0_algorithms: str

    class Config:
        env_file = Path(__file__).parent.parent.parent / ".env"
        env_file_encoding = 'utf-8'
        extra = 'ignore'


@lru_cache()
def get_auth_settings():
    return AuthConfig()
