from typing import override
from fastapi import FastAPI
from sqlalchemy import text
from starlette.responses import JSONResponse


from src.db import SessionDep
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware
from src.api.main import api_router
import logging

logger = logging.getLogger("uvicorn.error")

app = FastAPI()


@app.get("/")
async def root():
    return "Hello world"


@app.get("/test_db")
async def read_root(db: SessionDep):
    result = await db.execute(text("SELECT 1"))
    return {"result": result.scalar()}


app.include_router(api_router, prefix="/api")


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    @override
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
            return response
        except Exception as e:
            logger.error(f"Exception: {str(e)}")
            return JSONResponse(
                status_code=500, content={"detail": "Internal Server Error"}
            )


app.add_middleware(ExceptionHandlingMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080",
        "http://localhost:8081",
        "http://127.0.0.1:8081",
        "quartz-notes.github.io",
        "localhost:5173",
    ],  # Allows CORS from this origin
    allow_credentials=True,  # Allows cookies and credentials
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all HTTP headers
)
