from google import genai
from typing import Optional

class AIService:
    def __init__(self):
        self.client = genai.Client(
            vertexai=True,
            project="elemental-day-443510-e0",
            location="us-central1"
        )
    
    async def chat_with_gemini(self, message: str, model: str = "gemini-2.5-flash") -> dict:
        """
        Send a message to Gemini AI and get a response
        
        Args:
            message (str): The message to send to Gemini
            model (str): The model to use (default: gemini-2.5-flash)
            
        Returns:
            dict: Response containing the AI response or error
        """
        try:
            response = self.client.models.generate_content(
                model=model,
                contents=message,
            )
            return {"response": response.text, "success": True}
        except Exception as e:
            return {"error": str(e), "success": False}
    
    async def test_gemini(self) -> dict:
        """
        Test the Gemini AI connection with a simple message
        
        Returns:
            dict: Response containing the test result
        """
        return await self.chat_with_gemini("Hello, how are you?")

# Create a singleton instance
ai_service = AIService()
