import os
import google.generativeai as genai
from src.settings import settings
from src.services.ai.instructions import parse_instructions, summarize_instructions

genai.configure(api_key=settings.GEMINI_API)

# Create the model
parse_config = {
    "temperature": 0.5,
    "top_p": 0.7,
    "top_k": 40,
    "max_output_tokens": 4096,
    "response_mime_type": "application/json",
}
summarize_config = {
    "temperature": 0.3,
    "top_p": 0.5,
    "top_k": 20,
    "max_output_tokens": 2048,
    "response_mime_type": "application/json",
    # "response_mime_type": "text/plain",
}


parse_model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=parse_config,
    system_instruction=parse_instructions,
)

summarize_model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=summarize_config,
    system_instruction=summarize_instructions,
)
