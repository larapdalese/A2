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

import streamlit as st
import pandas as pd

def intro():
    st.write("# Bem-vindo ao meu aplicativo Streamlit! 👋")

def wishlist_page():
    st.write("# Wishlist")
    st.write("Esta é a página da Wishlist onde você pode adicionar itens que deseja!")

    # Dados da Wishlist
    data = [
        {"Nome do item": "Fenty Beauty Lipgloss", "Valor": 750.99},
        {"Nome do item": "Clinique Almost Lipstick", "Valor": 125.50},
        {"Nome do item": "Monotheme Vanilla Blossom", "Valor": 36.00},
    ]

    # Criar DataFrame
    wishlist_df = pd.DataFrame(data)

    # Exibir DataFrame na página
    st.write("### Itens na Wishlist")
    st.dataframe(wishlist_df)

# Função para criar um botão estilizado
def create_wishlist_button():
    st.markdown(
        """
        <style>
        .wishlist-button {
            display: inline-block;
            padding: 20px;
            background-color: #4CAF50; /* Cor da capa */
            color: white;
            border-radius: 10px;
            text-align: center;
            text-decoration: none;
            font-size: 24px;
            margin: 10px;
        }
        </style>
        <a class="wishlist-button" href="#wishlist">Wishlist</a>
        """,
        unsafe_allow_html=True,
    )

# Mapeando as funções para as páginas
page_names_to_funcs = {
    "Introdução": intro,
    "Wishlist": wishlist_page
}

# Sidebar para selecionar a página
demo_name = st.sidebar.selectbox("Escolha uma página", page_names_to_funcs.keys())

# Chama a função correspondente à página selecionada
if demo_name == "Wishlist":
    wishlist_page()
else:
    intro()

# Cria o botão "Wishlist" que leva à nova página
create_wishlist_button()


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
        {"Nome da despesa": "Show", "Data": "2024-07-20", "Categoria": "lazer", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 250},
        {"Nome da despesa": "Cinema", "Data": "2024-08-05", "Categoria": "lazer", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 50},
        {"Nome da despesa": "Férias", "Data": "2024-08-20", "Categoria": "lazer", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 3000},
        {"Nome da despesa": "Corte de cabelo", "Data": "2024-02-20", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 100},
        {"Nome da despesa": "Consulta médica", "Data": "2024-03-15", "Categoria": "saúde", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 250},
        {"Nome da despesa": "Lanchonete", "Data": "2024-04-05", "Categoria": "comida", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 45},
        {"Nome da despesa": "Supermercado", "Data": "2024-04-20", "Categoria": "supermercado", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 320},
        {"Nome da despesa": "Curso de idiomas", "Data": "2024-05-10", "Categoria": "educação", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 300},
        {"Nome da despesa": "Creme para pele", "Data": "2024-06-12", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 200},
        {"Nome da despesa": "Vacina", "Data": "2024-07-20", "Categoria": "saúde", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 150},
        {"Nome da despesa": "Almoço de negócios", "Data": "2024-08-22", "Categoria": "comida", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 95},
        {"Nome da despesa": "Aula de yoga", "Data": "2024-09-05", "Categoria": "educação", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 120},
        {"Nome da despesa": "Medicamentos", "Data": "2024-10-30", "Categoria": "saúde", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 200},
        {"Nome da despesa": "Despesas com animais de estimação", "Data": "2024-11-18", "Categoria": "saúde", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 85},
        {"Nome da despesa": "Investimentos", "Data": "2024-01-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-02-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-03-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-04-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-05-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-06-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-07-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-08-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-09-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-10-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-11-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
        {"Nome da despesa": "Investimentos", "Data": "2024-12-01", "Categoria": "investimentos", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 700},
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
    st.header("Orçamento do Mês:")
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
    st.write("")

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
