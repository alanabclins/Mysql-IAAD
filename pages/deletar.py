import streamlit as st
from mysql.connector import connect, Error

def conectar():
    return connect(
        host="localhost",
        user="root",
        password="",
        database="programacoes_de_filmes"
    )
def filmes_disponiveis(): # funcao que devolve lista de id de filmes ja existentes.
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

def canais_disponiveis():
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
        num_filme = st.selectbox('Numero ID filme ',filmes_disponiveis(), None, placeholder='Escolha um ID de um filme ja inserido.')
        submit_delete = st.form_submit_button('Deletar')
        if submit_delete:
            
            delete(tabela_escolhida, id_value=num_filme, id_column='num_filme')


    elif tabela_escolhida == 'Canal':
        num_canal = st.selectbox('Numero ID canal ',canais_disponiveis(), None, placeholder='Escolha um ID de um canal ja inserido.')
        submit_delete = st.form_submit_button('Deletar')
        if submit_delete:
            
            delete(tabela_escolhida, id_value = num_canal, id_column='num_canal')


    elif tabela_escolhida == 'Exibicao':
        num_filme_exibicao = st.selectbox('Numero ID filme ',filmes_disponiveis(), None, placeholder='Escolha um ID de um filme ja inserido.')
        num_canal_exibicao = st.selectbox('Numero ID canal ',canais_disponiveis(), None, placeholder='Escolha um ID de um canal ja inserido.')
        data_exibicao = st.text_input('Data de exibição do filme a deletar')
        submit_delete = st.form_submit_button('Deletar')

        if submit_delete:
            pk_valores = {
                'num_filme': num_filme_exibicao,
                'num_canal': num_canal_exibicao,
                'data_exibicao': data_exibicao
            }

            delete(tabela_escolhida, pk_valores=pk_valores )
