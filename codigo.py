import streamlit as st
import pandas as pd
import plotly.express as px

# Configurar a página para o layout expandido
st.set_page_config(layout="wide")

# Estilo CSS para reduzir margens laterais e expandir área de exibição
st.markdown("""
    <style>
    /* Expandir o container principal */
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
        max-width: 100%;
    }
    /* Expandir visualização dos gráficos e dataframes */
    .css-1lcbmhc, .css-1fcdlh8 {
        max-width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Criar DataFrame de despesas
df = pd.DataFrame(
    [
        {"Nome da despesa": "Sephora", "Data": "2024-01-15", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 750.99},
        {"Nome da despesa": "Farmácia", "Data": "2024-01-28", "Categoria": "saúde", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 125.50},
        {"Nome da despesa": "Starbucks", "Data": "2024-02-05", "Categoria": "comida", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 36},
        {"Nome da despesa": "Restaurante", "Data": "2024-02-18", "Categoria": "comida", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 80},
        {"Nome da despesa": "Uber", "Data": "2024-03-12", "Categoria": "transporte", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 15},
        {"Nome da despesa": "Roupas", "Data": "2024-08-10", "Categoria": "vestuário", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 550},
        {"Nome da despesa": "Sapatos", "Data": "2024-08-28", "Categoria": "vestuário", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 300},
        {"Nome da despesa": "Mercado", "Data": "2024-09-10", "Categoria": "supermercado", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 450},
        {"Nome da despesa": "Curso Online", "Data": "2024-10-12", "Categoria": "educação", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 180},
        {"Nome da despesa": "Conserto carro", "Data": "2024-11-05", "Categoria": "transporte", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 550},
        {"Nome da despesa": "Seguro carro", "Data": "2024-11-22", "Categoria": "transporte", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 850},
        {"Nome da despesa": "Jantar especial", "Data": "2024-12-15", "Categoria": "lazer", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 170},
    ]
)
df["Data"] = pd.to_datetime(df["Data"])

# Paleta de cores personalizada para cada categoria
color_map = {
    "beleza": "#FF6699",
    "saúde": "#66FF66",
    "comida": "#FFCC00",
    "transporte": "#6699FF",
    "vestuário": "#FF9966",
    "supermercado": "#66FFFF",
    "educação": "#9966FF",
    "lazer": "#FF6666"
}

# Adicionar coluna de cores ao DataFrame com base na categoria
df["Cor"] = df["Categoria"].map(color_map)

# Título e entrada para orçamento
st.markdown("<h1 style='text-align: center;'>Orçamento do mês:</h1>", unsafe_allow_html=True)
orcamento = st.number_input("Insira o orçamento do mês:", min_value=0.0, format="%.2f")
st.markdown("<h2 style='text-align: center;'>Opções</h2>", unsafe_allow_html=True)

# Dividir layout em duas colunas de tamanhos iguais
col1, col2 = st.columns(2)

# Exibir gráfico de rosca à esquerda
with col1:
    fig_pie = px.pie(
        df,
        names="Categoria",
        values="Valor",
        title="Distribuição de Gastos por Categoria",
        hole=0.4,
        color="Categoria",
        color_discrete_map=color_map
    )
    fig_pie.update_layout(margin=dict(t=30, l=0, r=0, b=0))
    st.plotly_chart(fig_pie, use_container_width=True)

# Exibir DataFrame colorido à direita
with col2:
    # Aplicar as cores de acordo com a categoria ao DataFrame exibido
    st.dataframe(df.style.apply(lambda x: [f"background-color: {color_map[x['Categoria']]}" if x['Categoria'] in color_map else "" for _ in x], axis=1))
