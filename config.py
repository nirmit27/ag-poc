"""
Settings and configuration
"""

from os import path, getenv, makedirs
from dotenv import load_dotenv

import autogen_core.models as Models


load_dotenv()

try:
    # NOTE: Gemini setup
    GEMINI_MODEL = Models.ModelFamily.GEMINI_2_5_FLASH
    GOOGLE_API_KEY = getenv("GOOGLE_API_KEY", "")

    if len(GEMINI_MODEL) == 0 or len(GOOGLE_API_KEY) == 0:
        raise ValueError("Missing LLM configuration.")

    # NOTE: Directory paths
    OPDIR_PATH = path.join(path.dirname(path.abspath(__file__)), "output")
    makedirs(OPDIR_PATH, exist_ok=True)

    OP_PATH = path.join(OPDIR_PATH, "response.json")

except Exception as e:
    print(f"ERROR: {e}")
    exit(-1)
