import getpass
import os
from langchain.chat_models import init_chat_model


def get_llm():
    return init_chat_model("gpt-4o", model_provider="openai")
