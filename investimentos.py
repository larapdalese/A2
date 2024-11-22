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
    st.subheader("Investimentos de Baixo Risco")
    st.markdown("""
        - **Tesouro Direto**: Um dos investimentos mais seguros do Brasil, ideal para quem busca estabilidade.
        - **CDBs de Bancos Grandes**: Certificados de Depósito Bancário que oferecem segurança e rendimento superior à poupança.
        - **Fundos de Renda Fixa**: Alternativa para diversificar e manter um risco controlado.
        - **Poupança**: Apesar de menos rentável, ainda é uma opção segura para reservas de emergência.
    """)
    st.markdown("[Saiba mais sobre opções de baixo risco](https://www.tesourodireto.com.br/)")
with col2:
    st.subheader("Gráficos de Cotação")
    def exibir_grafico_cotacao(ticker, moeda):
        today = datetime.datetime.today().strftime('%Y-%m-%d')  
        dados = yf.download(ticker, start='2023-01-01', end=today)     
        if not dados.empty and 'Close' in dados.columns:
            st.markdown(f"**{moeda}**")
            st.line_chart(dados['Close'])
            cotacao_dia = dados['Close'].iloc[-1]  
            st.write(f"Cotação do dia: R$ {cotacao_dia:.2f}")
            if len(dados) >= 30:
                media_30_dias = dados['Close'][-30:].mean()
                st.write(f"Média dos últimos 30 dias: R$ {media_30_dias:.2f}")
            else:
                st.write("Média dos últimos 30 dias: Não disponível (menos de 30 dias de dados)")
        else:
            st.error(f'Não foi possível obter os dados da cotação do {moeda} ou a coluna "Close" está ausente.')
    exibir_grafico_cotacao('USDBRL=X', 'Dólar')
    exibir_grafico_cotacao('EURBRL=X', 'Euro')
