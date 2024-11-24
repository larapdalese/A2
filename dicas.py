import streamlit as st
import requests

def buscar_noticias(termo=None):
    api_key = "d700b8cb09b888dc838bf50109bedd9e" 
    temas_principais = "finanças OR empreendedorismo OR economia"
    query = f"{temas_principais} {termo}" if termo else temas_principais
    
    url = f"https://gnews.io/api/v4/search?q={query}&lang=pt&token={api_key}&max=5"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"articles": []}

st.title("Buscador de Notícias")
st.markdown("Pesquise por notícias relacionadas a **Finanças**, **Empreendedorismo** e **Economia**.")

termo_busca = st.text_input("Digite um termo para refinar a pesquisa (opcional):")

if st.button("Pesquisar"):
    noticias = buscar_noticias(termo_busca)

    if noticias['articles']:
        st.success(f"Exibindo as últimas notícias sobre '{termo_busca or 'temas gerais'}'")
        for artigo in noticias['articles']:
            st.subheader(artigo['title'])
            st.markdown(f"Fonte: [{artigo['source']['name']}]({artigo['url']})")
            st.write(artigo['description'])
            st.write("---")
    else:
        st.warning("Não foram encontradas notícias para a sua pesquisa.")
      
