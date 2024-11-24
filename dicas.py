import os
import streamlit as st
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

os.environ['SPOTIPY_CLIENT_ID'] = '5dd03bf3704a4a2a903f136a7fd6c593'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'b13072de7dcf4d58ab6104e68fa649c4'

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

def buscar_podcasts():
    temas = "finanças OR feminismo OR empreendedorismo feminino"
    resultados = sp.search(q=temas, type='show', limit=50)
    podcasts_filtrados = [
        podcast for podcast in resultados['shows']['items']
        if any(
            t in podcast['name'].lower() or t in podcast['description'].lower()
            for t in ["finanças", "economia", "empreendedorismo", "feminino"]
        )
    ]

    podcast_nao_te_empodero = {
        "name": "Não Te Empodero",
        "description": "Um projeto de educação para a autonomia feminina em formato de podcast que acredita que o que empodera mulheres é o conhecimento!
O que tem em comum nas histórias vividas por mulheres? @mariacarolmedeiros, professora e pesquisadora, comenta o cotidiano na perspectiva da socialização feminina. Aqui você encontra discussões sobre a estrutura social que permeia a vida das mulheres, de forma embasada e a partir de autoras como Simone de Beauvoir e Michelle Perrot, numa linguagem fácil e sem achismos.
EPISÓDIO NOVO ÀS TERÇAS! Me siga no instagram @mariacarolmedeiros.",
        "external_urls": {"spotify": "https://open.spotify.com/show/21xaGKadO9f43mpihiAzhX"},
        "images": [{"url": "https://i.scdn.co/image/ab6765630000ba8a45d6b51f509769bfeb207bbb"}]
    }
    podcasts_filtrados.insert(0, podcast_nao_te_empodero)

    return podcasts_filtrados[:5]

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
                if 'image' in artigo and artigo['image']:
                    st.image(artigo['image'], caption="Imagem da notícia", use_column_width=True)
                st.write("---")
        else:
            st.warning("Nenhuma notícia encontrada para o tema pesquisado.")

with col2:
    st.title("Podcasts Femininos")
    st.subheader("Descubra 5 podcasts sobre economia, finanças e empreendedorismo feminino.")

    if st.button("Carregar Podcasts", key="botao_podcasts"):
        try:
            podcasts = buscar_podcasts()
            if podcasts:
                for podcast in podcasts:
                    st.write(f"### {podcast['name']}")
                    st.write(podcast['description'])
                    st.write(f"[Ouvir no Spotify]({podcast['external_urls']['spotify']})")
                    if 'images' in podcast and podcast['images']:
                        st.image(podcast['images'][0]['url'], width=200)
                    else:
                        st.warning("Imagem não disponível.")
                    st.write("---")
            else:
                st.warning("Nenhum podcast encontrado para os temas selecionados.")
        except Exception as e:
            st.error(f"Erro ao buscar os podcasts: {e}")
