import streamlit as st
import pandas as pd

# Criação do DataFrame com a coluna 'Data' em meses diferentes
df = pd.DataFrame(
    [
       {"Nome da despesa": "Sephora", "Valor": 750.99, "Categoria": "beleza", "Data": "2024-01-15"},
       {"Nome da despesa": "Starbucks", "Valor": 36, "Categoria": "comida", "Data": "2024-02-20"},
       {"Nome da despesa": "Uber", "Valor": 15, "Categoria": "transporte", "Data": "2024-03-10"},
       {"Nome da despesa": "Saraiva", "Valor": 45.50, "Categoria": "livros", "Data": "2024-04-05"}
    ]
)

# Converter a coluna 'Data' para o tipo datetime
df["Data"] = pd.to_datetime(df["Data"])

# Criar uma lista dos meses disponíveis no DataFrame
meses_disponiveis = df["Data"].dt.strftime("%Y-%m").unique()

# Selecionar o mês desejado pelo usuário
mes_selecionado = st.selectbox("Selecione o mês (AAAA-MM):", meses_disponiveis)

# Filtrar o DataFrame pelo mês selecionado
despesas_filtradas = df[df["Data"].dt.strftime("%Y-%m") == mes_selecionado]

# Exibir o DataFrame filtrado
st.write("Despesas do mês selecionado:")
st.write(despesas_filtradas)
