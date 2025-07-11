from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.services.ai import ai_service
import asyncio

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.get("/")
async def chat_root():
    return {"message": "Chat endpoint root"}

@router.get("/test-gemini")
async def test_gemini():
    """
    Test endpoint that redirects to AI service for Gemini testing
    """
    return await ai_service.test_gemini()

async def stream_gemini_response(message: str):
    result = await ai_service.chat_with_gemini(message)
    text = result.get("response", "")
    # Simulate streaming by yielding one character at a time
    for char in text:
        yield char
        await asyncio.sleep(0.01)  # Simulate typing speed

@router.post("/chat")
async def chat_with_ai(request: ChatRequest):
    """
    Chat endpoint that streams Gemini chat response
    """
    return StreamingResponse(stream_gemini_response(request.message), media_type="text/plain")