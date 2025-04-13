from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.db import get_db
from src.settings import settings

app = FastAPI()


def hello():
    print("Hello world")


@app.get("/")
async def root():
    return "Hello world"


@app.get("/env")
async def envv():
    return settings.model_dump()


@app.get("/test_db")
async def read_root(db: AsyncSession = Depends(get_db)):
    result = await db.execute(text("SELECT 1"))
    return {"result": result.scalar()}
