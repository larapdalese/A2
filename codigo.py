import streamlit as st
import pandas as pd
import plotly.express as px

# Aplicar estilo CSS para usar tela cheia
st.set_page_config(layout="wide")  # Configurar a página para o layout expandido

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
        {"Nome da despesa": "Táxi", "Data": "2024-03-30", "Categoria": "transporte", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 25},
        {"Nome da despesa": "Saraiva", "Data": "2024-04-10", "Categoria": "livros", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 45.50},
        {"Nome da despesa": "Livraria Cultura", "Data": "2024-04-25", "Categoria": "livros", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 60},
        {"Nome da despesa": "Cinema", "Data": "2024-05-15", "Categoria": "lazer", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 50},
        {"Nome da despesa": "Teatro", "Data": "2024-05-20", "Categoria": "lazer", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 120},
        {"Nome da despesa": "Academia", "Data": "2024-06-05", "Categoria": "fitness", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 200},
        {"Nome da despesa": "Yoga", "Data": "2024-06-22", "Categoria": "fitness", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 150},
        {"Nome da despesa": "Pet Shop", "Data": "2024-07-11", "Categoria": "pets", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 80},
        {"Nome da despesa": "Veterinário", "Data": "2024-07-25", "Categoria": "pets", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 300},
        {"Nome da despesa": "Roupas", "Data": "2024-08-10", "Categoria": "vestuário", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 500},
        {"Nome da despesa": "Sapatos", "Data": "2024-08-28", "Categoria": "vestuário", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 250},
        {"Nome da despesa": "Mercado", "Data": "2024-09-10", "Categoria": "supermercado", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 400},
        {"Nome da despesa": "Hortifruti", "Data": "2024-09-20", "Categoria": "supermercado", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 60},
        {"Nome da despesa": "Curso Online", "Data": "2024-10-12", "Categoria": "educação", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 150},
        {"Nome da despesa": "Workshop", "Data": "2024-10-26", "Categoria": "educação", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 200},
        {"Nome da despesa": "Conserto carro", "Data": "2024-11-05", "Categoria": "transporte", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 500},
        {"Nome da despesa": "Seguro carro", "Data": "2024-11-22", "Categoria": "transporte", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 800},
        {"Nome da despesa": "Jantar especial", "Data": "2024-12-15", "Categoria": "lazer", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 150},
        {"Nome da despesa": "Presente", "Data": "2024-12-25", "Categoria": "outros", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 100},
        {"Nome da despesa": "Mesada", "Data": "2024-01-05", "Categoria": "Salário", "Forma de pagamento": "crédito", "Tipo": "ganho", "Valor": 500},
        {"Nome da despesa": "Trabalho", "Data": "2024-01-10", "Categoria": "Salário", "Forma de pagamento": "débito", "Tipo": "ganho", "Valor": 3000},
        {"Nome da despesa": "Mesada", "Data": "2024-02-05", "Categoria": "Salário", "Forma de pagamento": "pix", "Tipo": "ganho", "Valor": 500},
        {"Nome da despesa": "Trabalho", "Data": "2024-02-10", "Categoria": "Salário", "Forma de pagamento": "crédito", "Tipo": "ganho", "Valor": 3000},
        {"Nome da despesa": "Mesada", "Data": "2024-03-05", "Categoria": "Salário", "Forma de pagamento": "débito", "Tipo": "ganho", "Valor": 500},
        {"Nome da despesa": "Trabalho", "Data": "2024-03-10", "Categoria": "Salário", "Forma de pagamento": "pix", "Tipo": "ganho", "Valor": 3000},
        {"Nome da despesa": "Mesada", "Data": "2024-04-05", "Categoria": "Salário", "Forma de pagamento": "crédito", "Tipo": "ganho", "Valor": 500},
        {"Nome da despesa": "Trabalho", "Data": "2024-04-10", "Categoria": "Salário", "Forma de pagamento": "débito", "Tipo": "ganho", "Valor": 3000},
        {"Nome da despesa": "Mesada", "Data": "2024-05-05", "Categoria": "Salário", "Forma de pagamento": "pix", "Tipo": "ganho", "Valor": 500},
        {"Nome da despesa": "Trabalho", "Data": "2024-05-10", "Categoria": "Salário", "Forma de pagamento": "crédito", "Tipo": "ganho", "Valor": 3000},
        {"Nome da despesa": "Mesada", "Data": "2024-06-05", "Categoria": "Salário", "Forma de pagamento": "débito", "Tipo": "ganho", "Valor": 500},
        {"Nome da despesa": "Trabalho", "Data": "2024-06-10", "Categoria": "Salário", "Forma de pagamento": "pix", "Tipo": "ganho", "Valor": 3000},
        {"Nome da despesa": "Mesada", "Data": "2024-07-05", "Categoria": "Salário", "Forma de pagamento": "crédito", "Tipo": "ganho", "Valor": 500},
        {"Nome da despesa": "Trabalho", "Data": "2024-07-10", "Categoria": "Salário", "Forma de pagamento": "débito", "Tipo": "ganho", "Valor": 3000},
        {"Nome da despesa": "Mesada", "Data": "2024-08-05", "Categoria": "Salário", "Forma de pagamento": "pix", "Tipo": "ganho", "Valor": 500},
        {"Nome da despesa": "Trabalho", "Data": "2024-08-10", "Categoria": "Salário", "Forma de pagamento": "crédito", "Tipo": "ganho", "Valor": 3000},
        {"Nome da despesa": "Mesada", "Data": "2024-09-05", "Categoria": "Salário", "Forma de pagamento": "débito", "Tipo": "ganho", "Valor": 500},
        {"Nome da despesa": "Trabalho", "Data": "2024-09-10", "Categoria": "Salário", "Forma de pagamento": "pix", "Tipo": "ganho", "Valor": 3000},
        {"Nome da despesa": "Mesada", "Data": "2024-10-05", "Categoria": "Salário", "Forma de pagamento": "crédito", "Tipo": "ganho", "Valor": 500},
        {"Nome da despesa": "Trabalho", "Data": "2024-10-10", "Categoria": "Salário", "Forma de pagamento": "débito", "Tipo": "ganho", "Valor": 3000},
    ]
)

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
            df["AnoMes"] = df["Data"].dt.to_period("M").astype(str)
            despesas_por_mes = df.groupby("AnoMes")["Valor"].sum().reset_index()
            fig_gastos_totais = px.line(despesas_por_mes, x="AnoMes", y="Valor", title="Gastos Totais ao Longo do Tempo")
            st.plotly_chart(fig_gastos_totais, use_container_width=True)
        
        elif escolha_mais_3 == "Gastos ao longo dos meses":
            df["Mes"] = df["Data"].dt.month
            despesas_por_mes = df.groupby("Mes")["Valor"].sum().reset_index()
            fig_gastos_mensais = px.line(despesas_por_mes, x="Mes", y="Valor", title="Gastos ao Longo dos Meses")
            st.plotly_chart(fig_gastos_mensais, use_container_width=True)
