import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(layout="wide")

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

apply_custom_css()

st.sidebar.title("Navegação")
st.sidebar.markdown("[Início 🏠](https://financedivas.streamlit.app)")
st.sidebar.markdown("[Gráficos 📊](https://graficosa2.streamlit.app/)")
st.sidebar.markdown("[Insights 💡](https://insightsa2.streamlit.app/)")
st.sidebar.markdown("[Notícias 🌎](https://newsa2.streamlit.app/)")


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
        display_line_chart(df)  
    with col2:
        st.write("")  
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
            if 'despesas_df' not in st.session_state:
                st.session_state['despesas_df'] = pd.DataFrame(columns=["Nome da despesa", "Data", "Categoria", "Forma de pagamento", "Tipo", "Valor"])
            st.session_state['despesas_df'] = pd.concat([st.session_state['despesas_df'], pd.DataFrame([nova_despesa])], ignore_index=True)
            st.success("Despesa adicionada com sucesso!")
            st.dataframe(st.session_state['despesas_df'])
def display_insights(df):
    st.subheader("Insights de Gastos")
    st.markdown("""
    - **Período de maior gasto do mês**:
    """)
    data_atual = pd.Timestamp.now().date()
    df_ultimos_30_dias = df[(df['Data'].dt.date >= (data_atual - pd.Timedelta(days=30))) & (df['Data'].dt.date <= data_atual)]
    df_gastos_diarios = df_ultimos_30_dias[df_ultimos_30_dias['Tipo'] == 'gasto'].groupby(df_ultimos_30_dias['Data'].dt.date)['Valor'].sum()
    dia_mais_gasto = df_gastos_diarios.idxmax() if not df_gastos_diarios.empty else "Sem dados"
    valor_dia_mais_gasto = df_gastos_diarios.max() if not df_gastos_diarios.empty else 0.0
    st.markdown(f"""
    O dia com maior gasto nos últimos 30 dias foi **{dia_mais_gasto}**, com um total de **R$ {valor_dia_mais_gasto:.2f}**.
    """)
    st.markdown("""
    - **Categoria com maior gasto acumulado**:
    """)
    categoria_mais_gastos = df[df['Tipo'] == 'gasto'].groupby('Categoria')['Valor'].sum().idxmax()
    valor_categoria_mais_gastos = df[df['Tipo'] == 'gasto'].groupby('Categoria')['Valor'].sum().max()
    st.markdown(f"""
    A categoria com mais despesas acumuladas é **{categoria_mais_gastos}**, com um total de **R$ {valor_categoria_mais_gastos:.2f}** em gastos.
    """)
    st.markdown("""
    - **Probabilidade de ultrapassar o orçamento**:
    """)
    total_gastos = df[df['Tipo'] == 'gasto']['Valor'].sum()
    df_categoria_prob = df[df['Tipo'] == 'gasto'].groupby('Categoria')['Valor'].sum() / total_gastos
    categoria_alto_risco = df_categoria_prob.idxmax()
    probabilidade_alto_risco = df_categoria_prob.max() * 100
    st.markdown(f"""
    A categoria com maior risco de ultrapassar o orçamento é **{categoria_alto_risco}**, com uma probabilidade de **{probabilidade_alto_risco:.2f}%**.
    """)
    if st.button("Fiquei curiosa, quero saber mais"):
        if dia_mais_gasto != "Sem dados":
            intervalo_inicio = dia_mais_gasto - pd.Timedelta(days=3)
            intervalo_fim = dia_mais_gasto + pd.Timedelta(days=3)
            df_detalhes = df[(df['Data'].dt.date >= intervalo_inicio) & (df['Data'].dt.date <= intervalo_fim)]
            st.write(f"Despesas entre **{intervalo_inicio}** e **{intervalo_fim}**:")
            st.dataframe(df_detalhes)
        else:
            st.write("Não há dados suficientes para exibir mais detalhes.")
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
    if 'editar_treemap' not in st.session_state:
        st.session_state['editar_treemap'] = False
    if 'categoria_colors' not in st.session_state:
        st.session_state['categoria_colors'] = {cat: px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)]
                                                for i, cat in enumerate(despesas_por_categoria['Categoria'])}
    fig = px.treemap(
        despesas_por_categoria,
        path=['Categoria'],
        values='Valor',
        title='Distribuição das Despesas por Categoria',
        color='Categoria',
        color_discrete_map=st.session_state['categoria_colors']
    )
    fig.update_layout(width=800, height=600)
    st.plotly_chart(fig)
    if st.button("Editar Cores do Gráfico de Treemap"):
        st.session_state['editar_treemap'] = not st.session_state['editar_treemap']
    if st.session_state['editar_treemap']:
        st.subheader("Editar Cores das Categorias")
        col1, col2 = st.columns(2)
        categorias = list(st.session_state['categoria_colors'].keys())
        for i in range(0, len(categorias), 2):
            with col1:
                if i < len(categorias):
                    st.session_state['categoria_colors'][categorias[i]] = st.color_picker(
                        f"Cor para {categorias[i]}", st.session_state['categoria_colors'][categorias[i]]
                    )
            with col2:
                if i + 1 < len(categorias):
                    st.session_state['categoria_colors'][categorias[i + 1]] = st.color_picker(
                        f"Cor para {categorias[i + 1]}", st.session_state['categoria_colors'][categorias[i + 1]]
                    )
        if st.button("Salvar Cores"):
            st.success("Cores do gráfico de treemap atualizadas com sucesso!")
            st.session_state['editar_treemap'] = False
def display_line_chart(df):
    if 'editar_grafico' not in st.session_state:
        st.session_state['editar_grafico'] = False
    df = df.sort_values('Data')  
    df_gastos = df[df['Tipo'] == 'gasto'].groupby('Data')['Valor'].sum().cumsum().reset_index()
    df_ganhos = df[df['Tipo'] == 'ganho'].groupby('Data')['Valor'].sum().cumsum().reset_index()
    if 'gasto_color' not in st.session_state:
        st.session_state['gasto_color'] = "#FF6347"  
    if 'ganho_color' not in st.session_state:
        st.session_state['ganho_color'] = "#4682B4" 
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
    if st.button("Editar"):
        st.session_state['editar_grafico'] = not st.session_state['editar_grafico']
    if st.session_state['editar_grafico']:
        col1, col2 = st.columns(2)
        with col1:
            st.session_state['gasto_color'] = st.color_picker("Cor de Gastos", st.session_state['gasto_color'])
        with col2:
            st.session_state['ganho_color'] = st.color_picker("Cor de Ganhos", st.session_state['ganho_color'])
        if st.button("Salvar"):
            st.success("Cores atualizadas com sucesso!")
            st.session_state['editar_grafico'] = False  
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
        if 'despesas_df' not in st.session_state:
            st.session_state['despesas_df'] = pd.DataFrame(columns=["Nome da despesa", "Data", "Categoria", "Forma de pagamento", "Tipo", "Valor"])
        st.session_state['despesas_df'] = pd.concat([st.session_state['despesas_df'], pd.DataFrame([nova_despesa])], ignore_index=True)
        st.success("Despesa adicionada com sucesso!")
        st.dataframe(st.session_state['despesas_df'])
def load_data():
    if 'despesas_df' not in st.session_state:
        # Dados iniciais carregados apenas uma vez
        data = [
            {"Nome da despesa": "Sephora", "Data": "2024-01-15", "Categoria": "beleza", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 750.99},
            {"Nome da despesa": "Farmácia", "Data": "2024-01-28", "Categoria": "saúde", "Forma de pagamento": "débito", "Tipo": "gasto", "Valor": 125.50},
            # Adicione outros registros conforme necessário
        ]
        df = pd.DataFrame(data)
        df['Data'] = pd.to_datetime(df['Data'])
        st.session_state['despesas_df'] = df
    else:
        df = st.session_state['despesas_df']  # Usa o DataFrame já carregado na sessão

    return df
def display_expense_view_options(df):
    st.subheader("Despesas")
    option = st.selectbox("Selecione uma visualização:", ["Todas as Despesas", "Por mês", "Por categoria", "Adicionar despesa"])
    if option == "Todas as Despesas":
        st.dataframe(st.session_state['despesas_df'])
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
df = load_data()
display_expense_view_options(df)
