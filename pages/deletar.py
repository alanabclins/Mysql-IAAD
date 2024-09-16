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


def delete( table: str, pk_valores=None, id_value=None, id_column=None):
    conexao = conectar()
    try:
        cursor = conexao.cursor()
        if table == 'Exibicao':
            where_clause = ' AND '.join([f"{coluna} = %s" for coluna in pk_valores.keys()])
            print(where_clause)
            query = f"DELETE FROM {table} WHERE {where_clause};"
            cursor.execute(query, tuple(pk_valores.values()))
        else:
            
            query = f"DELETE FROM {table} WHERE {id_column} = %s"
            print(query)
            cursor.execute(query, (id_value,))
        st.success(f"Registro deletado com sucesso.")
    except Error as e:
        st.error(f"Erro ao atualizar o registro: {e}")
    finally:
        conexao.commit()
        cursor.close()
        conexao.close()

st.subheader("Deletar dados")

tabela_escolhida = st.selectbox('Escolha a tabela que deseja deletar', ['Filme', 'Canal', 'Exibicao'])

# Formulário para deletar um registro
with st.form("delete"):
    st.write(f"Deletar um registro na tabela {tabela_escolhida}")
    
    if tabela_escolhida == 'Filme':
        nome_filme = st.selectbox('Nome do filme ',get_nome_filme(), None, placeholder='Escolha um filme já inserido.')
        if nome_filme:
            num_filme = get_id_filme(nome_filme)
        submit_delete = st.form_submit_button('Deletar')
        if submit_delete:
            
            delete(tabela_escolhida, id_value=num_filme, id_column='num_filme')


    elif tabela_escolhida == 'Canal':
        nome_canal = st.selectbox('Nome do canal ',get_nome_canal(), None, placeholder='Escolha canal já inserido.')
        if nome_canal:
            num_canal = get_id_canal(nome_canal)
        submit_delete = st.form_submit_button('Deletar')
        if submit_delete:
            
            delete(tabela_escolhida, id_value = num_canal, id_column='num_canal')


    elif tabela_escolhida == 'Exibicao':
        nome_filme_exibicao = st.selectbox('Nome do filme ',get_nome_filme(), None, placeholder='Escolha um filme já inserido.')
        if nome_filme_exibicao:
            num_filme_exibicao = get_id_filme(nome_filme_exibicao)
        nome_canal_exibicao = st.selectbox('Nome do canal ',get_nome_canal(), None, placeholder='Escolha um canal já inserido.')
        if nome_canal_exibicao:
            num_canal_exibicao = get_id_canal(nome_canal_exibicao)
        data_exibicao = st.text_input('Data de exibição do filme a deletar')
        submit_delete = st.form_submit_button('Deletar')

        if submit_delete:
            pk_valores = {
                'num_filme': num_filme_exibicao,
                'num_canal': num_canal_exibicao,
                'data_exibicao': data_exibicao
            }

            delete(tabela_escolhida, pk_valores=pk_valores )
