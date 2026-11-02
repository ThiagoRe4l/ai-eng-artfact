import os
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = os.getenv("MODEL_ID", "google_genai:gemini-3.5-flash-lite")
AGENT_MODEL_ID = os.getenv("AGENT_MODEL_ID", "google_genai:gemini-3.8-flash")

def validate_environment() -> None:
    required = (
        "GOOGLE_API_KEY",
    )
    missing = [name for name in required if not os.getenv(name)]
    if missing:
        raise RuntimeError(
            "Define it in your .env file (see the .env.example): " + ", ".join(missing) + "."
        )