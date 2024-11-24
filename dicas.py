import streamlit as st
import requests

def buscar_noticias(termo=None):
    api_key = "d700b8cb09b888dc838bf50109bedd9e"  # Substitua pela sua API Key do GNews
    temas_principais = "finanças OR empreendedorismo OR economia"
    query = f"{temas_principais} {termo}" if termo else temas_principais
    url = f"https://gnews.io/api/v4/search?q={query}&lang=pt&token={api_key}&max=5"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"articles": []}

# Lista fixa de podcasts
def obter_podcasts_femininos():
    return [
        {
            "name": "Não Te Empodero",
            "description": "Discussões profundas sobre o que realmente significa empoderar mulheres no mundo das finanças e negócios.",
            "url": "https://open.spotify.com/show/nao-te-empodero",
            "image": "https://via.placeholder.com/200?text=Nao+Te+Empodero"
        },
        {
            "name": "Ela Investe",
            "description": "Educação financeira para mulheres que desejam dominar o mercado de investimentos.",
            "url": "https://open.spotify.com/show/ela-investe",
            "image": "https://via.placeholder.com/200?text=Ela+Investe"
        },
        {
            "name": "Mulheres que Empreendem",
            "description": "Histórias inspiradoras e práticas para mulheres no mundo do empreendedorismo.",
            "url": "https://open.spotify.com/show/mulheres-que-empreendem",
            "image": "https://via.placeholder.com/200?text=Mulheres+que+Empreendem"
        },
        {
            "name": "Finanças Sem Medo",
            "description": "Desmistificando o universo financeiro para mulheres de todas as idades.",
            "url": "https://open.spotify.com/show/financas-sem-medo",
            "image": "https://via.placeholder.com/200?text=Financas+Sem+Medo"
        },
        {
            "name": "Empreenda Mulher",
            "description": "Dicas, estratégias e conversas sobre o papel da mulher no mundo dos negócios.",
            "url": "https://open.spotify.com/show/empreenda-mulher",
            "image": "https://via.placeholder.com/200?text=Empreenda+Mulher"
        },
    ]

# Interface Streamlit
col1, col2 = st.columns(2)

with col1:
    st.title("📰 Notícias")
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
    st.title("🎙️ Podcasts Femininos")
    st.subheader("Descubra 5 podcasts sobre economia, finanças e empreendedorismo feminino.")

    podcasts = obter_podcasts_femininos()
    for podcast in podcasts:
        st.write(f"### {podcast['name']}")
        st.write(podcast['description'])
        st.write(f"[Ouvir no Spotify]({podcast['url']})")
        st.image(podcast['image'], width=200)
        st.write("---")
