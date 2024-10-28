import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"Nome da despesa": "Sephora", "Valor": 750.99, "Categoria": "beleza"},
       {"Nome da despesa": "Starbucks", "Valor": 36, "Categoria": "comida"},
       {"Nome da despesa": "Uber", "Valor": 15, "Categoria": "transporte"},
       {"Nome da despesa": "Saraiva", "Valor": 45.50, "Categoria": "livros"}
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]

