import streamlit as st
import pandas as pd
import plotly.express as px

# Criar DataFrame de despesas
df = pd.DataFrame([
    {"Nome da despesa": "Sephora", "Valor": 750.99, "Categoria": "beleza", "Data": "2024-01-15"},
    {"Nome da despesa": "Farmácia", "Valor": 125.50, "Categoria": "saúde", "Data": "2024-01-28"},
    # (continue com os dados como na sua versão anterior)
])
df["Data"] = pd.to_datetime(df["Data"])

# Título e entrada para orçamento
st.markdown("<h1 style='text-align: center;'>Orçamento do mês:</h1>", unsafe_allow_html=True)
orcamento = st.number_input("Insira o orçamento do mês:", min_value=0.0, format="%.2f")
st.markdown("<h2 style='text-align: center;'>Despesas</h2>", unsafe_allow_html=True)

# Opções de visualização com "Mais 2"
st.markdown("<h4 style='text-align: center;'>Selecione uma opção:</h4>", unsafe_allow_html=True)
opcao = st.selectbox("Opções:", ["Todas as despesas", "Por categoria", "Mais 2"])
sub_opcao = None

if opcao == "Mais 2":
    sub_opcao = st.selectbox("Selecione a sub-opção:", ["Por mês", "Outra opção"])

# Visualização à esquerda
col1, col2 = st.columns([1, 1.5])

with col1:
    if opcao == "Todas as despesas":
        st.write(df)
    elif opcao == "Por categoria":
        categoria_selecionada = st.selectbox("Selecione a categoria:", df["Categoria"].unique())
        despesas_categoria = df[df["Categoria"] == categoria_selecionada]
        st.write(despesas_categoria)
    elif sub_opcao == "Por mês":
        mes_selecionado = st.selectbox("Selecione o mês:", ["Tudo"] + list(df["Data"].dt.strftime("%Y-%m").unique()))
        if mes_selecionado != "Tudo":
            despesas_filtradas = df[df["Data"].dt.strftime("%Y-%m") == mes_selecionado]
        else:
            despesas_filtradas = df
        st.write(despesas_filtradas)

# Gráficos à direita
with col2:
    if opcao == "Por categoria":
        fig = px.pie(df, values='Valor', names='Categoria', title="Distribuição por Categoria")
        st.plotly_chart(fig)
        
        # Gráfico de linha por mês
        fig_line = px.line(df, x="Data", y="Valor", color="Categoria", title="Despesas Mensais")
        st.plotly_chart(fig_line)

# Total gasto
total_gasto = df["Valor"].sum()
st.markdown(f"<h3 style='text-align: center;'>Total Gasto: R$ {total_gasto:.2f}</h3>", unsafe_allow_html=True)

# Formulário para adicionar nova despesa
st.subheader("Adicionar nova despesa")
with st.form("nova_despesa_form"):
    nome_despesa = st.text_input("Nome da despesa")
    valor_despesa = st.number_input("Valor", min_value=0.0, format="%.2f")
    categoria_despesa = st.selectbox("Categoria", df["Categoria"].unique())
    data_despesa = st.date_input("Data", value=pd.to_datetime("today"))
    submitted = st.form_submit_button("Adicionar despesa")
    if submitted:
        nova_despesa = {"Nome da despesa": nome_despesa, "Valor": valor_despesa, "Categoria": categoria_despesa, "Data": data_despesa}
        df = pd.concat([df, pd.DataFrame([nova_despesa])], ignore_index=True)
        st.success("Despesa adicionada com sucesso!")
