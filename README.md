# Voice AI Agent Backend

This is a best-practice FastAPI backend structure for a Voice AI Agent system. It is modular, scalable, and ready for integration with AI, TTS, and STT services.

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI app instance, router includes, startup logic
│   ├── api/
│   │   ├── __init__.py
│   │   └── endpoints/
│   │       ├── __init__.py
│   │       ├── chat.py        # Endpoints for chat/voice (REST & WebSocket)
│   │       └── health.py      # Health check endpoint
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Settings, environment variables
│   │   └── security.py        # CORS, authentication, etc.
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ai.py              # Vertex AI / LangChain logic
│   │   ├── tts.py             # ElevenLabs TTS logic
│   │   ├── stt.py             # LiveKit or other STT logic
│   │   └── property.py        # Real estate property search logic (if needed)
│   ├── models/
│   │   ├── __init__.py
│   │   ├── schemas.py         # Pydantic models for requests/responses
│   │   └── db.py              # SQLAlchemy models (if using a DB)
│   ├── db/
│   │   ├── __init__.py
│   │   ├── session.py         # DB session/engine setup
│   │   └── crud.py            # CRUD operations
│   └── utils/
│       ├── __init__.py
│       └── helpers.py         # Utility functions
├── tests/
│   ├── __init__.py
│   └── test_chat.py           # Example test file
├── requirements.txt
├── README.md
├── .env                       # Environment variables (never commit real secrets)
└── start.sh                   # Startup script (optional)
```

## Setup

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

## Notes
- Place your API endpoints in `app/api/endpoints/`.
- Add business logic and integrations in `app/services/`.
- Use `.env` for environment variables and secrets.
- Add tests in the `tests/` directory. 