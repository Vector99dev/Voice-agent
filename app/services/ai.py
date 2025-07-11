import google.generativeai as genai
from langchain_core.messages import HumanMessage
import os
import asyncio
import google.auth
from google.auth import default
from google.cloud import aiplatform
from google.cloud.aiplatform_v1.types import Content, Part

class AIService:
    def __init__(self):
        aiplatform.init(
            project="elemental-day-443510-e0",
            location="us-central1"
        )
        self.model = "projects/elemental-day-443510-e0/locations/us-central1/publishers/google/models/gemini-2.5-flash"

    async def stream_chat_with_langchain(self, message: str):
        try:
            def predict_stream():
                prediction_client = aiplatform.gapic.PredictionServiceClient()
                
                # Create content for the request with proper role
                part = Part()
                part.text = message
                content = Content()
                content.parts = [part]
                content.role = "user"  # Specify the role as "user"
                
                # Stream the response
                stream = prediction_client.stream_generate_content(
                    model=self.model,
                    contents=[content]
                )
                
                for response in stream:
                    if response.candidates and response.candidates[0].content:
                        for part in response.candidates[0].content.parts:
                            if part.text:
                                yield part.text
                    
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(None, lambda: list(predict_stream()))
            for chunk in result:
                yield chunk
                await asyncio.sleep(0)
                    
        except Exception as e:
            yield f"[Error]: {str(e)}"

ai_service = AIService()
