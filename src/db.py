from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase


# DATABASE_URL = "sqlite+aiosqlite:///./test.db"
# DATABASE_URL = "sqlite+aiosqlite:///./test.db"
DATABASE_URL = "postgresql+asyncpg://myuser:mypassword@0.0.0.0:5432/mydb"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with async_session() as session:
        yield session
