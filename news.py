### Alinne

st.set_page_config(layout="wide")

st.page_link("https://financedivas.streamlit.app", label="Início", icon="🏠")
st.page_link("pages/page_1.py", label="Gráficos")
st.page_link("pages/page_2.py", label="Insights de Gastos", disabled=True)
st.page_link("http://www.google.com", label="Notícias", icon="🌎")

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
