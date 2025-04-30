import uuid
from fastapi import APIRouter

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
def create_note(current_user: CurrentUser):  # pyright: ignore[reportUnusedParameter]
    return "meow"


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
