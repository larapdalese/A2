#junção de possibilidades.py e bolsa.py
#aqui o ususário encontra possibilidades de investimentos e, ao final da página, uma raspagem da bolsa de valores
import streamlit as st
import yfinance as yf
import pandas as pd
st.title('Gráfico da Cotação do Dólar (USD/BRL)')
ticker = 'USDBRL=X'
dados = yf.download(ticker, start='2023-01-01', end='2024-11-18')
if not dados.empty:
    st.line_chart(dados['Close'])
else:
    st.error('Não foi possível obter os dados da cotação do dólar.')
