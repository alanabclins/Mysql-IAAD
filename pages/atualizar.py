import streamlit as st
from mysql.connector import connect, Error

def conectar():
    return connect(
        host="localhost",
        user="root",
        password="",
        database="programacoes_de_filmes"
    )

def update(tabela, campos_valores, condicao, primary_key):
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        set_clause = ', '.join([f"{coluna} = %s" for coluna in campos_valores.keys()])
        query = f"UPDATE {tabela} SET {set_clause} WHERE {primary_key} = {condicao};"
        cursor.execute(query, tuple(campos_valores.values()))
        conexao.commit()
        st.success(f"{cursor.rowcount} registro(s) atualizado(s) com sucesso.")
    except Error as e:
        st.error(f"Erro ao atualizar o registro: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()

def update_exibicao(tabela, campos_valores, pk_valores):
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        set_clause = ', '.join([f"{coluna} = %s" for coluna in campos_valores.keys()])
        where_clause = ' AND '.join([f"{coluna} = %s" for coluna in pk_valores.keys()])
        print(where_clause)
        query = f"UPDATE {tabela} SET {set_clause} WHERE {where_clause};"

        cursor.execute(query, tuple(campos_valores.values()) + tuple(pk_valores.values()))
        conexao.commit()
        st.success(f"{cursor.rowcount} registro(s) atualizado(s) com sucesso.")
    except Error as e:
        st.error(f"Erro ao atualizar o registro: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()

def filmes_disponiveis(): # funcao que devolve lista de id de filmes ja existentes para o dropbox.
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT num_filme FROM filme;")
        id_filmes = [id[0] for id in cursor.fetchall()]
    except Error as e:
        st.error(f"{e}")
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
    return id_filmes

def canais_disponiveis(): # funcao que devolve lista de id de canais ja existentes para o dropbox.
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        cursor.execute(f"SELECT num_canal FROM canal;")
        id_canais = [id[0] for id in cursor.fetchall()]
    except Error as e:
        st.error(f"{e}")
    finally:
        if conexao.is_connected():

            cursor.close()
            conexao.close()
    return id_canais



st.subheader("Atualizar tabelas")

tabela_escolhida = st.selectbox('Escolha a tabela que deseja atualizar', ['Filme', 'Canal', 'Exibicao'])

with st.form("update"):
    st.write(f"Atualizar na tabela {tabela_escolhida}")

    if tabela_escolhida == 'Filme':
        num_filme = st.selectbox('Numero ID filme ',filmes_disponiveis(), None, placeholder='Escolha um ID de um filme ja inserido.')
        titulo_original = st.text_input('Novo titulo original')
        titulo_brasil = st.text_input('Novo titulo brasileiro')
        ano_lancamento = st.text_input('Novo ano')
        pais_origem = st.text_input('Novo pais de origem')
        categoria = st.text_input('Nova categoria')
        duracao = st.number_input('Nova duração do filme', value=None)
        submit_update = st.form_submit_button('Atualizar')

        if submit_update:
            campos_valores = {}
            if titulo_original:
                campos_valores['titulo_original'] = titulo_original
            if titulo_brasil:
                campos_valores['titulo_brasil'] = titulo_brasil
            if ano_lancamento:
                campos_valores['ano_lancamento'] = ano_lancamento
            if pais_origem:
                campos_valores['pais_origem'] = pais_origem
            if categoria:
                campos_valores['categoria'] = categoria
            if duracao:
                campos_valores['duracao'] = duracao
            update(tabela_escolhida, campos_valores, num_filme,'num_filme')

    elif tabela_escolhida == 'Canal':
        num_canal = st.selectbox('Numero ID canal ',canais_disponiveis(), None, placeholder='Escolha um ID de um canal ja inserido.')
        num_canal_novo = st.text_input('Novo numero ID do canal')
        nome = st.text_input('Novo nome do canal')
        sigla = st.text_input('Nova sigla')
        submit_update = st.form_submit_button('Atualizar')

        if submit_update:
            campos_valores = {}
            if num_canal_novo:
                campos_valores['num_canal'] = num_canal_novo
            if nome:
                campos_valores['nome'] = nome
            if sigla:
                campos_valores['sigla'] = sigla

            update(tabela_escolhida, campos_valores, num_canal, 'num_canal')

    elif tabela_escolhida == 'Exibicao':
        num_filme_exibicao = st.selectbox('Numero ID filme ',filmes_disponiveis(), None, placeholder='Escolha um ID de um filme ja inserido.')
        num_canal_exibicao = st.selectbox('Numero ID canal ',canais_disponiveis(), None, placeholder='Escolha um ID de um canal ja inserido.')
        data = st.text_input('Data de exibição atual')
        nova_data = st.text_input('Nova data de exibição')
        submit_update = st.form_submit_button('Atualizar')

        if submit_update:
            campos_valores = {}
            pk_valores = {}
            if num_filme_exibicao:
                pk_valores['num_filme'] = num_filme_exibicao
            if num_canal_exibicao:
                pk_valores['num_canal'] = num_canal_exibicao
            if data:
                pk_valores['data_exibicao'] = data
            if nova_data:
                campos_valores['data_exibicao'] = nova_data
            update_exibicao(tabela_escolhida, campos_valores, pk_valores)