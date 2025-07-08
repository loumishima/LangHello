from langchain.embeddings.base import init_embeddings


def get_embeddings():
    return init_embeddings("text-embedding-ada-002", provider="openai")
