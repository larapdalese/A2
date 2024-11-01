import streamlit as st 
import pandas as pd
import plotly.express as px

# Configurar a página para o layout expandido
st.set_page_config(layout="wide")

# CSS para reduzir margens laterais
st.markdown("""
    <style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
        max-width: 100%;
    }
    .css-1lcbmhc, .css-1fcdlh8 {
        max-width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# DataFrame de despesas
df = pd.DataFrame([
    {"Nome da despesa": "Sephora", "Data": "2024-01-15", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 750.99},
    {"Nome da despesa": "Farmácia", "Data": "2024-01-28", "Categoria": "saúde", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 125.50},
    {"Nome da despesa": "Starbucks", "Data": "2024-02-05", "Categoria": "comida", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 36},
    # ... (adicione o restante das despesas aqui)
])

# Entrada de orçamento mensal
st.header("Orçamento do mês:")
orcamento = st.number_input("Digite seu orçamento mensal:", min_value=0.0, format="%.2f", step=100.0)

# Mostrar despesas com filtros
st.header("Despesas")
opcao_visualizacao = st.selectbox("Visualizar despesas por:", ["Todas as Despesas", "Por mês", "Por categoria"])

if opcao_visualizacao == "Todas as Despesas":
    st.write(df)

elif opcao_visualizacao == "Por mês":
    df['Data'] = pd.to_datetime(df['Data'])
    df['Mês'] = df['Data'].dt.strftime('%Y-%m')
    mes_selecionado = st.selectbox("Selecione o mês:", df['Mês'].unique())
    despesas_mes = df[df['Mês'] == mes_selecionado]
    st.write(despesas_mes)

elif opcao_visualizacao == "Por categoria":
    categoria_selecionada = st.selectbox("Selecione a categoria:", df['Categoria'].unique())
    despesas_categoria = df[df['Categoria'] == categoria_selecionada]
    st.write(despesas_categoria)

# Total de gastos e saldo
total_gastos = df['Valor'].sum()
saldo = orcamento - total_gastos

st.markdown(f"### Total de gastos: R$ {total_gastos:.2f}")
st.markdown(f"### Saldo restante: R$ {saldo:.2f}")
