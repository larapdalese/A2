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
        {"Nome da despesa": "Corte de cabelo", "Data": "2024-01-25", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 150},
        {"Nome da despesa": "Visita ao dentista", "Data": "2024-01-30", "Categoria": "saúde", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 400},
        {"Nome da despesa": "Lanche na escola", "Data": "2024-02-10", "Categoria": "comida", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 25},
        {"Nome da despesa": "Pizza", "Data": "2024-02-22", "Categoria": "comida", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 60},
        {"Nome da despesa": "Passagem de ônibus", "Data": "2024-03-05", "Categoria": "transporte", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 10},
        {"Nome da despesa": "Pedágio", "Data": "2024-03-20", "Categoria": "transporte", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 5},
        {"Nome da despesa": "Maquiagem", "Data": "2024-04-10", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 200},
        {"Nome da despesa": "Remédios", "Data": "2024-04-25", "Categoria": "saúde", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 90},
        {"Nome da despesa": "Camiseta", "Data": "2024-05-15", "Categoria": "vestuário", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 100},
        {"Nome da despesa": "Calça", "Data": "2024-05-30", "Categoria": "vestuário", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 150},
        {"Nome da despesa": "Lanche na padaria", "Data": "2024-06-10", "Categoria": "comida", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 30},
        {"Nome da despesa": "Almoço com amigos", "Data": "2024-06-20", "Categoria": "comida", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 70},
        {"Nome da despesa": "Passeio", "Data": "2024-07-10", "Categoria": "lazer", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 120},
        {"Nome da despesa": "Jantar fora", "Data": "2024-07-25", "Categoria": "lazer", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 90},
        {"Nome da despesa": "Manicure", "Data": "2024-08-15", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 80},
        {"Nome da despesa": "Exame médico", "Data": "2024-08-30", "Categoria": "saúde", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 200},
        {"Nome da despesa": "Café", "Data": "2024-09-15", "Categoria": "comida", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 20},
        {"Nome da despesa": "Sorvete", "Data": "2024-09-25", "Categoria": "comida", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 15},
        {"Nome da despesa": "Passeio de bicicleta", "Data": "2024-10-20", "Categoria": "lazer", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 40},
        {"Nome da despesa": "Show de música", "Data": "2024-10-30", "Categoria": "lazer", "Forma de pagamento": "crédito", "Tipo": "gasto", "Valor": 100}
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
# Função para exibir gráfico de despesas por categoria com opção de edição de cores para cada categoria
def display_expense_chart(df):
    if 'editar_grafico_pizza' not in st.session_state:
        st.session_state['editar_grafico_pizza'] = False

    # Cores padrão para o gráfico de pizza
    if 'categoria_colors' not in st.session_state:
        categorias_unicas = df['Categoria'].unique()
        st.session_state['categoria_colors'] = {categoria: px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)] for i, categoria in enumerate(categorias_unicas)}

    # Criar gráfico de pizza
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
    fig.update_traces(marker=dict(colors=[st.session_state['categoria_colors'].get(cat, '#000000') for cat in despesas_por_categoria['Categoria']]))
    fig.update_layout(width=800, height=600)
    st.plotly_chart(fig)

    # Botão para mostrar opções de edição
    if st.button("Editar"):
        st.session_state['editar_grafico_pizza'] = not st.session_state['editar_grafico_pizza']

    # Exibir opções de edição de cores se 'Editar' foi clicado
    if st.session_state['editar_grafico_pizza']:
        st.write("**Escolha novas cores para cada categoria**")
        for categoria in despesas_por_categoria['Categoria']:
            nova_cor = st.color_picker(f"Cor para {categoria}", st.session_state['categoria_colors'][categoria])
            st.session_state['categoria_colors'][categoria] = nova_cor  # Atualiza a cor no estado da sessão

        # Botão de salvar para manter as alterações
        if st.button("Salvar"):
            st.success("Cores atualizadas com sucesso!")
            st.session_state['editar_grafico_pizza'] = False  # Esconde as opções de edição após salvar


# Função para exibir gráfico de linhas "Dinheiro ao longo do tempo"
# Função para exibir gráfico de linhas "Dinheiro ao longo do tempo" com opção de edição de cores
def display_line_chart(df):
    st.subheader("Dinheiro ao longo do tempo")
    if 'editar_grafico' not in st.session_state:
        st.session_state['editar_grafico'] = False

    # Gráfico inicial
    df = df.sort_values('Data')  # Ordenar por data
    df_gastos = df[df['Tipo'] == 'gasto'].groupby('Data')['Valor'].sum().cumsum().reset_index()
    df_ganhos = df[df['Tipo'] == 'ganho'].groupby('Data')['Valor'].sum().cumsum().reset_index()

    # Armazenar cores selecionadas no estado da sessão
    if 'gasto_color' not in st.session_state:
        st.session_state['gasto_color'] = "#FF6347"  # Cor padrão para gastos
    if 'ganho_color' not in st.session_state:
        st.session_state['ganho_color'] = "#4682B4"  # Cor padrão para ganhos

    # Mostrar gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_gastos['Data'], y=df_gastos['Valor'], mode='lines', name='Gastos',
        line=dict(color=st.session_state['gasto_color'])
    ))
    fig.add_trace(go.Scatter(
        x=df_ganhos['Data'], y=df_ganhos['Valor'], mode='lines', name='Ganhos',
        line=dict(color=st.session_state['ganho_color'])
    ))

    fig.update_layout(title="Evolução dos Gastos e Ganhos ao longo do tempo", xaxis_title="Data", yaxis_title="Valor Acumulado")
    st.plotly_chart(fig)

    # Botão para mostrar opções de edição
    if st.button("Editar"):
        st.session_state['editar_grafico'] = not st.session_state['editar_grafico']

    # Exibir opções de edição de cores se 'Editar' foi clicado
    if st.session_state['editar_grafico']:
        col1, col2 = st.columns(2)
        with col1:
            st.session_state['gasto_color'] = st.color_picker("Cor de Gastos", st.session_state['gasto_color'])
        with col2:
            st.session_state['ganho_color'] = st.color_picker("Cor de Ganhos", st.session_state['ganho_color'])

        # Botão de salvar para manter as alterações
        if st.button("Salvar"):
            st.success("Cores atualizadas com sucesso!")
            st.session_state['editar_grafico'] = False  # Esconde as opções de edição após salvar


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
apply_custom_css()

# Carregar os dados e exibir a seção principal da aplicação
df = load_data()
display_budget_section(df)
