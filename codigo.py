import streamlit as st
import pandas as pd
import plotly.express as px

# Supondo que você já tenha um DataFrame df preparado anteriormente

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
    escolha = st.radio("Opções", ["Todas as Despesas", "Por Categoria", "Mais 4"])

    # Exibir DataFrames de acordo com a opção escolhida
    if escolha == "Todas as Despesas":
        st.write(df)
    elif escolha == "Por Categoria":
        categoria_selecionada = st.selectbox("Escolha uma categoria:", df["Categoria"].unique())
        despesas_categoria = df[df["Categoria"] == categoria_selecionada]
        st.write(despesas_categoria)
    elif escolha == "Mais 4":
        escolha_mais_4 = st.radio("Opções adicionais", ["Por mês", "Gastos totais ao longo do tempo", "Categorias ao longo dos meses", "Adicionar despesa"])
        
        if escolha_mais_4 == "Por mês":
            mes_selecionado = st.selectbox("Selecione o mês:", ["Tudo"] + list(df["Data"].dt.to_period("M").astype(str).unique()))
            if mes_selecionado == "Tudo":
                st.write(df)
            else:
                despesas_mes = df[df["Data"].dt.to_period("M").astype(str) == mes_selecionado]
                st.write(despesas_mes)
                
        elif escolha_mais_4 == "Gastos totais ao longo do tempo":
            df["AnoMes"] = df["Data"].dt.to_period("M").astype(str)
            despesas_por_mes = df.groupby("AnoMes")["Valor"].sum().reset_index()
            fig_gastos_totais = px.line(despesas_por_mes, x="AnoMes", y="Valor", title="Gastos Totais ao Longo do Tempo")
            st.plotly_chart(fig_gastos_totais, use_container_width=True)
        
        elif escolha_mais_4 == "Categorias ao longo dos meses":
            df["Mes"] = df["Data"].dt.month
            despesas_por_categoria_mes = df.groupby(["Mes", "Categoria"])["Valor"].sum().reset_index()
            fig_categorias_mensais = px.bar(despesas_por_categoria_mes, x="Mes", y="Valor", color="Categoria", 
                                             title="Categorias ao Longo dos Meses", barmode="group")
            st.plotly_chart(fig_categorias_mensais, use_container_width=True)

        elif escolha_mais_4 == "Adicionar despesa":
            with st.form(key='my_form'):
                nome_despesa = st.text_input("Nome da despesa:")
                data_despesa = st.date_input("Data da despesa:")
                categoria_despesa = st.selectbox("Categoria:", df["Categoria"].unique())
                forma_pagamento = st.selectbox("Forma de pagamento:", ["crédito", "débito", "pix"])
                valor_despesa = st.number_input("Valor da despesa:", min_value=0.0, format="%.2f")
                
                submit_button = st.form_submit_button(label='Adicionar despesa')
                
                if submit_button:
                    nova_despesa = {
                        "Nome da despesa": nome_despesa,
                        "Data": data_despesa,
                        "Categoria": categoria_despesa,
                        "Forma de pagamento": forma_pagamento,
                        "Tipo": "gasto",
                        "Valor": valor_despesa
                    }
                    df = df.append(nova_despesa, ignore_index=True)  # Adiciona a nova despesa ao DataFrame
                    st.success("Despesa adicionada com sucesso!")
                    st.write(df)  # Exibe o DataFrame atualizado
