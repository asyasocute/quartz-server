from fastapi import APIRouter
from . import login
from . import users
from . import notes
from . import ai

api_router = APIRouter()
api_router.include_router(prefix="/login", router=login.router)
api_router.include_router(prefix="/users", router=users.router)
api_router.include_router(prefix="/notes", router=notes.router)
api_router.include_router(prefix="/ai", router=ai.router)
