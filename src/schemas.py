from datetime import datetime
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserCreate(BaseModel):
    username: str
    password: str


class TokenPayload(BaseModel):
    exp: int
    sub: str


class User(BaseModel):
    username: str


class UserCreate(User):
    password: str


class Request(BaseModel):
    prompt: str
