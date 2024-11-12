### Alinne

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from google_search_results import GoogleSearch

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

### OBS: ESTÁ SENDO FEITO O USO DE API, SOMENTE SÃO POSSÍVEIS 100 PESQUISAS MENSAIS!!!

def search_edufinance(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": "ee383981e582d0ebe2db86c966c9f63b004483a9c8263b8bf99d057ad9fc83b7"
        "location": "Brazil",
        "google_domain": "google.com.br",
        "gl": "br",
        "hl": "pt",
        "safe": "active",
        "tbm": "nws",
        "start": "0",
        "num": "1"
    }
    search = GoogleSearch(params)
    organic_results = search.get_hash().get('organic_results', [])
    return organic_results

st.title("Pesquisa do Google - Educação Financeira")
query = st.text_input("Digite o termo de pesquisa", "educação financeira")

if st.button("Buscar"):
    results = search_edufinance(query)
    if results:
        st.write(f"Encontrei {len(results)} resultados para '{query}':")
        for result in results:
            st.write(f"**{result['title']}**")
            st.write(f"[Link]({result['link']})")
    else:
        st.write("Nenhum resultado encontrado.")

###
