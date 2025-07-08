from langchain.prompts import PromptTemplate


def get_prompt_template():
    template = """
    Você é um assistente que auxilia o usuário a lembrar dos dados pessoas dele e
    responde baseado no contexto abaixo.

    Contexto:
    {context}

    Pergunta:
    {input}

    Responda de forma completa.
    """
    return PromptTemplate(template=template, input_variables=["context", "input"])
