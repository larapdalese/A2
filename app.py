import streamlit as st

# Função principal
def main():
    # Título da aplicação
    st.title("Meu Aplicativo")

    # Menu lateral
    menu = st.sidebar.selectbox("Menu", ["Perfil", "Por categoria", "Investimentos", "Configurações e Suporte", "Voltar para a página principal"])

    # Exibir conteúdo baseado na escolha do menu
    if menu == "Perfil":
        show_profile()
    elif menu == "Por categoria":
        show_by_category()
    elif menu == "Investimentos":
        show_investments()
    elif menu == "Configurações e Suporte":
        show_settings_support()
    elif menu == "Voltar para a página principal":
        show_home()

# Funções para cada página
def show_home():
    st.subheader("Página Principal")
    st.write("Bem-vindo à página principal do seu aplicativo!")

def show_profile():
    st.subheader("Perfil")
    st.write("Esta é a seção do Perfil.")

def show_by_category():
    st.subheader("Por Categoria")
    st.write("Esta é a seção de despesas por categoria.")

def show_investments():
    st.subheader("Investimentos")
    st.write("Esta é a seção de Investimentos.")

def show_settings_support():
    st.subheader("Configurações e Suporte")
    st.write("Esta é a seção de Configurações e Suporte.")

# Execução do aplicativo
if __name__ == "__main__":
    main()

streamlit run app.py
