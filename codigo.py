import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(layout="wide")

# CSS para aumentar o espaço de exibição e reduzir margens
st.markdown("""
    <style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
        max-width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# Dados de exemplo para o DataFrame
df = pd.DataFrame(
    [
        {"Nome da despesa": "Sephora", "Valor": 750.99, "Categoria": "beleza", "Data": "2024-01-15"},
        {"Nome da despesa": "Farmácia", "Valor": 125.50, "Categoria": "saúde", "Data": "2024-01-28"},
        {"Nome da despesa": "Starbucks", "Valor": 36, "Categoria": "comida", "Data": "2024-02-05"},
        {"Nome da despesa": "Restaurante", "Valor": 80, "Categoria": "comida", "Data": "2024-02-18"},
        # ... (outros dados)
    ]
)
df["Data"] = pd.to_datetime(df["Data"])

# Padronizar valores na coluna "Categoria" para minúsculas e sem espaços extras
df["Categoria"] = df["Categoria"].str.strip().str.lower()

# Título e orçamento
st.markdown("<h1 style='text-align: center;'>Orçamento do mês:</h1>", unsafe_allow_html=True)
orcamento = st.number_input("Insira o orçamento do mês:", min_value=0.0, format="%.2f")
st.markdown("<h2 style='text-align: center;'>Opções</h2>", unsafe_allow_html=True)

# Dividir layout em duas colunas
col1, col2 = st.columns(2)

# Gráfico de rosca na coluna da esquerda
with col1:
    fig_pie = px.pie(df, names="Categoria", values="Valor", title="Distribuição de Gastos por Categoria", hole=0.4)
    fig_pie.update_layout(margin=dict(t=30, l=0, r=0, b=0))
    st.plotly_chart(fig_pie, use_container_width=True)

# Menu de opções na coluna da direita
with col2:
    st.write("**Opções**")
    col_a, col_b, col_c = st.columns(3)

    escolha = None  # Variável para armazenar a escolha
    with col_a:
        if st.button("Todas as Despesas"):
            escolha = "Todas as Despesas"
    with col_b:
        if st.button("Por Categoria"):
            escolha = "Por Categoria"
    with col_c:
        if st.button("Mais 3"):
            escolha = "Mais 3"

    # Exibir DataFrame ou gráfico de acordo com a escolha
    if escolha == "Todas as Despesas":
        st.write(df)
    elif escolha == "Por Categoria":
        categoria_selecionada = st.selectbox("Escolha uma categoria:", df["Categoria"].unique())
        despesas_categoria = df[df["Categoria"] == categoria_selecionada]
        st.write(despesas_categoria)
    elif escolha == "Mais 3":
        with st.expander("Mais opções"):
            escolha_mais_3 = st.radio("Selecione uma das opções adicionais:", ["Por mês", "Gastos totais ao longo do tempo", "Gastos ao longo dos meses"])

            if escolha_mais_3 == "Por mês":
                mes_selecionado = st.selectbox("Selecione o mês:", ["Tudo"] + list(df["Data"].dt.to_period("M").astype(str).unique()))
                if mes_selecionado == "Tudo":
                    st.write(df)
                else:
                    despesas_mes = df[df["Data"].dt.to_period("M").astype(str) == mes_selecionado]
                    st.write(despesas_mes)

            elif escolha_mais_3 == "Gastos totais ao longo do tempo":
                df["AnoMes"] = df["Data"].dt.to_period("M").astype(str)
                despesas_por_mes = df.groupby("AnoMes")["Valor"].sum().reset_index()
                fig_gastos_totais = px.line(despesas_por_mes, x="AnoMes", y="Valor", title="Gastos Totais ao Longo do Tempo")
                st.plotly_chart(fig_gastos_totais, use_container_width=True)

            elif escolha_mais_3 == "Gastos ao longo dos meses":
                df["Mes"] = df["Data"].dt.month
                despesas_por_mes = df.groupby("Mes")["Valor"].sum().reset_index()
                fig_gastos_mensais = px.line(despesas_por_mes, x="Mes", y="Valor", title="Gastos ao Longo dos Meses")
                st.plotly_chart(fig_gastos_mensais, use_container_width=True)
