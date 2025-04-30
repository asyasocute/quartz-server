from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from src.models.user import User
from src.security import get_password_hash, pwd_context


async def get_user_by_username(username: str, db: AsyncSession) -> User | None:
    stmt = select(User).where(User.username == username)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def create_user(
    username: str, password: str, db: AsyncSession, is_superuser: bool = False
) -> User:
    new_user: User = User(
        username=username,
        hashed_password=get_password_hash(password),
        is_superuser=is_superuser,
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


async def authenticate(
    session: AsyncSession, username: str, password: str
) -> User | None:
    stmt = select(User).where(User.username == username)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    if user and pwd_context.verify(password, user.hashed_password):
        return user
    return None

