import streamlit as st
import pandas as pd
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
df["Data"] = pd.to_datetime(df["Data"])
meses_disponiveis = ["Tudo"] + list(df["Data"].dt.strftime("%Y-%m").unique())
mes_selecionado = st.selectbox("Selecione o mês (AAAA-MM) ou 'Tudo' para ver todos:", meses_disponiveis)
if mes_selecionado == "Tudo":
    despesas_filtradas = df
else:
    despesas_filtradas = df[df["Data"].dt.strftime("%Y-%m") == mes_selecionado]
if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = 0
tamanho_pagina = 10
total_paginas = (len(despesas_filtradas) - 1) // tamanho_pagina + 1
inicio = st.session_state.pagina_atual * tamanho_pagina
fim = inicio + tamanho_pagina
st.write(f"Despesas {inicio + 1} - {min(fim, len(despesas_filtradas))} de {len(despesas_filtradas)}")
st.write(despesas_filtradas.iloc[inicio:fim])
total_gasto = despesas_filtradas["Valor"].sum()
st.write(f"Total gasto: R$ {total_gasto:.2f}")
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("< Anterior") and st.session_state.pagina_atual > 0:
        st.session_state.pagina_atual -= 1
with col3:
    if st.button("Próximo >") and st.session_state.pagina_atual < total_paginas - 1:
        st.session_state.pagina_atual += 1
