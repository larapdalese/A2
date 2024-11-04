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

# Exemplo de DataFrame
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
        # (adicionar mais dados conforme necessário)
    ]
)

# Criar uma coluna de data do tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Calcular totais
total_gastos = df[df['Tipo'] == 'gasto']['Valor'].sum()
total_ganhos = df[df['Tipo'] == 'ganho']['Valor'].sum()
saldo = total_ganhos - total_gastos

# Colunas para a seção do orçamento
col1, col2 = st.columns([2, 1])  # Mais espaço para a coluna do orçamento

with col1:
    st.header("Dados financeiros:")
    # Campo para inserir o orçamento do mês
    orçamento = st.number_input("Insira seu orçamento mensal:", min_value=0, value=0, step=100)
    st.write(f"O orçamento mensal é: R$ {orçamento}")

    # Exibir totais
    st.write(f"Total de Gastos: R$ {total_gastos:.2f}")
    st.write(f"Total de Ganhos: R$ {total_ganhos:.2f}")
    st.write(f"Saldo: R$ {saldo:.2f}")

    # Agrupar despesas por categoria
    despesas_por_categoria = df[df['Tipo'] == 'gasto'].groupby('Categoria')['Valor'].sum().reset_index()

    # Definir um limite para considerar as menores categorias como "Outros"
    threshold = 50  # Exemplo: categorias com valor total menor que 50 serão agrupadas

    # Criar nova categoria "Outros" para categorias menores que o limite
    despesas_por_categoria['Categoria'] = despesas_por_categoria.apply(
        lambda x: x['Categoria'] if x['Valor'] >= threshold else 'Outros',
        axis=1
    )

    # Agrupar novamente após a modificação
    despesas_por_categoria = despesas_por_categoria.groupby('Categoria')['Valor'].sum().reset_index()

    # Gráfico de pizza para despesas
    fig = px.pie(despesas_por_categoria, values='Valor', names='Categoria', title='Distribuição das Despesas por Categoria')
    
    # Atualizar layout para aumentar o tamanho do gráfico
    fig.update_layout(width=800, height=600)  # Ajuste os valores conforme necessário
    st.plotly_chart(fig)

with col2:
    st.empty() 

with col2:
    st.subheader("Despesas")
    option = st.selectbox("Selecione uma visualização:", ["Todas as Despesas", "Por mês", "Por categoria"])
    
    if option == "Todas as Despesas":
        st.dataframe(df)
    elif option == "Por mês":
        mes_selecionado = st.selectbox("Selecione o mês:", df['Data'].dt.month.unique(), format_func=lambda x: pd.to_datetime(f"2024-{x}-01").strftime("%B"))
        despesas_mes = df[df['Data'].dt.month == mes_selecionado]
        st.dataframe(despesas_mes)
    elif option == "Por categoria":
        categoria_selecionada = st.selectbox("Selecione a categoria:", df['Categoria'].unique())
        despesas_categoria = df[df['Categoria'] == categoria_selecionada]
        st.dataframe(despesas_categoria)
