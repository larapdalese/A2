import streamlit as st
import pandas as pd

# Criação do DataFrame
df = pd.DataFrame(
    [
       {"Nome da despesa": "Sephora", "Valor": 750.99, "Categoria": "beleza"},
       {"Nome da despesa": "Starbucks", "Valor": 36, "Categoria": "comida"},
       {"Nome da despesa": "Uber", "Valor": 15, "Categoria": "transporte"},
       {"Nome da despesa": "Saraiva", "Valor": 45.50, "Categoria": "livros"}
    ]
)

# Permitir edição da tabela no Streamlit
edited_df = st.data_editor(df, num_rows="dynamic")

# Encontrar a despesa com o maior valor
highest_expense = edited_df.loc[edited_df["Valor"].idxmax()]

st.write("Despesa de maior valor:")
st.write(highest_expense)
