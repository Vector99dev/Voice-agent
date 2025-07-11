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

async def stream_langchain_response(message: str):
    async for chunk in ai_service.stream_chat_with_langchain(message):
        yield chunk
        await asyncio.sleep(0)  # Yield control to event loop

@router.post("/chat")
async def chat_with_ai(request: ChatRequest):
    """
    Chat endpoint that streams Gemini chat response via LangChain
    """
    return StreamingResponse(stream_langchain_response(request.message), media_type="text/plain")