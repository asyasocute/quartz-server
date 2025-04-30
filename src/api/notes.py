import uuid
from fastapi import APIRouter

from src.crud import add_note
from src.db import SessionDep
from src.schemas import NoteCreate, NoteScheme
from src.security import CurrentUser


router = APIRouter(tags=["notes"])


@router.get("/")
def get_note(
    note_id: int, current_user: CurrentUser  # pyright: ignore[reportUnusedParameter]
):
    return "meow"


@router.get("/all")
def get_notes(current_user: CurrentUser):  # pyright: ignore[reportUnusedParameter]
    return "meow"


@router.post("/create")
async def create_note(
    new_note: NoteCreate,
    current_user: CurrentUser,  # pyright: ignore[reportUnusedParameter]
    session: SessionDep,
) -> NoteScheme:
    return await add_note(session=session, note=new_note, user_id=current_user.id)


@router.patch("/edit")
def edit_note(
    note_id: int, current_user: CurrentUser  # pyright: ignore[reportUnusedParameter]
):
    return "meow"


@router.post("/delete")
def delete_note(
    note_id: int, current_user: CurrentUser  # pyright: ignore[reportUnusedParameter]
):
    return "meow"


@router.post("/tags")
def tags(
    note_id: int, current_user: CurrentUser  # pyright: ignore[reportUnusedParameter]
):
    return ["currently not working", "tag1", "tag2", "tag3"]
