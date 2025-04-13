from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.settings import settings


# DATABASE_URL = "sqlite+aiosqlite:///./test.db"
# DATABASE_URL = "sqlite+aiosqlite:///./test.db"

engine = create_async_engine(settings.DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with async_session() as session:
        yield session


db_session = Annotated[AsyncSession, Depends(get_db)]
