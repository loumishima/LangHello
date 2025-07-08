from fastapi import FastAPI, Body
from src.vector_store.get_store import get_vectorstore
from src.chains.retrieval_qa import create_qa_chain
from pydantic import BaseModel


class PromptMessage(BaseModel):
    input: str


app = FastAPI()


@app.post("/llm")
def talk(text: PromptMessage):
    input = text.input
    print(input)
    # create_vectorstore()
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever()

    chain = create_qa_chain(retriever)

    response = chain.invoke({"input": input})

    return response
