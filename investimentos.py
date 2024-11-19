#junção de possibilidades.py e bolsa.py
#aqui o ususário encontra possibilidades de investimentos e, ao final da página, uma raspagem da bolsa de valores
import streamlit as st
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import datetime
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
    """, unsafe_allow_html=True)
st.write("") 
url1 = "https://www.bv.com.br/bv-inspira/orientacao-financeira/comecar-a-investir"
url2 = "https://www.gov.br/investidor/pt-br/investir/como-investir/como-funciona-a-bolsa"
def raspar_conteudo(url):
    try:
        response = requests.get(url, timeout=10)  
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        conteudo = soup.find('h1')  
        return conteudo.text.strip() if conteudo else "Conteúdo não encontrado."
    except requests.exceptions.RequestException as e:
        return f"Erro de requisição: {e}"
    except Exception as e:
        return f"Erro inesperado: {e}"
col1, col2 = st.columns(2)
with col1:
    st.subheader("Desmistificação")
    try:
        conteudo_raspado1 = raspar_conteudo(url1)
        conteudo_raspado2 = raspar_conteudo(url2)
        st.markdown(f"[O que são investimentos?]({url1})")
        st.markdown(f"[O que é a bolsa de valores?]({url2})")
    except Exception as e:
        st.error(f"Erro ao raspar conteúdo: {e}")
with col2:
    st.subheader("Gráficos de cotação")
    st.markdown("<ul><li><span style='font-size: 24px;'>Dólar</span></li></ul>", unsafe_allow_html=True)
    ticker = 'USDBRL=X'
    today = datetime.datetime.today().strftime('%Y-%m-%d')  
    dados = yf.download(ticker, start='2023-01-01', end=today)
    if not dados.empty:
        st.line_chart(dados['Close'])
    else:
        st.error('Não foi possível obter os dados da cotação do dólar.')
