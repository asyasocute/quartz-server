from statistics import median_low
from fastapi.security.oauth2 import OAuth2PasswordBearer


from datetime import datetime, timedelta, timezone
from typing import Annotated, Any

from fastapi import Depends, HTTPException
import jwt
from passlib.context import CryptContext
from sqlalchemy.sql import select


from src.schemas import TokenPayload, User
from src.models.user import User as UserModel
from src.settings import settings
from src.db import SessionDep

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(subject: str | Any, expires_delta: timedelta) -> str:
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


reusable_oauth2: OAuth2PasswordBearer = OAuth2PasswordBearer(
    tokenUrl=f"/api/login/access-token"
)
TokenDep = Annotated[str, Depends(reusable_oauth2)]


async def get_current_user(session: SessionDep, token: TokenDep):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
        if datetime.fromtimestamp(token_data.exp, tz=timezone.utc) < datetime.now(
            timezone.utc
        ):
            raise HTTPException(
                status_code=401,
                detail="Token expired",
            )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
        )

    query = select(UserModel).where(UserModel.id == int(token_data.sub))
    result = await session.execute(query)
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
