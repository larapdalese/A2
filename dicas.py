import streamlit as st
import requests
import math

# Função para buscar notícias da API do GNEWS
def buscar_noticias(palavra_chave, pagina=1):
    api_key = "d700b8cb09b888dc838bf50109bedd9e"
    if not palavra_chave:
        palavra_chave = "finanças OR educação financeira OR empreendedorismo"
    url = f"https://gnews.io/api/v4/search?q={palavra_chave}&lang=pt&token={api_key}&max=10&page={pagina}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"articles": []}

# Interface com Streamlit
st.title("Notícias sobre Educação Financeira, Finanças e Empreendedorismo")
st.markdown("Encontre as últimas notícias e atualizações sobre educação financeira, finanças e empreendedorismo.")

# Input de palavra-chave
palavra_chave = st.text_input("Digite a palavra-chave para buscar notícias:")

if "pagina" not in st.session_state:
    st.session_state.pagina = 1

if st.button('Buscar Notícias') or palavra_chave:
    st.session_state.pagina = 1
    noticias = buscar_noticias(palavra_chave, st.session_state.pagina)

    if noticias['articles']:
        for artigo in noticias['articles']:
            st.subheader(artigo['title'])
            st.markdown(f"[{artigo['source']['name']}]({artigo['url']})")
            st.write(artigo['description'])
            st.write("---")

      
