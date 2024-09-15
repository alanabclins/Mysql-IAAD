import streamlit as st
from mysql.connector import connect, Error
from utils.funcoes import get_nome_filme, get_nome_canal, get_id_filme, get_id_canal

def conectar():
    return connect(
        host="localhost",
        user="root",
        password="",
        database="programacoes_de_filmes"
    )

def insert(table: str, valores: tuple):
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        columns = cursor.column_names
        cursor.execute(f"INSERT INTO {table} {columns} VALUES {valores}")
        conexao.commit()
        st.success(f"Dados inseridos com sucesso.")
    except Error as e:
        st.error(f"Erro ao inserir o canal: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            
st.subheader("Inserir dados")

tabela_escolhida = st.selectbox("Escolha a tabela na qual deseja inserir",("Filme", "Canal", "Exibicao"))

with st.form("Insert"):
    st.write(f"Insira dados na tabela {tabela_escolhida}")

    if tabela_escolhida=='Filme':
        num_filme = st.number_input('Numero ID do filme', value=None)
        titulo_original = st.text_input('Título original')
        titulo_br = st.text_input('Título brasileiro')
        ano = st.text_input('Ano')
        pais_origem = st.text_input('País de origem')
        categoria = st.text_input('Categoria')
        duracao = st.number_input('Duração do filme', value=None)
        submit = st.form_submit_button('Inserir dados')
        if submit:
            valores = (num_filme,titulo_original,titulo_br,ano,pais_origem,categoria,duracao)
            insert(tabela_escolhida,valores)

    elif tabela_escolhida == 'Canal':
        num_canal = st.number_input('Numero ID do canal', value=None)
        nome_canal = st.text_input('Nome do canal')
        sigla_canal = st.text_input('Sigla do canal')
        submit_canal = st.form_submit_button('Inserir dados')
        if submit_canal:
            valores = (num_canal,nome_canal,sigla_canal)
            insert(tabela_escolhida,valores)

    elif tabela_escolhida == 'Exibicao':
        nome_filmes = st.selectbox('Nome do filme ',get_nome_filme(), None, placeholder='Escolha um filme já inserido.')
        if nome_filmes:
            num_filme_exibicao = get_id_filme(nome_filmes)
        nome_canal_exibicao = st.selectbox('Numero ID canal', get_nome_canal(), None, placeholder='Escolha o ID de um canal já inserido.')
        if nome_canal_exibicao:
            num_canal_exibicao = get_id_canal(nome_canal_exibicao)
        data_exibicao = st.text_input('Data e horário de exibição', placeholder='yyyy-mm-dd hh:mm:ss')
        submit_exibicao = st.form_submit_button('Inserir dados')
        if submit_exibicao:
            valores = (num_filme_exibicao,num_canal_exibicao,data_exibicao)
            insert(tabela_escolhida,valores)