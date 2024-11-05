import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Configurar página para layout expandido
st.set_page_config(layout="wide")

# Adicionar CSS para expandir área de exibição
def apply_custom_css():
    st.markdown("""
        <style>
        .main .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
            max-width: 100%;
        }
        .wishlist-widget {
            width: 100%;
            height: 150px;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            border-radius: 10px;
            cursor: pointer;
            overflow: hidden;
            position: relative;
            font-size: 1.2em;
            color: #fff;
            font-weight: bold;
            text-align: left;
        }
        .wishlist-text {
            padding-left: 20px;
            background: rgba(0, 0, 0, 0.5);
            height: 100%;
            display: flex;
            align-items: center;
            flex: 1;
        }
        .wishlist-color {
            width: 50px;
            height: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

# Função para carregar dados de despesas
def load_data():
    data = [
        {"Nome da despesa": "Sephora", "Data": "2024-01-15", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 750.99},
        {"Nome da despesa": "Farmácia", "Data": "2024-01-28", "Categoria": "saúde", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 125.50},
        # Continue com os demais dados...
    ]
    df = pd.DataFrame(data)
    df['Data'] = pd.to_datetime(df['Data'])
    return df

# Função para calcular e exibir o orçamento e totais
def display_budget_section(df):
    total_gastos = df[df['Tipo'] == 'gasto']['Valor'].sum()
    total_ganhos = df[df['Tipo'] == 'ganho']['Valor'].sum()
    saldo = total_ganhos - total_gastos

    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("Orçamento do Mês:")
        orçamento = st.number_input("Insira seu orçamento mensal:", min_value=0, value=0, step=100)
        st.write(f"O orçamento mensal é: R$ {orçamento:.2f}")
        st.write(f"Total de Gastos: R$ {total_gastos:.2f}")
        st.write(f"Total de Ganhos: R$ {total_ganhos:.2f}")
        st.write(f"Saldo: R$ {saldo:.2f}")

        display_expense_chart(df)
        display_line_chart(df)  # Adicionar o gráfico de linhas logo abaixo do gráfico de pizza

    with col2:
        st.write("")  # Espaço vazio para alinhamento
        display_expense_view_options(df)

# Função para exibir gráfico de despesas por categoria
def display_expense_chart(df):
    despesas_por_categoria = (
        df[df['Tipo'] == 'gasto']
        .groupby('Categoria')['Valor']
        .sum()
        .reset_index()
        .assign(Categoria=lambda x: x['Categoria'].where(x['Valor'] >= 50, 'Outros'))
        .groupby('Categoria')
        .sum()
        .reset_index()
    )
    
    fig = px.pie(despesas_por_categoria, values='Valor', names='Categoria', title='Distribuição das Despesas por Categoria')
    fig.update_layout(width=800, height=600)
    st.plotly_chart(fig)

# Função para exibir gráfico de linhas "Dinheiro ao longo do tempo"
def display_line_chart(df):
    st.subheader("Dinheiro ao longo do tempo")
    gasto_color = st.color_picker("Escolha a cor para a linha de Gastos", "#FF6347")
    ganho_color = st.color_picker("Escolha a cor para a linha de Ganhos", "#4682B4")

    df = df.sort_values('Data')  # Ordenar por data
    df_gastos = df[df['Tipo'] == 'gasto'].groupby('Data')['Valor'].sum().cumsum().reset_index()
    df_ganhos = df[df['Tipo'] == 'ganho'].groupby('Data')['Valor'].sum().cumsum().reset_index()

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_gastos['Data'], y=df_gastos['Valor'], mode='lines', name='Gastos', line=dict(color=gasto_color)))
    fig.add_trace(go.Scatter(x=df_ganhos['Data'], y=df_ganhos['Valor'], mode='lines', name='Ganhos', line=dict(color=ganho_color)))

    fig.update_layout(title="Evolução dos Gastos e Ganhos ao longo do tempo", xaxis_title="Data", yaxis_title="Valor Acumulado")
    st.plotly_chart(fig)

# Função para exibir opções de visualização de despesas
def display_expense_view_options(df):
    st.subheader("Despesas")
    option = st.selectbox("Selecione uma visualização:", ["Todas as Despesas", "Por mês", "Por categoria", "Adicionar despesa"])
    
    if option == "Todas as Despesas":
        st.dataframe(df)
    elif option == "Por mês":
        mes_selecionado = st.selectbox(
            "Selecione o mês:",
            sorted(df['Data'].dt.month.unique()),
            format_func=lambda x: pd.to_datetime(f"2024-{x}-01").strftime("%B")
        )
        despesas_mes = df[df['Data'].dt.month == mes_selecionado]
        st.dataframe(despesas_mes)
    elif option == "Por categoria":
        categoria_selecionada = st.selectbox("Selecione a categoria:", df['Categoria'].unique())
        despesas_categoria = df[df['Categoria'] == categoria_selecionada]
        st.dataframe(despesas_categoria)
    elif option == "Adicionar despesa":
        add_expense(df)

# Função para adicionar uma nova despesa ao DataFrame
def add_expense(df):
    st.subheader("Adicionar nova despesa")
    nome_despesa = st.text_input("Nome da despesa")
    data_despesa = st.date_input("Data da despesa")
    categoria_despesa = st.selectbox("Categoria", ["beleza", "saúde", "comida", "transporte", "vestuário", "supermercado", "educação", "lazer", "investimentos", "Salário"])
    forma_pagamento = st.selectbox("Forma de pagamento", ["débito", "crédito", "pix"])
    tipo_despesa = st.selectbox("Tipo", ["gasto", "ganho"])
    valor_despesa = st.number_input("Valor", min_value=0.0, step=0.01)

    if st.button("Adicionar"):
        nova_despesa = {
            "Nome da despesa": nome_despesa,
            "Data": pd.to_datetime(data_despesa),
            "Categoria": categoria_despesa,
            "Forma de pagamento": forma_pagamento,
            "Tipo": tipo_despesa,
            "Valor": valor_despesa
        }
        df = df.append(nova_despesa, ignore_index=True)
        st.success("Despesa adicionada com sucesso!")
        st.dataframe(df)  # Atualizar a exibição do DataFrame com a nova despesa

# Página principal
def main_page():
    st.header("Página Principal")
    df = load_data()
    display_budget_section(df)
    
    # Seletor de cor e widget Wishlist
    color = st.color_picker("Escolha uma cor para sua capa da Wishlist", "#3498db")
    st.markdown(
        f"""
        <div class="wishlist-widget" style="background-color: {color};" onclick="window.location.href = '?page=wishlist'">
            <div class="wishlist-color" style="background-color: {color};"></div>
            <div class="wishlist-text">Wishlist</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Página Wishlist
def wishlist_page():
    st.header("Wishlist")
    st.write("Esta é a página da Wishlist. Adicione seu conteúdo aqui.")

# Controle de navegação entre páginas
def main():
    apply_custom_css()
    
    # Definir a página ativa com base na URL
    page = st.experimental_get_query_params().get("page", ["main"])[0]
    
    if page == "main":
        main_page()
    elif page == "wishlist":
        wishlist_page()

# Adicionar JavaScript para redirecionar ao clicar no widget Wishlist
st.write(
    """
    <script>
    const wishlist = document.querySelector('.wishlist-widget');
    if (wishlist) {
        wishlist.addEventListener('click', function() {
            window.location.href = '?page=wishlist';
        });
    }
    </script>
    """,
    unsafe_allow_html=True
)

if __name__ == "__main__":
    main()
