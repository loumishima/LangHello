from src.vector_store.get_store import get_vectorstore
from src.chains.retrieval_qa import create_qa_chain

if __name__ == "__main__":
    # Cria o vectorstore (só na primeira vez)
    # vector store deveria ser um singleton!
    # INFO: comentar logo em seguida

    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever()

    chain = create_qa_chain(retriever)

    while True:
        query = input("Faça sua pergunta (ou 'sair'): ")
        if query.lower() in ["sair", "quit", "exit"]:
            break
        response = chain.invoke({"input": query})
        print("\nResposta:", response["answer"], "\n")
