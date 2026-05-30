import os
from pathlib import Path

from dotenv import load_dotenv

_ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(_ENV_PATH, override=True)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if OPENAI_API_KEY:
	os.environ.setdefault("OPENAI_API_KEY", OPENAI_API_KEY)

# Do not print sensitive information such as API key lengths in logs.

SERVER_API_KEY = os.getenv("SERVER_API_KEY")

PORT = int(os.getenv("PORT"))

OPENAI_MODEL = "gpt-4o-mini"

API_VERSION = "v0"

ERROR_MESSAGE = "We are facing an issue, please try after sometimes."
