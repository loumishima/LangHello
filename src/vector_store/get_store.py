from langchain_qdrant import Qdrant
from qdrant_client import QdrantClient
from src.llm.embeddings import get_embeddings
from src.data_ingestion.loader import load_documents
from src.data_ingestion.splitter import split_documents

QDRANT_COLLECTION_NAME = "meus_dados"


def get_vectorstore():
    documents = load_documents()
    docs = split_documents(documents)

    embeddings = get_embeddings()

    # Conecta no Qdrant
    client = QdrantClient(host="qdrant", port=6333)
    # client = QdrantClient(path=":memory:")

    # Cria ou conecta o vectorstore no Qdrant
    vectorstore = Qdrant.from_documents(
        docs,
        embeddings,
        collection_name=QDRANT_COLLECTION_NAME,
        url="http://qdrant:6333",
        # path=":memory:",
    )

    print(f"Collection '{QDRANT_COLLECTION_NAME}' criada no Qdrant.")

    return vectorstore
