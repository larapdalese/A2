import streamlit as st
import pandas as pd
df = pd.DataFrame(
    [
       {"Nome da despesa": "Sephora", "Valor": 750.99, "Categoria": "beleza", "Data": "2024-01-15"},
       {"Nome da despesa": "Starbucks", "Valor": 36, "Categoria": "comida", "Data": "2024-02-20"},
       {"Nome da despesa": "Uber", "Valor": 15, "Categoria": "transporte", "Data": "2024-03-10"},
       {"Nome da despesa": "Saraiva", "Valor": 45.50, "Categoria": "livros", "Data": "2024-04-05"}
    ]
)
df["Data"] = pd.to_datetime(df["Data"]).dt.date
meses_disponiveis = ["Tudo"] + list(pd.to_datetime(df["Data"]).dt.strftime("%Y-%m").unique())
mes_selecionado = st.selectbox("Selecione o mês da despesa ou 'Tudo' para ver todas!!", meses_disponiveis)
if mes_selecionado == "Tudo":
    despesas_filtradas = df
else:
    despesas_filtradas = df[pd.to_datetime(df["Data"]).dt.strftime("%Y-%m") == mes_selecionado]
st.write("Despesas do mês selecionado:")
st.write(despesas_filtradas)

