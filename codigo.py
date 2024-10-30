import streamlit as st
import pandas as pd
import plotly.express as px

# Aplicar estilo CSS para usar tela cheia
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
        {"Nome da despesa": "Maquiagem", "Data": "2024-01-20", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 200},
        {"Nome da despesa": "Consulta médica", "Data": "2024-02-25", "Categoria": "saúde", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 300},
        {"Nome da despesa": "Lanche no trabalho", "Data": "2024-03-15", "Categoria": "comida", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 50},
        {"Nome da despesa": "Uber Eats", "Data": "2024-03-25", "Categoria": "comida", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 120},
        {"Nome da despesa": "Combustível", "Data": "2024-04-15", "Categoria": "transporte", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 100},
        {"Nome da despesa": "Limpeza do carro", "Data": "2024-04-20", "Categoria": "transporte", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 70},
        {"Nome da despesa": "Vestido", "Data": "2024-05-15", "Categoria": "vestuário", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 200},
        {"Nome da despesa": "Acessórios", "Data": "2024-05-20", "Categoria": "vestuário", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 150},
        {"Nome da despesa": "Supermercado", "Data": "2024-06-15", "Categoria": "supermercado", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 500},
        {"Nome da despesa": "Material escolar", "Data": "2024-07-15", "Categoria": "educação", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 150}, 
        {"Nome da despesa": "Show", "Data": "2024-07-20", "Categoria": "lazer", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 300},
        {"Nome da despesa": "Férias", "Data": "2024-08-01", "Categoria": "lazer", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 2000},
        {"Nome da despesa": "Curso", "Data": "2024-08-25", "Categoria": "educação", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 600}
    ]
)

# Converter a coluna 'Data' para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Calcular o total de gastos e ganhos
total_gastos = df[df['Tipo'] == 'gasto']['Valor'].sum()
total_ganhos = df[df['Tipo'] == 'ganho']['Valor'].sum()
total_mensal = total_ganhos - total_gastos

# Exibir o orçamento do mês
st.header("Orçamento do mês:")
st.write(f"Total de Gastos: R$ {total_gastos:.2f}")
st.write(f"Total de Ganhos: R$ {total_ganhos:.2f}")
st.write(f"Saldo: R$ {total_mensal:.2f}")

# Seção de visualização de despesas
st.subheader("Despesas")

# Opções para visualizar as despesas
visualizacao = st.selectbox("Escolha uma opção:", ["Todas as Despesas", "Por Mês", "Por Categoria"])

if visualizacao == "Todas as Despesas":
    st.write(df)
    
elif visualizacao == "Por Mês":
    mes_selecionado = st.selectbox("Escolha o mês:", pd.date_range(start=df['Data'].min(), end=df['Data'].max(), freq='M').strftime('%Y-%m').tolist())
    df_mensal = df[df['Data'].dt.strftime('%Y-%m') == mes_selecionado]
    st.write(df_mensal)
    
    # Gráfico de gastos mensais
    gastos_mensais = df_mensal.groupby(pd.Grouper(key='Data', freq='M'))['Valor'].sum().reset_index()
    fig = px.line(gastos_mensais, x='Data', y='Valor', title='Gastos Mensais', labels={'Valor': 'Total de Gastos', 'Data': 'Mês'})
    st.plotly_chart(fig)

elif visualizacao == "Por Categoria":
    categoria_selecionada = st.selectbox("Escolha a categoria:", df['Categoria'].unique())
    df_categoria = df[df['Categoria'] == categoria_selecionada]
    st.write(df_categoria)

    # Gráfico de gastos por categoria
    gastos_categoria = df_categoria.groupby(pd.Grouper(key='Data', freq='M'))['Valor'].sum().reset_index()
    fig = px.bar(gastos_categoria, x='Data', y='Valor', title='Gastos por Categoria', labels={'Valor': 'Total de Gastos', 'Data': 'Mês'})
    st.plotly_chart(fig)

# Seção de gráficos de gastos totais
st.subheader("Gráficos de Gastos Totais")
gastos_totais = df.groupby(pd.Grouper(key='Data', freq='M'))['Valor'].sum().reset_index()
fig_total = px.line(gastos_totais, x='Data', y='Valor', title='Total de Gastos ao Longo do Tempo', labels={'Valor': 'Total de Gastos', 'Data': 'Mês'})
st.plotly_chart(fig_total)

