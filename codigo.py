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
        .edit-link {
            font-size: 0.8em;
            color: #3498db;
            text-decoration: underline;
            cursor: pointer;
            margin-top: 10px;
        }
        .small-text {
            font-size: 0.8em;
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
        display_money_over_time(df)

    with col2:
        st.write("")  # Espaço vazio para alinhamento
        display_expense_view_options(df)

# Função para exibir gráfico de despesas por categoria com edição de cores
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

    # Configurar cores padrão para as categorias
    if "categoria_cores" not in st.session_state:
        st.session_state["categoria_cores"] = {cat: px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)]
                                               for i, cat in enumerate(despesas_por_categoria["Categoria"].unique())}

    # Criar gráfico de pizza com cores personalizáveis
    fig = px.pie(
        despesas_por_categoria,
        values='Valor',
        names='Categoria',
        title='Distribuição das Despesas por Categoria',
        color_discrete_map=st.session_state["categoria_cores"]
    )
    st.plotly_chart(fig)

    # Botão para editar cores das categorias
    if st.button("Editar", key="edit_pie_chart"):
        with st.expander("Opções de Cores para Categorias", expanded=True):
            st.write("Escolha as cores para cada categoria:")
            for categoria in despesas_por_categoria["Categoria"].unique():
                nova_cor = st.color_picker(f"Cor para {categoria}", st.session_state["categoria_cores"][categoria], key=f"cor_{categoria}")
                st.session_state["categoria_cores"][categoria] = nova_cor

# Função para exibir o gráfico de linha de dinheiro ao longo do tempo com edição de cores
def display_money_over_time(df):
    st.subheader("Dinheiro ao Longo do Tempo")
    df_sorted = df.sort_values("Data")
    df_ganhos = df_sorted[df_sorted["Tipo"] == "ganho"]
    df_gastos = df_sorted[df_sorted["Tipo"] == "gasto"]

    fig = go.Figure()
    ganhos_color = st.session_state.get("ganhos_color", "#1f77b4")
    gastos_color = st.session_state.get("gastos_color", "#ff7f0e")

    fig.add_trace(go.Scatter(x=df_ganhos["Data"], y=df_ganhos["Valor"].cumsum(), mode="lines", name="Ganhos", line=dict(color=ganhos_color)))
    fig.add_trace(go.Scatter(x=df_gastos["Data"], y=df_gastos["Valor"].cumsum(), mode="lines", name="Gastos", line=dict(color=gastos_color)))
    st.plotly_chart(fig)

    # Botão para editar cores das linhas
    if st.button("Editar", key="edit_line_chart"):
        with st.expander("Opções de Cores para Linhas", expanded=True):
            st.write("Escolha as cores para as linhas:")
            st.session_state["ganhos_color"] = st.color_picker("Linha de Ganhos", ganhos_color, key="ganhos_color")
            st.session_state["gastos_color"] = st.color_picker("Linha de Gastos", gastos_color, key="gastos_color")

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
        with st.form("nova_despesa"):
            nome = st.text_input("Nome da despesa")
            data = st.date_input("Data")
            categoria = st.selectbox("Categoria", df["Categoria"].unique())
            forma_pagamento = st.selectbox("Forma de pagamento", ["débito", "crédito", "pix"])
            valor = st.number_input("Valor", min_value=0.0)
            if st.form_submit_button("Adicionar"):
                nova_despesa = {"Nome da despesa": nome, "Data": pd.to_datetime(data), "Categoria": categoria, 
                                "Forma de pagamento": forma_pagamento, "Tipo": "gasto", "Valor": valor}
                df = df.append(nova_despesa, ignore_index=True)
                st.success("Despesa adicionada com sucesso!")

# Função principal para executar o app
def main():
    apply_custom_css()
    df = load_data()
    display_budget_section(df)

if __name__ == "__main__":
    main()
