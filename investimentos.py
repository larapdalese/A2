#junção de possibilidades.py e bolsa.py
#aqui o ususário encontra possibilidades de investimentos e, ao final da página, uma raspagem da bolsa de valores
import streamlit as st
import yfinance as yf
import datetime
import altair as alt
st.set_page_config(layout="wide", page_title="Investimentos")
def apply_custom_css():
    st.markdown("""
        <style>
        .main .block-container {
            padding-top: 0rem; /* Remove o espaço do container principal */
            padding-bottom: 1rem;
            padding-left: 0.5rem;
            padding-right: 0.5rem;
            max-width: 100%;
        }
        .centered-title {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-top: -50px; /* Valor aumentado para subir ainda mais */
        }
        </style>
    """, unsafe_allow_html=True)
apply_custom_css()
st.markdown("""
    <h1 class="centered-title">Investimentos</h1>
    """, unsafe_allow_html=True)
st.write("")
st.write("")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Tipos de investimento")
    st.markdown("Saiba um pouco mais sobre investimentos e as alternativas para o dinheiro que está sobrando na conta e que você não deseja gastar com mimos, clique nas palavras azuis sublinhadas para ser direcionada a páginas que te trarão mais informações sobre os tipos de investimentos.")
    st.markdown("""
    <style>
    .custom-subsubtitle {
        font-size: 20px; 
        font-weight: bold; 
        margin-bottom: 10px; 
    }
    </style>
    <p class="custom-subsubtitle">Investimentos de baixo risco</p>
""", unsafe_allow_html=True)
    st.markdown("Rendem menos & são mais seguros!")
    st.markdown("""
        - **Tesouro Direto**: 
        [Um dos investimentos mais seguros do Brasil, ideal para quem busca estabilidade.](https://www.tesourodireto.com.br/)
    """)
    st.markdown("""
        - **CDB**: 
        [Certificados de Depósito Bancário que oferecem segurança e rendimento superior à poupança, cada banco possui o seu.](https://www.b3.com.br/pt_br/produtos-e-servicos/registro/renda-fixa-e-valores-mobiliarios/certificado-de-deposito-bancario.htm)
    """)
    st.markdown("""
        - **Poupança**: 
        [Apesar de menos rentável, ainda é uma opção segura para reservas de emergência.](https://www.gov.br/pt-br/servicos-estaduais/conta-poupanca)
    """)
    st.markdown("""
    <style>
    .custom-subsubtitle {
        font-size: 20px; 
        font-weight: bold; 
        margin-bottom: 10px; 
    }
    </style>
    <p class="custom-subsubtitle">Investimentos de médio risco</p>
""", unsafe_allow_html=True)
    st.markdown("Rendem um pouco mais que os de baixo risco & as chances de você perder seu dinheiro não são altas!")
    st.markdown("""
        - **Fundos Imobiliários**: 
        [ Fundos que investem em imóveis (como shoppings e escritórios) ou em títulos relacionados ao mercado imobiliário, oferecem dividendos mensais (aluguéis) e têm potencial de valorização.](https://fiis.com.br/)
    """)
    st.markdown("""
        - **Ações de Empresas Consolidadas**: 
        [Investimento em empresas com histórico estável e boa governança, como bancos e empresas de energia, oferecem ganhos de valorização e dividendos.](https://borainvestir.b3.com.br/objetivos-financeiros/investir-melhor/descomplicando-as-blue-chips-tudo-o-que-voce-tem-que-saber/?gclid=Cj0KCQiAuou6BhDhARIsAIfgrn4PBJ0mHiZPbEOReROu8PAUVwltoUxjd9QJF78X4ZVu5DDhiHyJggkaAs-wEALw_wcB)
    """)
    st.markdown("""
        - **Tesouro Direto**: 
        [Título público atrelado à inflação e com pagamentos semestrais de juros, protege contra a inflação e oferece retornos previsíveis.](https://www.tesourodireto.com.br/)
    """)
    st.markdown("""
    <style>
    .custom-subsubtitle {
        font-size: 20px; 
        font-weight: bold; 
        margin-bottom: 10px; 
    }
    </style>
    <p class="custom-subsubtitle">Investimentos de alto risco</p>
""", unsafe_allow_html=True)
    st.markdown("São os que mais rendem & tem as maiores chances de perda! Dica? Faça com aquele dinheiro que você têm certeza de que não precisará, que está mesmo disposta a arriscar")
    st.markdown("""
        - **Câmbio**: 
        [Investimentos abertos atrelados a moedas estrangeiras, como dólar ou euro.](https://www.modalmais.com.br/blog/cambio-como-funciona/)
    """)
    st.markdown("""
        - **Criptomoedas**: 
        [Moeda digital que não depende de sistema bancário.](https://investalk.bb.com.br/noticias/quero-aprender/criptomoedas-e-suas-oportunidades-de-investimento-o-guia-investalk-cripto)
    """)
    st.markdown("""
        - **Day Trade**: 
        [compra e venda de ativos dentro de um único dia de negociação, exige conhecimento profundo do mercado, habilidades técnicas avançadas e capacidade de tomar decisões rápidas.](https://borainvestir.b3.com.br/glossario/day-trade/?gclid=Cj0KCQiAuou6BhDhARIsAIfgrn6fiKkHF_iJl9jPtah1vdWo9gcNFfZRd07HkfqIjOjYUVDw1kjcE4MaAopOEALw_wcB)
    """)
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
    exibir_grafico_cotacao('USDBRL=X', 'Bolsa do Dólar')
    st.write(
        """
        Saber o valor do dólar e o quanto o preço dele varia pode ser muito importante, muito além de motivos como viagens programadas. 
        Com a alta do dólar, empresas que exportam seus produtos (como carne, açúcar, grãos e outros produtos) optam estrategicamente 
        em atender o mercado de fora do Brasil, porque rende mais dinheiro. Dessa forma, a oferta de produtos ao mercado daqui é reduzida 
        e, por ter menos para vender, acontece o aumento de preços no supermercado.
        """
    )
    exibir_grafico_cotacao('^BVSP', 'Bolsa de Valores Brasileira')
    st.markdown(
        """
        [Ok, mas o que é a Bolsa de Valores Brasileira/IBOVESPA?](https://g1.globo.com/economia/especial-publicitario/inteligencia-financeira/noticia/2022/06/23/voce-sabe-o-que-e-o-ibovespa-e-sua-importancia-no-mercado-de-capitais.ghtml)
        """
    )
