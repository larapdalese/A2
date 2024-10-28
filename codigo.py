import streamlit as st
import pandas as pd

df = pd.DataFrame(
    [
       {"Nome da despesa": "Sephora", "Valor": 750.99, "Categoria": beleza , "Data": 31/01/2024},
       {"Nome da despesa": "Starbucks", "Valor": 36, "Categoria": comida, "Data": 25/02/2024},
       {"Nome da despesa": "Uber", "Valor": 15, "Categoria": transporte, "Data": 30/03/2024},
       {"Nome da despesa": "Saraiva", "Valor": 45.50, "Categoria": livros, "Data": 04/04/2024}
   ]
)
edited_df = st.data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]

