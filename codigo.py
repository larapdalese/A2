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
        display_line_chart(df)  # Adicionar o gráfico de linhas logo abaixo do gráfico de pizza

    with col2:
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

# Função para exibir gráfico de linhas "Dinheiro ao longo do tempo" com opção de editar cores
def display_line_chart(df):
    st.subheader("Dinheiro ao longo do tempo")

    # Gráfico inicial com cores padrão
    df = df.sort_values('Data')  # Ordenar por data
    df_gastos = df[df['Tipo'] == 'gasto'].groupby('Data')['Valor'].sum().cumsum().reset_index()
    df_ganhos = df[df['Tipo'] == 'ganho'].groupby('Data')['Valor'].sum().cumsum().reset_index()

    gasto_color = "#FF6347"
    ganho_color = "#4682B4"

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_gastos['Data'], y=df_gastos['Valor'], mode='lines', name='Gastos', line=dict(color=gasto_color)))
    fig.add_trace(go.Scatter(x=df_ganhos['Data'], y=df_ganhos['Valor'], mode='lines', name='Ganhos', line=dict(color=ganho_color)))

    fig.update_layout(title="Evolução dos Gastos e Ganhos ao longo do tempo", xaxis_title="Data", yaxis_title="Valor Acumulado")
    st.plotly_chart(fig)

    # Opção para editar cores das linhas
    with st.expander("Editar"):
        st.markdown('<span class="small-text">Linha de ganhos</span>', unsafe_allow_html=True)
        ganho_color = st.color_picker("", ganho_color, key="ganho_color_picker")
        
        st.markdown('<span class="small-text">Linha de gastos</span>', unsafe_allow_html=True)
        gasto_color = st.color_picker("", gasto_color, key="gasto_color_picker")

        # Atualizar o gráfico com as novas cores
        fig.update_traces(selector=dict(name='Gastos'), line=dict(color=gasto_color))
        fig.update_traces(selector=dict(name='Ganhos'), line=dict(color=ganho_color))
        st.plotly_chart(fig)  # Renderizar o gráfico atualizado com novas cores

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

# Controle de navegação entre páginas
def main():
    apply_custom_css()
    main_page()

if __name__ == "__main__":
    main()
