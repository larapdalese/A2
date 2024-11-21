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

    # Parâmetros da API (substitua pelo valor real)
    api_key = "d700b8cb09b888dc838bf50109bedd9e"  # Substitua pela sua chave API válida
    termos_busca = st.text_area("Busque por palavras-chave para encontrar resultados ainda melhores, diva:", "", height=100)

    # Buscar notícias usando a API
        noticias = buscar_noticias_gnews(api_key, termos_busca, pagina)

    # Se não houver notícias encontradas
    if not noticias:
        st.write("Nenhuma notícia encontrada. Tente novamente mais tarde.")
        return

    # Mostrar as notícias encontradas (4 por página)
    noticias_por_pagina = 4
    inicio = (pagina - 1) * noticias_por_pagina
    fim = inicio + noticias_por_pagina
    noticias_pagina = noticias[inicio:fim]

    for noticia in noticias_pagina:
        st.subheader(noticia['title'])
        st.write(noticia['description'])
        st.write(f"[Leia mais]({noticia['url']})")
        st.markdown("---")

    # Rodapé com controle de páginas
    st.markdown("---")
    total_paginas = len(noticias) // noticias_por_pagina + (1 if len(noticias) % noticias_por_pagina > 0 else 0)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write(f"Página {pagina} de {total_paginas}")
        if pagina < total_paginas:
            if st.button("Próxima Página"):
                st.experimental_rerun()
        if pagina > 1:
            if st.button("Página Anterior"):
                st.experimental_rerun()

# Rodar a função de dicas se for o arquivo principal
if __name__ == "__main__":
    mostrar_dicas()
