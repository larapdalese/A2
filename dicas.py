import streamlit as st
import requests

# Função para buscar notícias sobre educação financeira usando a GNews API
def buscar_noticias_gnews(api_key, termos_busca, pagina=1):
    try:
        # Definindo a URL da API e os parâmetros
        api_url = f"https://gnews.io/api/v4/search?q={termos_busca}&lang=pt&token={api_key}&country=br&page={pagina}"
        
        # Fazendo a requisição GET à GNews API
        response = requests.get(api_url)
        response.raise_for_status()       # Levanta exceção se ocorrer um erro

        # Convertendo a resposta para JSON
        dados = response.json()
        return dados['articles']
    except Exception as e:
        st.error(f"Erro ao buscar notícias: {e}")
        return []

# Função para mostrar as notícias na aba "Dicas"
def mostrar_dicas():
    st.title("Dicas de Educação Financeira para Mulheres")
    st.write("Explore notícias simples e práticas que ajudam mulheres a entender melhor o mundo das finanças pessoais!")


 api_key = "d700b8cb09b888dc838bf50109bedd9e"  
    termos_busca = "educação financeira OR finanças OR mulheres OR empreendedorismo"

    # Controle de paginação
    pagina = st.number_input("Página", min_value=1, step=1, value=1)

    # Buscar notícias usando a API
    noticias = buscar_noticias_gnews(api_key, termos_busca, pagina)

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

