from fastapi import FastAPI
from sqlalchemy import text


from src.db import db_session
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
async def read_root(db: db_session):
    result = await db.execute(text("SELECT 1"))
    return {"result": result.scalar()}
