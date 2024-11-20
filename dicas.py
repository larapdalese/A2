import streamlit as st
import requests

# Função para buscar notícias sobre investimentos usando a NewsAPI
def buscar_noticias_educacaofinanceira(api_url, api_key, termos_busca):
    try:
   
        params = {
            'q': termos_busca,            # Termos de busca (notícias relacionadas a finanças simples)
            'apiKey': api_key,            # Chave da API (obtida ao se registrar na NewsAPI)
            'language': 'pt',             # Notícias em português
            'sortBy': 'relevance'         # Ordenação por relevância
        }

        # Fazendo a requisição GET à NewsAPI
        response = requests.get(api_url, params=params)
        response.raise_for_status()       # Levanta exceção se ocorrer um erro

        # Convertendo a resposta para JSON
        dados = response.json()
        return dados['articles']
    except Exception as e:
        st.error(f"Erro ao buscar notícias: {e}")
        return []

# Função para mostrar as notícias na aba "Dicas"
def mostrar_dicas():
    st.title("Dicas de Investimentos para Iniciantes")
    st.write("Confira notícias simples e fáceis de entender para começar sua jornada no mundo das finanças!")

    # Parâmetros da API (substitua pelo valor real)
    api_url = "https://newsapi.org/v2/everything"
    api_key = "4f55225bc66b48659ecd186d41db2db5"  
    termos_busca = "investimentos OR educação financeira para iniciantes OR conceitos básicos de economia"

    # Buscar notícias usando a API
    noticias = buscar_noticias_investimentos(api_url, api_key, termos_busca)

    # Se não houver notícias encontradas
    if not noticias:
        st.write("Nenhuma notícia encontrada. Tente novamente mais tarde.")
        return

    # Mostrar as notícias encontradas
    for noticia in noticias:
        st.subheader(noticia['title'])
        st.write(noticia['description'])
        st.write(f"[Leia mais]({noticia['url']})")
        st.markdown("---")

# Rodar a função de dicas se for o arquivo principal
if __name__ == "__main__":
    mostrar_dicas()

