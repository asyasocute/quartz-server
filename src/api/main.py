from fastapi import APIRouter
from . import login
from . import users

api_router = APIRouter()
api_router.include_router(login.router)
api_router.include_router(users.router)
