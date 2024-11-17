 pip install transformers
from transformers import pipeline

def criar_maria():
    # Carrega um pipeline de conversação com o modelo GPT-2.
    assistente = pipeline("text-generation", model="gpt2")
    
    # Interface simples da assistente.
    print("Oi, eu sou a Maria Clara, sua assistente financeira virtual! Como posso ajudar hoje?")
    while True:
        entrada = input("Você: ")
        if entrada.lower() in ["sair", "tchau", "até mais"]:
            print("Maria Clara: Foi um prazer ajudar! Até a próxima!")
            break
        resposta = assistente(entrada, max_length=50, num_return_sequences=1)
        print("Maria Clara:", resposta[0]['generated_text'][len(entrada):].strip())

# Cria a assistente virtual Maria Clara.
criar_maria()
```
