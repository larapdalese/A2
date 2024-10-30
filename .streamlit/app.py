import streamlit as st

# Definindo a URL das imagens
profile_image_url = "https://i.pinimg.com/564x/86/8d/ab/868dab99f9d90a367c320a170ab9eab3.jpg"
header_image_url = "https://i.pinimg.com/564x/3f/a6/9f/3fa69f6c8b6f7dbf8fccd3ac7ee5b2b3.jpg"

# Configuração da página
st.set_page_config(page_title="Perfil", layout="wide")

# Criando a seção do cabeçalho
st.markdown(
    f"""
    <div style="position: relative; text-align: center;">
        <img src="{header_image_url}" alt="Header" style="width: 100%; height: auto; border-radius: 8px;">
        <img src="{profile_image_url}" alt="Profile Image" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100px; height: 100px; border-radius: 50%; border: 3px solid white;">
    </div>
    """,
    unsafe_allow_html=True
)

# Adicionando informações do usuário
st.write("### Nome do Usuário")
st.write("@usuario_exemplo")

st.write("## Bio")
st.write("Aqui você pode adicionar uma breve descrição sobre você.")

st.write("### Outras informações")
st.write("- Localização: Cidade, País")
st.write("- Website: [www.seusite.com](http://www.seusite.com)")
