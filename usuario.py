#login, senha, etc

import streamlit as st
import hashlib
import json
import os

# Funções auxiliares para hashing e manipulação de credenciais
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists("users.json"):
        return {}
    with open("users.json", "r") as file:
        return json.load(file)

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file)

# Carrega os usuários existentes
users = load_users()

# Interface Streamlit
st.title("Sistema de Login e Registro")

# Aba de navegação
menu = st.sidebar.radio("Menu", ["Login", "Registrar"])

if menu == "Registrar":
    st.subheader("Criar uma Nova Conta")
    new_username = st.text_input("Escolha um Nome de Usuário")
    new_password = st.text_input("Escolha uma Senha", type="password")
    confirm_password = st.text_input("Confirme sua Senha", type="password")

    if st.button("Registrar"):
        if new_password != confirm_password:
            st.error("As senhas não coincidem.")
        elif new_username in users:
            st.error("Nome de usuário já existe. Escolha outro.")
        else:
            # Salva o novo usuário
            users[new_username] = hash_password(new_password)
            save_users(users)
            st.success("Conta criada com sucesso! Agora você pode fazer login.")

if menu == "Login":
    st.subheader("Faça Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if username in users and users[username] == hash_password(password):
            st.success(f"Bem-vindo, {username}!")
            st.write("Aqui está o conteúdo restrito.")
        else:
            st.error("Usuário ou senha incorretos.")
