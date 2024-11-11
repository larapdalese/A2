### Alinne

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

### OBS: ESTÁ SENDO FEITO O USO DE API, SOMENTE SÃO POSSÍVEIS 100 PESQUISAS MENSAIS!!!

import requests
import pandas as pd
import json

# Defina os parâmetros da pesquisa
params = {
    'api_key': '09b0486c1e432e382a217aaafdf24358f019d8e2ed14e7cee0b6d19e5586a62c'
    'engine': 'google',
    'q': 'Coffee',
    'location': 'Brazil',
    'google_domain': 'google.com.br',
    'gl': 'br',
    'hl': 'pt'
}

url = 'https://serpapi.com/search.json?engine=google&q=Coffee&location=Brazil&google_domain=google.com.br&gl=br&hl=pt&api_key=09b0486c1e432e382a217aaafdf24358f019d8e2ed14e7cee0b6d19e5586a62c'

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
#   print(json.dumps(data, indent=4))  # Exibe o JSON formatado, apenas para entender a estrutura

    organic_results = data.get('organic_results', [])

    if organic_results:
        df = pd.DataFrame(organic_results)
        df[['position', 'title', 'link', 'snippet']].head()
    else:
        print("Nenhum resultado orgânico encontrado.")
else:
    print(f"Erro na requisição. Status Code: {response.status_code}")


###
