st.set_page_config(layout="centered")
st.image("path/para/sua-imagem-header.jpg", use_column_width=True)
col1, col2 = st.columns([1, 3])
with col1:
    st.image("path/para/sua-foto-perfil.jpg", width=150)
with col2:
    st.markdown("<h1 style='font-size:40px;'>Seu Nome</h1>", unsafe_allow_html=True)
    st.write("Descrição breve ou bio.")
st.write("---")
st.write("Aqui você pode adicionar mais informações, links de redes sociais, ou seções sobre o que você faz.")

