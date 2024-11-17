### Alinne

import streamlit as st
import requests
import os

st.set_page_config(page_title="Maria Clara - CHATBOT")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Como posso te ajudar hoje, diva?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Como posso te ajudar hoje, diva?"}]
st.sidebar.button('Limpar histórico de chat', on_click=clear_chat_history)

def generate_groq_response(prompt_input):
    api_key = os.environ.get("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")
    url = "https://api.groq.com/openai/v1/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    messages = [
        {"role": "system", "content": (
            "Você é uma assistente de educação financeira para mulheres. Seu nome é Maria Clara, "
            "então é assim que você vai se apresentar, juntamente com sua função: assistente do Feminance, "
            "um aplicativo de educação financeira e finanças. Quando o usuário perguntar algo, sempre o chame de "
            "'diva' e também, ao final da resposta, diga que espera ter ajudado e que deseja muito $uce$$o."
        )}
    ]
    for dict_message in st.session_state.messages:
        messages.append(dict_message)

    response = requests.post(
        url, 
        headers=headers,
        json={
            "model": "llama3-8b-8192",  # Substitua com o modelo desejado
            "messages": messages + [{"role": "user", "content": prompt_input}],
            "temperature": 0.5,
            "max_tokens": 1024,
            "top_p": 1,
            "stop": None,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Erro ao obter resposta: {response.status_code}"

if prompt := st.chat_input("Digite sua pergunta:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                response = generate_groq_response(prompt)
                placeholder = st.empty()
                full_response = ''
                for item in response:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)

        message = {"role": "assistant", "content": full_response}
        st.session_state.messages.append(message)

### Alinne
