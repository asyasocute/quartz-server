from typing import Literal


import uuid
from fastapi import APIRouter

from src.crud import add_note, all_notes, delete_note, edit_note, get_one_note
from src.db import SessionDep
from src.models import note
from src.schemas import NoteCreate, NoteScheme
from src.security import CurrentUser


router = APIRouter(tags=["notes"])


@router.get("/")
async def get_note(
    note_id: int,
    current_user: CurrentUser,
    session: SessionDep,
):
    return await get_one_note(note_id=note_id, session=session, user_id=current_user.id)


@router.get("/all")
async def get_notes(
    current_user: CurrentUser,
    session: SessionDep,
) -> list[int]:

    return await all_notes(session=session, user_id=current_user.id)


@router.post("/create")
async def create_note(
    new_note: NoteCreate,
    current_user: CurrentUser,
    session: SessionDep,
) -> NoteScheme:
    return await add_note(session=session, note=new_note, user_id=current_user.id)


@router.patch("/edit")
async def edit_notes(
    note_id: int,
    new_note: NoteCreate,
    session: SessionDep,
    current_user: CurrentUser,
) -> NoteScheme:
    return await edit_note(
        session=session, note=new_note, note_id=note_id, user_id=current_user.id
    )


@router.post("/delete")
async def delete_notes(
    note_id: int,
    session: SessionDep,
    current_user: CurrentUser,
) -> None:
    return await delete_note(note_id=note_id, session=session, user_id=current_user.id)


@router.post("/tags")
async def tags(
    note_id: int,  # pyright: ignore[reportUnusedParameter]
    session: SessionDep,  # pyright: ignore[reportUnusedParameter]
    current_user: CurrentUser,  # pyright: ignore[reportUnusedParameter]
):
    return ["currently not working", "tag1", "tag2", "tag3"]
