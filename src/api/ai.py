from fastapi import APIRouter


router = APIRouter(tags=["ai"])


@router.get("/summarize")
async def summarize():
    return "ping"


@router.get("/tags")
async def tags_for_note():
    return "ping"


@router.get(path="/generate")
async def generate():
    return "ping"
