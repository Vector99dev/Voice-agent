#!/usr/bin/env python3
"""Check which Vertex AI models are available"""

def check_model_availability():
    """Test which models are actually available"""
    
    models_to_test = [
        "gemini-1.0-pro",
        "gemini-1.5-pro", 
        "gemini-1.5-flash",
        "gemini-pro",
        "chat-bison@001",
        "text-bison@001"
    ]
    
    print("🔍 Testing Model Availability in Vertex AI")
    print("=" * 50)
    
    for model in models_to_test:
        try:
            from vertexai.language_models import ChatModel
            import vertexai
            
            # Initialize Vertex AI
            vertexai.init(project="elemental-day-443510-e0", location="us-central1")
            
            # Try to load the model
            chat_model = ChatModel.from_pretrained(model)
            print(f"✅ {model} - AVAILABLE")
            
        except Exception as e:
            error_msg = str(e)
            if "not found" in error_msg.lower():
                print(f"❌ {model} - NOT AVAILABLE")
            else:
                print(f"⚠️ {model} - ERROR: {error_msg[:80]}")
    
    print("\n📋 Summary:")
    print("- If you see ✅ AVAILABLE → You can use that model")
    print("- If you see ❌ NOT AVAILABLE → Model not available in your region")
    print("- If you see ⚠️ ERROR → There might be a setup issue")

if __name__ == "__main__":
    check_model_availability() 