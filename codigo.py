import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Orçamento Mensal", layout="wide")

# Criar DataFrame de despesas
df = pd.DataFrame(
    [
        {"Nome da despesa": "Sephora", "Valor": 750.99, "Categoria": "beleza", "Data": "2024-01-15"},
        {"Nome da despesa": "Farmácia", "Valor": 125.50, "Categoria": "saúde", "Data": "2024-01-28"},
        {"Nome da despesa": "Starbucks", "Valor": 36, "Categoria": "comida", "Data": "2024-02-05"},
        {"Nome da despesa": "Restaurante", "Valor": 80, "Categoria": "comida", "Data": "2024-02-18"},
        {"Nome da despesa": "Uber", "Valor": 15, "Categoria": "transporte", "Data": "2024-03-12"},
        {"Nome da despesa": "Táxi", "Valor": 25, "Categoria": "transporte", "Data": "2024-03-30"},
        {"Nome da despesa": "Saraiva", "Valor": 45.50, "Categoria": "livros", "Data": "2024-04-10"},
        {"Nome da despesa": "Livraria Cultura", "Valor": 60, "Categoria": "livros", "Data": "2024-04-25"},
        {"Nome da despesa": "Cinema", "Valor": 50, "Categoria": "lazer", "Data": "2024-05-15"},
        {"Nome da despesa": "Teatro", "Valor": 120, "Categoria": "lazer", "Data": "2024-05-20"},
        {"Nome da despesa": "Academia", "Valor": 200, "Categoria": "fitness", "Data": "2024-06-05"},
        {"Nome da despesa": "Yoga", "Valor": 150, "Categoria": "fitness", "Data": "2024-06-22"},
        {"Nome da despesa": "Pet Shop", "Valor": 80, "Categoria": "pets", "Data": "2024-07-11"},
        {"Nome da despesa": "Veterinário", "Valor": 300, "Categoria": "pets", "Data": "2024-07-25"},
        {"Nome da despesa": "Roupas", "Valor": 500, "Categoria": "vestuário", "Data": "2024
