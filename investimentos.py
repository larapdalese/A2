#junção de possibilidades.py e bolsa.py
#aqui o ususário encontra possibilidades de investimentos e, ao final da página, uma raspagem da bolsa de valores
import streamlit as st
import yfinance as yf
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
st.write("") 
col1, col2 = st.columns(2)
with col1:
    st.subheader("Desmistificação")
    st.markdown(
        """
        <iframe src="https://www.bv.com.br/bv-inspira/orientacao-financeira/comecar-a-investir" 
        width="100%" height="600px" frameborder="0"></iframe>
        """, 
        unsafe_allow_html=True
    )
