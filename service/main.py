import os
import asyncio
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm # For multi-model support
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types # For creating message Content/Parts

import warnings
warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

from core.logger import logger
from agents.master_agent import MasterAgent

os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "False"

if __name__ == "__main__":
    logger.info("Nexa system starting...")

    master = MasterAgent()

    while True:
        try:
            user_input = input("\n🎙️  You: ")
            if user_input.lower() in {"exit", "quit"}:
                print("👋 Bye!")
                break

            task = {"text": user_input}
            response = master.execute(task)
            print("🤖 Nexa:", response["response"])

        except Exception as e:
            logger.exception(f"Unhandled error: {e}")
            print("⚠️ Something went wrong.")
