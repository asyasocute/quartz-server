from fastapi import FastAPI
from sqlalchemy import text


from src.db import SessionDep
from src.settings import settings
from src.api.main import api_router

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
async def read_root(db: SessionDep):
    result = await db.execute(text("SELECT 1"))
    return {"result": result.scalar()}


app.include_router(api_router, prefix="/api")
