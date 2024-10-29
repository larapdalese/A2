import streamlit as st
import pandas as pd
import plotly.express as px

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
        {"Nome da despesa": "Roupas", "Valor": 500, "Categoria": "vestuário", "Data": "2024-08-10"},
        {"Nome da despesa": "Sapatos", "Valor": 250, "Categoria": "vestuário", "Data": "2024-08-28"},
        {"Nome da despesa": "Mercado", "Valor": 400, "Categoria": "supermercado", "Data": "2024-09-10"},
        {"Nome da despesa": "Hortifruti", "Valor": 60, "Categoria": "supermercado", "Data": "2024-09-20"},
        {"Nome da despesa": "Curso Online", "Valor": 150, "Categoria": "educação", "Data": "2024-10-12"},
        {"Nome da despesa": "Workshop", "Valor": 200, "Categoria": "educação", "Data": "2024-10-26"},
        {"Nome da despesa": "Conserto carro", "Valor": 500, "Categoria": "transporte", "Data": "2024-11-05"},
        {"Nome da despesa": "Seguro carro", "Valor": 800, "Categoria": "transporte", "Data": "2024-11-22"},
        {"Nome da despesa": "Jantar especial", "Valor": 150, "Categoria": "lazer", "Data": "2024-12-15"},
        {"Nome da despesa": "Presente", "Valor": 100, "Categoria": "outros", "Data": "2024-12-25"}
    ]
)
df["Data"] = pd.to_datetime(df["Data"])

# Título e entrada para orçamento
st.markdown("<h1 style='text-align: center;'>Orçamento do mês:</h1>", unsafe_allow_html=True)
orcamento = st.number_input("Insira o orçamento do mês:", min_value=0.0, format="%.2f")
st.markdown("<h2 style='text-align: center;'>Opções</h2>", unsafe_allow_html=True)

# Dividir layout em duas colunas iguais
col1, col2 = st.columns(2)

# Exibir gráfico de rosca à esquerda
with col1:
    fig_pie = px.pie(df, names="Categoria", values="Valor", title="Distribuição de Gastos por Categoria", hole=0.4)
    fig_pie.update_layout(margin=dict(t=30, l=0, r=0, b=0))  # Remove margens extras
    st.plotly_chart(fig_pie, use_container_width=True)  # Gráfico usa toda a largura da coluna

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
            df["AnoMes"] = df["Data"].dt.to_period("M").astype(str)
            despesas_por_mes = df.groupby("AnoMes")["Valor"].sum().reset_index()
            fig_gastos_totais = px.line(despesas_por_mes, x="AnoMes", y="Valor", title="Gastos Totais ao Longo do Tempo")
            st.plotly_chart(fig_gastos_totais, use_container_width=True)
        
        elif escolha_mais_3 == "Gastos ao longo dos meses":
            df["Mes"] = df["Data"].dt.month
            despesas_por_mes = df.groupby("Mes")["Valor"].sum().reset_index()
            fig_gastos_mensais = px.line(despesas_por_mes, x="Mes", y="Valor", title="Gastos ao Longo dos Meses")
            st.plotly_chart(fig_gastos_mensais, use_container_width=True)
