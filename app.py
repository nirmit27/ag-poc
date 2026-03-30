"""
AutoGen - DEMO
"""

import asyncio
from json import dump
# from pprint import pprint

from autogen_core.models import UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient

from config import *


# TODO: Run the agent and stream the messages to the console.
async def main():
    user_prompt = (
        "Explain the first law of thermodynamics in the most concise way possible."
    )

    model_client = OpenAIChatCompletionClient(
        model=GEMINI_MODEL,
        api_key=GOOGLE_API_KEY,
    )

    response = await model_client.create(
        [UserMessage(content=user_prompt, source="user")]
    )

    with open(OP_PATH, "w") as fp:
        dump(response.content, fp)

    await model_client.close()


# Driver
if __name__ == "__main__":
    asyncio.run(main())
