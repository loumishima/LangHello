from src.llm.prompt import get_prompt_template
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_retrieval_chain
from src.llm.model import get_llm


def create_qa_chain(retriever):
    llm = get_llm()

    prompt = get_prompt_template()

    output_parser = StrOutputParser()

    return create_retrieval_chain(
        retriever=retriever, combine_docs_chain=prompt | llm | output_parser
    )
