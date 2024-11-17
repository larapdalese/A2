### Alinne

import streamlit as st
import requests
import os

st.set_page_config(page_title="Maria Clara - CHATBOT")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Como posso te ajudar hoje, diva?"}]

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

    try:
        response = requests.post(
            url,
            headers=headers,
            json={
                "model": "llama3-8b-8192", 
                "messages": messages + [{"role": "user", "content": prompt_input}],
                "temperature": 0.5,
                "max_tokens": 1024,
                "top_p": 1,
                "stop": None,
                "stream": False 
            }
        )

        if response.status_code == 200:
            response_data = response.json()
            if 'choices' in response_data and len(response_data['choices']) > 0:
                return response_data['choices'][0]['message']['content']
            else:
                return "Resposta não encontrada ou formato inesperado."
        else:
            return f"Erro na API Groq: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Erro ao chamar a API Groq: {str(e)}"

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Como posso te ajudar hoje, diva?"}]
st.sidebar.button('Limpar histórico de chat', on_click=clear_chat_history)

if prompt := st.chat_input("Digite sua pergunta:"):
    st.session_state.messages.append({"role": "user", "content": prompt}) 
    with st.chat_message("user"):
        st.write(prompt) 

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."): 
            response = generate_groq_response(prompt)
            st.write(response)

    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)

### Alinne
