import streamlit as st
import pandas as pd
import plotly.express as px

import streamlit as st

# Título do aplicativo
st.title("Meu Perfil")

# CSS para estilização
st.markdown(
    """
    <style>
    .header {
        position: relative;
        width: 100%;
        height: 200px;  /* Altura da imagem de cabeçalho */
        overflow: hidden;
    }
    
    .header img {
        width: 100%;
        height: auto;
    }
    
    .profile-photo {
        position: absolute;
        bottom: -50px;  /* Ajuste para posicionar a imagem do perfil */
        left: 20px;     /* Distância do lado esquerdo */
        border-radius: 50%;
        width: 100px;  /* Tamanho da imagem do perfil */
        height: 100px; /* Tamanho da imagem do perfil */
        border: 3px solid white;  /* Borda branca */
    }

    .user-info {
        margin-top: 70px;  /* Espaço abaixo da imagem do perfil */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Exibir foto de cabeçalho
header_image = "https://i.pinimg.com/564x/3f/a6/9f/3fa69f6c8b6f7dbf8fccd3ac7ee5b2b3.jpg"
profile_photo = "https://i.pinimg.com/564x/86/8d/ab/868dab99f9d90a367c320a170ab9eab3.jpg"

st.markdown(
    f"""
    <div class="header">
        <img src="{header_image}" alt="Header Image">
        <img class="profile-photo" src="{profile_photo}" alt="Profile Photo">
    </div>
    """,
    unsafe_allow_html=True
)

# Adicionar informações do usuário
st.markdown("""
    <div class="user-info">
        ### Nome do Usuário
        - Bio: Aqui está uma breve descrição sobre você.
        - Localização: Cidade, País
        - Interesses: Interesses que você gostaria de compartilhar.
    </div>
    """,
    unsafe_allow_html=True
)

# Adicione mais elementos abaixo conforme necessário

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


# Criar DataFrame de despesas
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
)
df["Data"] = pd.to_datetime(df["Data"])


# Título e entrada para orçamento
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
