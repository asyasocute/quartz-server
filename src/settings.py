import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql+asyncpg://myuser:mypassword@0.0.0.0:5432/mydb"
    )

    def get_database_url(self):
        return self.DATABASE_URL


settings = Settings()
