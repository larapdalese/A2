import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from groq import Groq
import os
import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yfinance as yf
import datetime

def home_page():
    st.set_page_config(layout="wide", page_title="Home")
    image_path = "logo.png"
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        st.image(image_path, caption=None, width=300, use_column_width=False, clamp=False, channels="RGB", output_format="auto")
    
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
            </style>
        """, unsafe_allow_html=True)
    
    apply_custom_css()

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
            display_expense_view_options(df)
            display_insights(df)
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
            names='Categoria',
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
    def main():
        df = load_data()
        if 'df_despesas' in st.session_state:
            df = st.session_state.df_despesas
        display_budget_section(df)
    def display_expense_view_options(df):
        st.subheader("Despesas")
        option = st.selectbox("Selecione uma visualização:", ["Todas as Despesas", "Por mês", "Por categoria", "Adicionar despesa", "Editar planilha"])
        if option == "Todas as Despesas":
            if 'df_despesas' in st.session_state:
                st.dataframe(st.session_state.df_despesas)
            else:
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
        elif option == "Editar planilha":
            edit_expense(df)
    def add_expense(df):
        st.subheader("Adicionar nova despesa")
        if 'df_despesas' not in st.session_state:
            st.session_state.df_despesas = df.copy() 
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
            st.session_state.df_despesas = pd.concat([st.session_state.df_despesas, pd.DataFrame([nova_despesa])], ignore_index=True)
            st.success("Despesa adicionada com sucesso!")
            st.dataframe(st.session_state.df_despesas)
    df = load_data()
    def edit_expense(df):
        st.subheader("Editar Planilha")
        if 'df_despesas' not in st.session_state:
            st.session_state.df_despesas = df.copy()
        df_display = st.session_state.df_despesas.reset_index(drop=True).copy()
        st.dataframe(df_display)
        linha_para_excluir = st.number_input("Número da linha para excluir (baseado no índice):", min_value=0, max_value=len(df_display)-1, step=1)
        if st.button("Excluir linha"):
            st.session_state.df_despesas = st.session_state.df_despesas.drop(index=linha_para_excluir).reset_index(drop=True)
            st.success(f"Linha {linha_para_excluir} excluída com sucesso!")
            st.dataframe(st.session_state.df_despesas)
        if st.button("Reordenar linhas"):
            st.session_state.df_despesas = st.session_state.df_despesas.sort_values(by="Data").reset_index(drop=True)
            st.success("Linhas reordenadas por Data!")
            st.dataframe(st.session_state.df_despesas)
    def add_expense(df):
        st.subheader("Adicionar nova despesa") 
        if 'df_despesas' not in st.session_state:
            st.session_state.df_despesas = df.copy()
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
            st.session_state.df_despesas = pd.concat([st.session_state.df_despesas, pd.DataFrame([nova_despesa])], ignore_index=True)
            st.success("Despesa adicionada com sucesso!")
            st.dataframe(st.session_state.df_despesas)
    main()

def graphs_page():
    st.write("Página de Dicas. Coloque aqui as informações e funcionalidades da página de dicas.")

def mariaclara_page():
    st.set_page_config(layout="wide", page_title="Maria Clara - CHATBOT")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Oi, meu nome é Maria Clara! Como posso te ajudar hoje?"}]
    
    api_key = "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"
    
    def generate_groq_response(prompt_input):
        client = Groq(api_key=api_key)
    
        messages = [
            {"role": "system", "content": (
                "Você é uma assistente de educação financeira para mulheres chamada Maria Clara. "
                "Seu objetivo é ajudar as usuárias com dúvidas sobre finanças, explicando conceitos financeiros "
                "de maneira clara e oferecendo conselhos úteis. Sempre forneça respostas completas e evite fazer muitas perguntas. "
                "Tente explicar o máximo possível e se necessário, forneça exemplos. "
                "Ao final de cada resposta, diga que espera ter ajudado e deseja sucesso na jornada financeira."
            )}
        ]
    
        for dict_message in st.session_state.messages:
            messages.append(dict_message)
    
        messages.append({"role": "user", "content": prompt_input})
    
        try:
            chat_completion = client.chat.completions.create(
                messages=messages,
                model="llama3-groq-8b-8192-tool-use-preview",
                temperature=0.5,
                max_tokens=3000,
                top_p=0.9,
                stop=[],
                stream=None,
            )
    
            return chat_completion.choices[0].message.content
    
        except Exception as e:
            return f"Erro ao chamar a API Groq: {str(e)}"
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    def clear_chat_history():
        st.session_state.messages = [{"role": "assistant", "content": "Como posso te ajudar hoje, diva?"}]
    st.sidebar.button('Limpar histórico de chat', on_click=clear_chat_history)
    
    if prompt := st.chat_input("Digite sua pergunta:"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
    
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."): 
                response = generate_groq_response(prompt)
                st.write(response)
    
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)


def indicacoes_page():
    st.set_page_config(layout="wide", page_title="Indicações")
    
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
            </style>
        """, unsafe_allow_html=True)
    
    apply_custom_css()

    os.environ['SPOTIPY_CLIENT_ID'] = '5dd03bf3704a4a2a903f136a7fd6c593' 
    os.environ['SPOTIPY_CLIENT_SECRET'] = 'b13072de7dcf4d58ab6104e68fa649c4'
    
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
    
    def buscar_noticias(termo=None):
        api_key = "d700b8cb09b888dc838bf50109bedd9e"
        temas_principais = "finanças OR empreendedorismo OR economia"
        query = f"{temas_principais} {termo}" if termo else temas_principais
        url = f"https://gnews.io/api/v4/search?q={query}&lang=pt&token={api_key}&max=5"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"articles": []}
    
    def buscar_podcast_por_id(podcast_id):
        try:
            podcast = sp.show(podcast_id)
            return {
                "name": podcast["name"],
                "description": podcast["description"],
                "url": podcast["external_urls"]["spotify"],
                "image": podcast["images"][0]["url"] if podcast["images"] else None
            }
        except Exception as e:
            st.error(f"Erro ao buscar o podcast '{podcast_id}': {e}")
            return None
    
    def buscar_podcasts():
        temas = "finanças OR feminismo OR empreendedorismo feminino"
        resultados = sp.search(q=temas, type='show', limit=10)
        podcasts_filtrados = [
            {
                "name": podcast['name'],
                "description": podcast['description'],
                "url": podcast['external_urls']['spotify'],
                "image": podcast['images'][0]['url'] if podcast['images'] else None
            }
            for podcast in resultados['shows']['items']
            if any(
                t in podcast['name'].lower() or t in podcast['description'].lower()
                for t in ["finanças", "economia", "empreendedorismo", "feminino"]
            )
        ]
        return podcasts_filtrados[:4]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.title("Notícias")
        st.markdown("Pesquise notícias sobre **Finanças**, **Empreendedorismo** e **Economia**.")
    
        termo_busca = st.text_input("Digite um termo para refinar a pesquisa (opcional):", key="noticias")
        if st.button("Pesquisar Notícias", key="botao_noticias"):
            noticias = buscar_noticias(termo_busca)
    
            if noticias['articles']:
                st.success(f"Exibindo as últimas notícias sobre '{termo_busca or 'temas gerais'}'")
                for artigo in noticias['articles']:
                    st.subheader(artigo['title'])
                    st.markdown(f"Fonte: [{artigo['source']['name']}]({artigo['url']})")
                    st.write(artigo['description'])
                    if 'image' in artigo and artigo['image']:
                        st.image(artigo['image'], caption="Imagem da notícia", use_column_width=True)
                    st.write("---")
            else:
                st.warning("Nenhuma notícia encontrada para o tema pesquisado.")
    
    with col2:
        st.title("Podcasts")
        if st.button("Carregar Podcasts", key="botao_podcasts"):
            try:
                podcast_nao_te_empodero = buscar_podcast_por_id("21xaGKadO9f43mpihiAzhX")
                outros_podcasts = buscar_podcasts()
                podcasts = [podcast_nao_te_empodero] + outros_podcasts if podcast_nao_te_empodero else outros_podcasts
    
                if podcasts:
                    for podcast in podcasts[:5]:
                        st.write(f"### {podcast['name']}")
                        if 'image' in podcast and podcast['image']:
                            st.image(podcast['image'], width=200)
                        else:
                            st.warning("Imagem não disponível.")
    
                        with st.expander("Leia mais"):
                            st.write(podcast['description'])
                        
                        st.write(f"[Ouvir no Spotify]({podcast['url']})")
                        st.write("---")
                else:
                    st.warning("Nenhum podcast encontrado para os temas selecionados.")
            except Exception as e:
                st.error(f"Erro ao buscar os podcasts: {e}")

def insights_page():
    st.write("Página de Possibilidades. Coloque aqui as informações e funcionalidades da página de Possibilidades.")


def investimentos_page():
    st.set_page_config(layout="wide", page_title="Investimentos")

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
            </style>
        """, unsafe_allow_html=True)

    apply_custom_css()
    
    st.markdown("""
        <style>
        .centered-title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
        }
        .centered-subtitle {
            text-align: center;
            font-size: 18px;
        }
        </style>
        <h1 class="centered-title">Investimentos</h1>
        <p class="centered-subtitle">
            Aqui você encontra possibilidades de investimentos, cotação do dólar e outros valores da <br>
            bolsa atual. Caso não entenda algo, a Maria Clara estará sempre à sua disposição!<3
        </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Tipos de investimento")
        st.markdown("Saiba um pouco mais sobre investimentos e as alternativas para o dinheiro que está sobrando na conta e que você não deseja gastar com mimos, clique nas palavras azuis sublinhadas para ser direcionada a páginas que te trarão mais informações sobre os tipos de investimentos.")
        st.markdown("""
        <style>
        .custom-subsubtitle {
            font-size: 20px; 
            font-weight: bold; 
            margin-bottom: 10px; 
        }
        </style>
        <p class="custom-subsubtitle">Investimentos de baixo risco</p>
    """, unsafe_allow_html=True)
        st.markdown("Rendem menos & são mais seguros!")
        st.markdown("""
            - **Tesouro Direto**: 
            [Um dos investimentos mais seguros do Brasil, ideal para quem busca estabilidade.](https://www.tesourodireto.com.br/)
        """)
        st.markdown("""
            - **CDB**: 
            [Certificados de Depósito Bancário que oferecem segurança e rendimento superior à poupança, cada banco possui o seu.](https://www.b3.com.br/pt_br/produtos-e-servicos/registro/renda-fixa-e-valores-mobiliarios/certificado-de-deposito-bancario.htm)
        """)
        st.markdown("""
            - **Poupança**: 
            [Apesar de menos rentável, ainda é uma opção segura para reservas de emergência.](https://www.gov.br/pt-br/servicos-estaduais/conta-poupanca)
        """)
        st.markdown("""
        <style>
        .custom-subsubtitle {
            font-size: 20px; 
            font-weight: bold; 
            margin-bottom: 10px; 
        }
        </style>
        <p class="custom-subsubtitle">Investimentos de médio risco</p>
    """, unsafe_allow_html=True)
    with col2:
        st.subheader("Gráficos de Cotação")
        def exibir_grafico_cotacao(ticker, moeda):
            today = datetime.datetime.today().strftime('%Y-%m-%d')  # Data atual
            dados = yf.download(ticker, start='2023-01-01', end=today)
            if not dados.empty:
                st.markdown(f"**{moeda}**")
                st.line_chart(dados['Close'])
            else:
                st.error(f'Não foi possível obter os dados da cotação do {moeda}.')
        exibir_grafico_cotacao('USDBRL=X', 'Dólar')
        exibir_grafico_cotacao('EURBRL=X', 'Euro')


pages = {
    "Essencial": [
        st.Page(home_page, title="Home", icon=None, url_path=None, default=False),
        st.Page(graphs_page, title="Gráficos", icon=None, url_path=None, default=False),
        st.Page(mariaclara_page, title="Maria Clara - Chatbot", icon=None, url_path=None, default=False),
    ],
    "Investimentos": [
       st.Page(indicacoes_page, title="Indicações", icon=None, url_path=None, default=False),
       st.Page(insights_page, title="Insights", icon=None, url_path=None, default=False),
       st.Page(investimentos_page, title="Invista como uma garota", icon=None, url_path=None, default=False),
    ],
}

pg = st.navigation(pages, position="sidebar", expanded=False)
pg.run()
