import streamlit as st
from mysql.connector import connect, Error


def conectar():
    return connect(
        host="localhost",
        user="root",
        password="",
        database="programacoes_de_filmes"
    )

def get_dados(tabela:str, coluna:str): # funcao para pegar dados em uma coluna x de uma tabela y.
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT {coluna} FROM {tabela};")
        dados = [id[0] for id in cursor.fetchall()]
    except Error as e:
        st.error(f"{e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return dados
         
def get_nome_filme(): # funcao que devolve lista de nomes de filmes ja existentes.
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT titulo_original FROM filme;")
        nome_filmes = [id[0] for id in cursor.fetchall()]
    except Error as e:
        st.error(f"{e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return nome_filmes

def get_nome_canal(): # funcao que devolve lista de nomes de canais ja existentes.
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT nome FROM canal;")
        nome_canais = [id[0] for id in cursor.fetchall()]
    except Error as e:
        st.error(f"{e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return nome_canais

def get_id_filme(filme:str): #funcao que retorna id de um filme x.
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT num_filme FROM filme WHERE titulo_original = '{filme}';")
        num_filme = cursor.fetchone()
    except Error as e:
        st.error(f"{e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return num_filme[0]

def get_id_canal(canal:str): #funcao que retorna id de um canal x.
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT num_canal FROM canal WHERE nome = '{canal}';")
        num_canal = cursor.fetchone()
    except Error as e:
        st.error(f"{e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return num_canal[0]