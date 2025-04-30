from fastapi import HTTPException
from sqlalchemy.sql.selectable import Select


from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_400_BAD_REQUEST
from src.models.user import User
from src.security import get_password_hash, pwd_context
from src.schemas import NoteCreate, NoteScheme
from src.models.note import Note


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
    query = select(User).where(User.username == username)
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    if user and pwd_context.verify(password, user.hashed_password):
        return user
    return None


async def add_note(session: AsyncSession, note: NoteCreate, user_id: int) -> NoteScheme:
    new_note = Note(name=note.name, text=note.name, user_id=user_id)
    session.add(new_note)
    await session.commit()
    await session.refresh(new_note)
    return NoteScheme(
        id=new_note.id, user_id=new_note.user_id, name=new_note.name, text=new_note.text
    )


async def all_notes(session: AsyncSession, user_id: int) -> list[int]:
    query = select(Note.id).where(Note.user_id == user_id)
    result = await session.execute(query)
    return [id for (id,) in result.all()]


async def get_one_note(
    note_id: int, session: AsyncSession, user_id: int
) -> NoteScheme | None:
    query = select(Note).where(Note.user_id == user_id).where(Note.id == note_id)
    result = await session.execute(query)
    note = result.scalar_one_or_none()
    if not note:
        raise HTTPException(status_code=400)
    return NoteScheme(id=note.id, name=note.name, text=note.text, user_id=note.user_id)
