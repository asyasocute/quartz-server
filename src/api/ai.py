import json
from fastapi import APIRouter

from src.exceptions import GeminiApiException
from src.schemas import Request
from src.security import CurrentUser
from src.settings import settings
from src.services.ai.gemini import parse_model, summarize_model


router = APIRouter(tags=["ai"])


# @router.get("/summarize")
# async def summarize():
#     return "ping"


# @router.get("/tags")
# async def tags_for_note():
#     return "ping"


# @router.get(path="/generate")
# async def generate():
#     return "ping"


@router.post("/parse")
async def ai_parse(request: Request, current_user: CurrentUser):
    try:
        response = await parse_model.generate_content_async(request.prompt)
    except:
        return GeminiApiException()
    if settings.ENVIRONMENT == "local":
        print(request.prompt, response.text)
    return json.loads(response.text)


@router.post(path="/summarize")
async def ai_summarize(request: Request, current_user: CurrentUser):
    try:
        response = await summarize_model.generate_content_async(request.prompt)
    except:
        return GeminiApiException()
    if settings.ENVIRONMENT == "local":
        print(request.prompt, response.text)
    return json.loads(response.text)
