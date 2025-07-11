#!/usr/bin/env python3
"""List all available models in Vertex AI"""

from google.cloud import aiplatform

def list_available_models():
    """List all available models in your project"""
    project = "elemental-day-443510-e0"
    location = "us-central1"
    
    try:
        # Initialize Vertex AI
        aiplatform.init(project=project, location=location)
        
        # List available models
        client = aiplatform.gapic.ModelServiceClient(
            client_options={"api_endpoint": f"{location}-aiplatform.googleapis.com"}
        )
        
        parent = f"projects/{project}/locations/{location}"
        models = client.list_models(parent=parent)
        
        print(f"🔍 Available models in {project}/{location}:")
        print("=" * 50)
        
        for model in models:
            print(f"📋 Model: {model.display_name}")
            print(f"   ID: {model.name}")
            print(f"   Description: {model.description}")
            print("-" * 30)
            
    except Exception as e:
        print(f"❌ Error listing models: {e}")

if __name__ == "__main__":
    list_available_models() 