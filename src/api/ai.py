from fastapi import APIRouter

from src.settings import settings


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


@router.post("/parse")
async def ai_parse(request: Request):
    response = await parse_model.generate_content_async(request.prompt)
    if settings.ENVIRONMENT == "local":
        print(request.prompt, response.text)
    return json.loads(response.text)


@router.post(path="/summarize")
async def ai_summarize(request: Request) -> Any:
    response = await summarize_model.generate_content_async(request.prompt)
    if settings.ENVIRONMENT == "local":
        print(request.prompt, response.text)
    return json.loads(response.text)


@router.post(path="/tags")
async def ai_tags(prompt: str):
    return ["tag1", "tag2", "tag3"]
