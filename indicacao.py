#api do spotipy + indicação de instagram
### Alinne

import os
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

os.environ['SPOTIPY_CLIENT_ID'] = 'daa2918ffa6f47ca801da8ebf9653878'
os.environ['SPOTIPY_CLIENT_SECRET'] = '90f841a0eb9044058a48780b646d6bbd'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

def buscar_podcasts(tema):
    resultados = sp.search(q=tema, type='show', limit=10)
    return resultados['shows']['items']

st.title("Buscador de Podcasts - Finanças para Mulheres")
st.subheader("Pesquise e explore podcasts relacionados a finanças")

tema = st.text_input("Digite o tema da pesquisa (ex.: finanças para mulheres):")

if st.button("Pesquisar"):
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
            else:
                st.warning(f"Nenhum podcast encontrado para '{tema}'.")
        except Exception as e:
            st.error(f"Erro ao buscar os podcasts: {e}")
    else:
        st.warning("Por favor, insira um tema para pesquisar.")
