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
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    conteudo = soup.find('div', class_='bv-text')  
    return conteudo.text.strip() if conteudo else "Conteúdo não encontrado."
col1, col2 = st.columns(2)
with col1:
    st.subheader("Desmistificação")
    conteudo_raspado = raspar_conteudo(url)
    if conteudo_raspado != "Conteúdo não encontrado.":
        st.markdown(f"""
            <div>
                <h4>O que são investimentos?</h4>
                <p>{conteudo_raspado[:300]}... <a href="{url}" target="_blank">Leia mais</a></p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.error("Não foi possível encontrar o conteúdo.")
