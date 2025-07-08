import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

FASTAPI_URL = os.getenv("FASTAPI_URL")

st.title("Simulador de ChatGPT")

st.title("Welcome!")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Carrega a memória salva da sessão
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


llm_input = {}
if prompt := st.chat_input("Say something..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    llm_input = {"input": prompt}
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Trocar por chamada ao FASTApi com LangChain Agent.
    llm_response = requests.post(f"{FASTAPI_URL}/llm", json=llm_input)

    response = llm_response.json()["answer"]
    with st.chat_message("ai"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
