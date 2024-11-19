#junção de possibilidades.py e bolsa.py
#aqui o ususário encontra possibilidades de investimentos e, ao final da página, uma raspagem da bolsa de valores
import streamlit as st
import yfinance as yf
import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd 
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
    st.subheader("Gráficos de Cotação")
    def exibir_grafico_cotacao(ticker, moeda):
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        data_inicio = (datetime.datetime.today() - datetime.timedelta(days=180)).strftime('%Y-%m-%d')  
        dados = yf.download(ticker, start=data_inicio, end=today)
        if not dados.empty:
            st.markdown(f"**{moeda}**")
            st.line_chart(dados['Close'])
            cotacao_dia = dados['Close'].iloc[-1]
            if not pd.isnull(cotacao_dia): 
                cotacao_dia = float(cotacao_dia)
                media_30_dias = float(dados['Close'][-30:].mean())
                media_3_meses = float(dados['Close'][-90:].mean())
                variacao_percentual = ((cotacao_dia - media_3_meses) / media_3_meses) * 100
                st.write(f"Cotação do dia: {cotacao_dia:.2f}")
                st.write(f"Média dos últimos 30 dias: {media_30_dias:.2f}")
                if st.button(f"É um bom momento para comprar {moeda.lower()}?"):
                    if cotacao_dia < media_3_meses:
                        st.write(f"Sim, porque o valor de hoje é {cotacao_dia:.2f}, {abs(variacao_percentual):.2f}% abaixo da média dos últimos 3 meses ({media_3_meses:.2f}).")
                    else:
                        st.write(f"Não, porque o valor de hoje é {cotacao_dia:.2f}, {variacao_percentual:.2f}% acima da média dos últimos 3 meses ({media_3_meses:.2f}).")

                    if st.button("Obrigada!"):
                        st.empty()  
            else:
                st.warning(f"A cotação do dia não está disponível para o {moeda}.")
        else:
            st.error(f'Não foi possível obter os dados da cotação do {moeda}.')
    exibir_grafico_cotacao('USDBRL=X', 'Dólar')
    exibir_grafico_cotacao('EURBRL=X', 'Euro')
