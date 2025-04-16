import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = os.getenv("SECRET_KEY", "pls_set_secret_key")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    # DATABASE_URL: str = os.getenv("DATABASE_URL")
    # SERVER_ADDRESS: str = os.getenv("SERVER_ADDRESS", "0.0.0.0")
    # SERVER_PORT: str = os.getenv("SERVER_PORT", "8000")

    def get_database_url(self):
        return self.DATABASE_URL

    # class Config:
    #     env_file: str = ".env"


settings = Settings()
