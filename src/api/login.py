from datetime import timedelta
from typing import Annotated
from src.settings import settings
from src.db import SessionDep
from src.schemas import Token, User
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src.security import CurrentUser, create_access_token
from src.crud import authenticate


router = APIRouter(tags=["login"])


@router.post("/login/access-token", response_model=Token)
async def login_access_token(
    session: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = await authenticate(
        session=session,
        username=form_data.username,
        password=form_data.password,
    )
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(user.id, expires_delta=access_token_expires)

    return Token(access_token=access_token)


@router.post("/login/test-token")
def test_token(current_user: CurrentUser) -> User:
    return User(username=current_user.username)
