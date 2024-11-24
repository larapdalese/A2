import os
import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

os.environ['SPOTIPY_CLIENT_ID'] = 'daa2918ffa6f47ca801da8ebf9653878'
os.environ['SPOTIPY_CLIENT_SECRET'] = '90f841a0eb9044058a48780b646d6bbd'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

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

def buscar_podcasts(tema):
    resultados = sp.search(q=tema, type='show', limit=10)
    return resultados['shows']['items']

col1, col2 = st.columns(2)

with col1:
    st.title("Notícias")
    st.markdown("Pesquise notícias sobre **Finanças**, **Empreendedorismo** e **Economia**.")

    termo_busca = st.text_input("Digite um termo para refinar a pesquisa (opcional):", key="noticias")
    if st.button("Pesquisar Notícias", key="botao_noticias"):
        noticias = buscar_noticias(termo_busca)

        if noticias['articles']:
            st.success(f"Exibindo as últimas notícias sobre '{termo_busca or 'temas gerais'}'")
            for artigo in noticias['articles']:
                st.subheader(artigo['title'])
                st.markdown(f"Fonte: [{artigo['source']['name']}]({artigo['url']})")
                st.write(artigo['description'])
                st.write("---")
        else:
            st.warning("Nenhuma notícia encontrada para o tema pesquisado.")

with col2:
    st.title("🎙️ Podcasts")
    st.subheader("Pesquise e explore podcasts relacionados a finanças.")

    tema = st.text_input("Digite o tema da pesquisa (ex.: finanças para mulheres):", key="podcasts")
    if st.button("Pesquisar Podcasts", key="botao_podcasts"):
        if tema:
            try:
                podcasts = buscar_podcasts(tema)
                if podcasts:
                    st.success(f"Encontramos {len(podcasts)} podcasts sobre '{tema}'!")
                    for podcast in podcasts:
                        st.write(f"### {podcast['name']}")
                        st.write(podcast['description'])
                        st.write(f"[Ouvir no Spotify]({podcast['external_urls']['spotify']})")
                        st.image(podcast['images'][0]['url'], width=200)
                        st.write("---")
                else:
                    st.warning(f"Nenhum podcast encontrado para '{tema}'.")
            except Exception as e:
                st.error(f"Erro ao buscar os podcasts: {e}")
        else:
            st.warning("Por favor, insira um tema para pesquisar.")
