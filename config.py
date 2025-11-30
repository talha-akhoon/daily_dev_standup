from dotenv import load_dotenv
import os

load_dotenv()

USE_OPENAI = os.getenv("USE_OPENAI", "false").lower() == "true"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_TOKEN = os.getenv("HF_TOKEN")
