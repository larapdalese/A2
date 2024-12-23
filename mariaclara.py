### Alinne

import streamlit as st
from groq import Groq

st.set_page_config(page_title="Maria Clara - CHATBOT")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Oi, meu nome é Maria Clara! Como posso te ajudar hoje?"}]

api_key = "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"

def generate_groq_response(prompt_input):
    client = Groq(api_key=api_key)

    messages = [
        {"role": "system", "content": (
            "Você é uma assistente de educação financeira para mulheres chamada Maria Clara. "
            "Seu objetivo é ajudar as usuárias com dúvidas sobre finanças, explicando conceitos financeiros "
            "de maneira clara e oferecendo conselhos úteis. Sempre forneça respostas completas e evite fazer muitas perguntas. "
            "Tente explicar o máximo possível e se necessário, forneça exemplos. "
            "Ao final de cada resposta, diga que espera ter ajudado e deseja sucesso na jornada financeira."
        )}
    ]

    for dict_message in st.session_state.messages:
        messages.append(dict_message)

    messages.append({"role": "user", "content": prompt_input})

    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-groq-8b-8192-tool-use-preview",
            temperature=0.5,
            max_tokens=3000,
            top_p=0.9,
            stop=[],
            stream=None,
        )

        return chat_completion.choices[0].message.content

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
