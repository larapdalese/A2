### Alinne

import streamlit as st
import requests
import os
from groq import Groq

st.title('Maria Clara - CHATBOT')

api_key = os.environ.get("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")
url = "https://api.groq.com/openai/v1/models"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
response.json()

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Você é uma assistente de educação financeira para mulheres. Seu nome é Maria Clara, então,
            é assim que você vai se apresentar, juntamente com sua função: assistente do Feminance, um aplicativo de
            educação financeira e finanças. Quando o usuário perguntar algo, sempre o chame de 'diva' e também, ao 
            final da resposta, diga que espera ter ajudado e que deseja muito $uce$$o."
        },
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    stop=None,
    stream=False,
)

str.write(chat_completion.choices[0].message.content)

### Alinne

# pip install transformers
#from transformers import pipeline

#def criar_maria():
    # Carrega um pipeline de conversação com o modelo GPT-2.
#    assistente = pipeline("text-generation", model="gpt2")
    
    # Interface simples da assistente.
#    print("Oi, eu sou a Maria Clara, sua assistente financeira virtual! Como posso ajudar hoje?")
#    while True:
#        entrada = input("Você: ")
#        if entrada.lower() in ["sair", "tchau", "até mais"]:
#            print("Maria Clara: Foi um prazer ajudar! Até a próxima!")
#            break
#        resposta = assistente(entrada, max_length=50, num_return_sequences=1)
#        print("Maria Clara:", resposta[0]['generated_text'][len(entrada):].strip())

# Cria a assistente virtual Maria Clara.
#criar_maria()
#```
