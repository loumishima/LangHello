from langchain_community.document_loaders import DirectoryLoader
from src.config.config import DOCS_PATH


def load_documents():
    loader = DirectoryLoader(str(DOCS_PATH))
    return loader.load()
