from fastapi import APIRouter, HTTPException

from src import crud
from src.db import SessionDep
from src.schemas import UserCreate


router = APIRouter(tags=["users"])


@router.post("/")
async def create_user_(session: SessionDep, user_in: UserCreate):
    user = await crud.get_user_by_username(db=session, username=user_in.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this username already exists in the system.",
        )
    user = await crud.create_user(
        username=user_in.username, password=user_in.password, db=session
    )
    return {"id": user.id, "username": user.username}
