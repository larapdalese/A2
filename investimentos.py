#junção de possibilidades.py e bolsa.py
#aqui o ususário encontra possibilidades de investimentos e, ao final da página, uma raspagem da bolsa de valores
import streamlit as st
import yfinance as yf
import requests
from bs4 import BeautifulSoup
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
def raspar_conteudo(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')
        conteudo = soup.find('div')  
        return conteudo.text.strip() if conteudo else "Conteúdo não encontrado."
    except requests.exceptions.RequestException as e:
        return f"Erro de requisição: {e}"
    except Exception as e:
        return f"Erro inesperado: {e}"
col1, col2 = st.columns(2)
with col1:
    st.subheader("Desmistificação")
    try:
        conteudo_raspado = raspar_conteudo(url)
        st.write("Raspagem concluída com sucesso.")  
    except Exception as e:
        st.error(f"Erro ao raspar conteúdo: {e}")
        conteudo_raspado = None
