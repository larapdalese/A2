import streamlit as st
import pandas as pd

# Criar DataFrame de despesas
df = pd.DataFrame(
    [
        {"Nome da despesa": "Sephora", "Valor": 750.99, "Categoria": "beleza", "Data": "2024-01-15"},
        {"Nome da despesa": "Farmácia", "Valor": 125.50, "Categoria": "saúde", "Data": "2024-01-28"},
        {"Nome da despesa": "Starbucks", "Valor": 36, "Categoria": "comida", "Data": "2024-02-05"},
        {"Nome da despesa": "Restaurante", "Valor": 80, "Categoria": "comida", "Data": "2024-02-18"},
        {"Nome da despesa": "Uber", "Valor": 15, "Categoria": "transporte", "Data": "2024-03-12"},
        {"Nome da despesa": "Táxi", "Valor": 25, "Categoria": "transporte", "Data": "2024-03-30"},
        {"Nome da despesa": "Saraiva", "Valor": 45.50, "Categoria": "livros", "Data": "2024-04-10"},
        {"Nome da despesa": "Livraria Cultura", "Valor": 60, "Categoria": "livros", "Data": "2024-04-25"},
        {"Nome da despesa": "Cinema", "Valor": 50, "Categoria": "lazer", "Data": "2024-05-15"},
        {"Nome da despesa": "Teatro", "Valor": 120, "Categoria": "lazer", "Data": "2024-05-20"},
        {"Nome da despesa": "Academia", "Valor": 200, "Categoria": "fitness", "Data": "2024-06-05"},
        {"Nome da despesa": "Yoga", "Valor": 150, "Categoria": "fitness", "Data": "2024-06-22"},
        {"Nome da despesa": "Pet Shop", "Valor": 80, "Categoria": "pets", "Data": "2024-07-11"},
        {"Nome da despesa": "Veterinário", "Valor": 300, "Categoria": "pets", "Data": "2024-07-25"},
        {"Nome da despesa": "Roupas", "Valor": 500, "Categoria": "vestuário", "Data": "2024-08-10"},
        {"Nome da despesa": "Sapatos", "Valor": 250, "Categoria": "vestuário", "Data": "2024-08-28"},
        {"Nome da despesa": "Mercado", "Valor": 400, "Categoria": "supermercado", "Data": "2024-09-10"},
        {"Nome da despesa": "Hortifruti", "Valor": 60, "Categoria": "supermercado", "Data": "2024-09-20"},
        {"Nome da despesa": "Curso Online", "Valor": 150, "Categoria": "educação", "Data": "2024-10-12"},
        {"Nome da despesa": "Workshop", "Valor": 200, "Categoria": "educação", "Data": "2024-10-26"},
        {"Nome da despesa": "Conserto carro", "Valor": 500, "Categoria": "transporte", "Data": "2024-11-05"},
        {"Nome da despesa": "Seguro carro", "Valor": 800, "Categoria": "transporte", "Data": "2024-11-22"},
        {"Nome da despesa": "Jantar especial", "Valor": 150, "Categoria": "lazer", "Data": "2024-12-15"},
        {"Nome da despesa": "Presente", "Valor": 100, "Categoria": "outros", "Data": "2024-12-25"}
    ]
)
df["Data"] = pd.to_datetime(df["Data"]).dt.date

# Título e entrada para orçamento
st.markdown("<h1 style='text-align: center;'>Orçamento do mês:</h1>", unsafe_allow_html=True)
orcamento = st.number_input("Insira o orçamento do mês:", min_value=0.0, format="%.2f")
st.markdown("<h2 style='text-align: center;'>Despesas</h2>", unsafe_allow_html=True)

# Opções de visualização
st.markdown("<h4 style='text-align: center;'>Selecione uma opção:</h4>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Todas as Despesas"):
        st.write(df)
with col2:
    mes_selecionado = st.selectbox("Por mês:", ["Tudo"] + list(pd.to_datetime(df["Data"]).dt.strftime("%Y-%m").unique()))
    if mes_selecionado:
        if mes_selecionado == "Tudo":
            despesas_filtradas = df
        else:
            despesas_filtradas = df[pd.to_datetime(df["Data"]).dt.strftime("%Y-%m") == mes_selecionado]
        st.write(despesas_filtradas)
with col3:
    categoria_selecionada = st.selectbox("Por categoria:", df["Categoria"].unique())
    if categoria_selecionada:
        despesas_categoria = df[df["Categoria"] == categoria_selecionada]
        st.write(despesas_categoria)

# Exibir total gasto
total_gasto = df["Valor"].sum()  # Calcular total de todas as despesas
st.markdown(f"<h3 style='text-align: center;'>Total Gasto: R$ {total_gasto:.2f}</h3>", unsafe_allow_html=True)

# Adicionar nova despesa
st.subheader("Adicionar nova despesa")
with st.form("nova_despesa_form"):
    nome_despesa = st.text_input("Nome da despesa")
    valor_despesa = st.number_input("Valor", min_value=0.0, format="%.2f")
    categoria_despesa = st.selectbox("Categoria", df["Categoria"].unique())
    data_despesa = st.date_input("Data", value=pd.to_datetime("today"))
    submitted = st.form_submit_button("Adicionar despesa")
    if submitted:
        nova_despesa = {
            "Nome da despesa": nome_despesa,
            "Valor": valor_despesa,
            "Categoria": categoria_despesa,
            "Data": data_despesa
        }
        df = df.append(nova_despesa, ignore_index=True)  # Adicionar nova despesa ao DataFrame
        st.success("Despesa adicionada com sucesso!")

# Exibir DataFrame atualizado
st.write(df)
