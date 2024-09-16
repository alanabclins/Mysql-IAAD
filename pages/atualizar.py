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
        query = f"UPDATE {tabela} SET {set_clause} WHERE {where_clause};"

        cursor.execute(query, tuple(campos_valores.values()) + tuple(pk_valores.values()))
        conexao.commit()
        st.success(f"{cursor.rowcount} registro(s) atualizado(s) com sucesso.")
    except Error as e:
        st.error(f"Erro ao atualizar o registro: {e}")
    finally:
        if conexao.is_connected():
            cursor.close()



st.subheader("Atualizar tabelas")

tabela_escolhida = st.selectbox('Escolha a tabela que deseja atualizar', ['Filme', 'Canal', 'Exibicao'])

with st.form("Update"):
    st.write(f"Atualizar na tabela {tabela_escolhida}")

    if tabela_escolhida == 'Filme':
        nome_filme = st.selectbox('Nome do filme ',get_nome_filme(), None, placeholder='Escolha um filme já inserido.')
        if nome_filme:
            num_filme = get_id_filme(nome_filme)
        novo_num_filme = duracao = st.number_input('Novo ID', value=None)
        titulo_original = st.text_input('Novo título original')
        titulo_brasil = st.text_input('Novo título brasileiro')
        ano_lancamento = st.text_input('Novo ano')
        pais_origem = st.text_input('Novo país de origem')
        categoria = st.text_input('Nova categoria')
        duracao = st.number_input('Nova duração do filme', value=None)
        submit_update = st.form_submit_button('Atualizar')

        if submit_update:
            campos_valores = {}
            if novo_num_filme:
                campos_valores['num_filme'] = novo_num_filme
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
        nome_canal = st.selectbox('Nome do canal ',get_nome_canal(), None, placeholder='Escolha um canal já inserido.')
        if nome_canal:
            num_canal = get_id_canal(nome_canal)
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
        nome_filme_exibicao = st.selectbox('Nome do filme ',get_nome_filme(), None, placeholder='Escolha um filme já inserido.')
        if nome_filme_exibicao:
            num_filme_exibicao = get_id_filme(nome_filme_exibicao)
        nome_canal_exibicao = st.selectbox('Nome do canal ',get_nome_canal(), None, placeholder='Escolha um canal já inserido.')
        if nome_canal_exibicao:
            num_canal_exibicao = get_id_canal(nome_canal_exibicao)
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