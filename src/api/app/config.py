from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str

    AUTH0_DOMAIN: str
    AUTH0_API_AUDIENCE: str
    AUTH0_ISSUER: str
    AUTH0_ALGORITHMS: str

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()

