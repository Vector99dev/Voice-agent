from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.ai import ai_service

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

@router.post("/chat")
async def chat_with_ai(request: ChatRequest):
    """
    Chat endpoint that redirects to AI service for Gemini chat
    """
    return await ai_service.chat_with_gemini(request.message)