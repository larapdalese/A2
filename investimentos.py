#junção de possibilidades.py e bolsa.py
#aqui o ususário encontra possibilidades de investimentos e, ao final da página, uma raspagem da bolsa de valores
import streamlit as st
import yfinance as yf
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
    <p class="centered-subtitle">Aqui você encontra possibilidades de investimentos, cotação do dólar e outros valores da bolsa atual. Sinta-se à vontade para aprender e, caso não entenda algo, a Maria Clara estará sempre à sua disposição<3</p>
    """, unsafe_allow_html=True)
ticker = 'USDBRL=X'
dados = yf.download(ticker, start='2023-01-01', end='2024-11-18')
if not dados.empty:
    st.line_chart(dados['Close'])
else:
    st.error('Não foi possível obter os dados da cotação do dólar.')
