#junção de possibilidades.py e bolsa.py
#aqui o ususário encontra possibilidades de investimentos e, ao final da página, uma raspagem da bolsa de valores
import streamlit as st
import yfinance as yf
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
    <p class="centered-subtitle">
        Aqui você encontra possibilidades de investimentos, cotação do dólar e outros valores da <br>
        bolsa atual. Caso não entenda algo, a Maria Clara estará sempre à sua disposição!<3
    </p>
    """, unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.subheader("Desmistificação")
    st.markdown("[O que são investimentos?](https://www.bv.com.br/bv-inspira/orientacao-financeira/comecar-a-investir)")
    st.markdown("[O que é a bolsa de valores?](https://www.gov.br/investidor/pt-br/investir/como-investir/como-funciona-a-bolsa)")
with col2:
    st.subheader("Gráficos de Cotação")
    def exibir_grafico_cotacao(ticker, moeda):
        today = datetime.datetime.today().strftime('%Y-%m-%d')  
        dados = yf.download(ticker, start='2023-01-01', end=today)
        if not dados.empty:
            st.markdown(f"**{moeda}**")
            st.line_chart(dados['Close'])
        else:
            st.error(f'Não foi possível obter os dados da cotação do {moeda}.')
    exibir_grafico_cotacao('USDBRL=X', 'Dólar')
    exibir_grafico_cotacao('EURBRL=X', 'Euro')
