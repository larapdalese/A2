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

# Criar DataFrame de despesas e ganhos
df = pd.DataFrame([
    {"Nome da despesa": "Sephora", "Data": "2024-01-15", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 750.99},
    {"Nome da despesa": "Farmácia", "Data": "2024-01-28", "Categoria": "saúde", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 125.50},
    # ... (adicione o restante dos dados aqui)
    {"Nome da despesa": "Férias", "Data": "2024-08-20", "Categoria": "lazer", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 3000}
])
df["Data"] = pd.to_datetime(df["Data"])

# Título e entrada para orçamento
st.markdown("<h1 style='text-align: center;'>Orçamento do mês:</h1>", unsafe_allow_html=True)
orcamento = st.number_input("Insira o orçamento do mês:", min_value=0.0, format="%.2f")
st.markdown("<h2 style='text-align: center;'>Opções</h2>", unsafe_allow_html=True)

# Dividir layout em duas colunas de tamanhos iguais
col1, col2 = st.columns(2)

# Exibir gráfico de rosca à esquerda
with col1:
    fig_pie = px.pie(df, names="Categoria", values="Valor", title="Distribuição de Gastos por Categoria", hole=0.4)
    fig_pie.update_layout(margin=dict(t=30, l=0, r=0, b=0))
    st.plotly_chart(fig_pie, use_container_width=True)

# Exibir menu de opções à direita
with col2:
    escolha = st.radio("Opções", ["Todas as Despesas", "Por Categoria", "Mais 3"])

    # Exibir DataFrames de acordo com a opção escolhida
    if escolha == "Todas as Despesas":
        st.write(df)
    elif escolha == "Por Categoria":
        categoria_selecionada = st.selectbox("Escolha uma categoria:", df["Categoria"].unique())
        despesas_categoria = df[df["Categoria"] == categoria_selecionada]
        st.write(despesas_categoria)
    elif escolha == "Mais 3":
        escolha_mais_3 = st.radio("Opções adicionais", ["Por mês", "Gastos totais ao longo do tempo", "Gastos ao longo dos meses"])
        
        if escolha_mais_3 == "Por mês":
            mes_selecionado = st.selectbox("Selecione o mês:", ["Tudo"] + list(df["Data"].dt.to_period("M").astype(str).unique()))
            if mes_selecionado == "Tudo":
                st.write(df)
            else:
                despesas_mes = df[df["Data"].dt.to_period("M").astype(str) == mes_selecionado]
                st.write(despesas_mes)
        
        elif escolha_mais_3 == "Gastos totais ao longo do tempo":
            fig_line = px.line(df, x="Data", y="Valor", color="Categoria", title="Gastos Totais ao Longo do Tempo")
            fig_line.update_layout(margin=dict(t=30, l=0, r=0, b=0))
            st.plotly_chart(fig_line, use_container_width=True)
        
        elif escolha_mais_3 == "Gastos ao longo dos meses":
            df["Mês"] = df["Data"].dt.to_period("M")
            despesas_mes = df.groupby("Mês")["Valor"].sum().reset_index()
            fig_bar = px.bar(despesas_mes, x="Mês", y="Valor", title="Gastos ao Longo dos Meses")
            fig_bar.update_layout(margin=dict(t=30, l=0, r=0, b=0))
            st.plotly_chart(fig_bar, use_container_width=True)
