import streamlit as st
import pandas as pd

# Criação do DataFrame com a nova coluna 'Data'
df = pd.DataFrame(
    [
       {"Nome da despesa": "Sephora", "Valor": 750.99, "Categoria": "beleza", "Data": "2024-10-01"},
       {"Nome da despesa": "Starbucks", "Valor": 36, "Categoria": "comida", "Data": "2024-10-02"},
       {"Nome da despesa": "Uber", "Valor": 15, "Categoria": "transporte", "Data": "2024-10-03"},
       {"Nome da despesa": "Saraiva", "Valor": 45.50, "Categoria": "livros", "Data": "2024-10-04"}
    ]
)

# Transformar a coluna 'Data' para o tipo datetime, caso deseje realizar manipulações de datas
df["Data"] = pd.to_datetime(df["Data"])

# Permitir edição da tabela no Streamlit
edited_df = st.data_editor(df, num_rows="dynamic")

# Encontrar a despesa com o maior valor
highest_expense = edited_df.loc[edited_df["Valor"].idxmax()]

st.write("Despesa de maior valor:")
st.write(highest_expense)
