import streamlit as st
from mysql.connector import connect, Error

# Função para conectar ao banco
def conectar():
    return connect(
        host="localhost",
        user="root",
        password="",
        database="programacoes_de_filmes"
    )

# Função para inserir canal no banco de dados
def inserir_canal(num_canal, nome, sigla):
    try:
        conn = conectar()
        cursor = conn.cursor()
        query = "INSERT INTO canal (num_canal, nome, sigla) VALUES (%s, %s, %s)"
        cursor.execute(query, (num_canal, nome, sigla))
        conn.commit()
        st.success("Canal inserido com sucesso!")
    except Error as e:
        st.error(f"Erro ao inserir o canal: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Interface do Streamlit para inserir canal
st.title("Inserir Canal")

with st.form("Inserir Canal"):
    num_canal = st.text_input("Número do Canal")
    nome = st.text_input("Nome do Canal")
    sigla = st.text_input("Sigla do Canal (opcional)")
    
    submit = st.form_submit_button("Inserir Canal")
    
    if submit:
        if num_canal and nome:
            inserir_canal(num_canal, nome, sigla)
        else:
            st.error("Por favor, preencha todos os campos obrigatórios.")
