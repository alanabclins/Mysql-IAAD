import streamlit as st
from mysql.connector import connect, Error

def conectar_db():
    return connect(
        host="localhost",
        user="root",
        password="",
        database="programacoes_de_filmes"
    )

# Função para deletar um registro
def delete( table: str, pk_valores: dict, id_column=None, id_value=None):
    conexao = conectar_db()
    cursor = conexao.cursor()
    if table == 'Exibicao':
        where_clause = ' AND '.join([f"{coluna} = %s" for coluna in pk_valores.keys()])
        print(where_clause)
        query = f"DELETE FROM {table} WHERE {where_clause};"
        cursor.execute(query, tuple(pk_valores.values()))
    else:
        query = f"DELETE FROM {table} WHERE {id_column} = %s"
        cursor.execute(query, (id_value,))
    conexao.commit()
    cursor.close()
    conexao.close()

st.subheader("Deletar dados")

tabela_escolhida = st.selectbox('Escolha a tabela que deseja deletar', ['Filme', 'Canal', 'Exibicao'])

# Formulário para deletar um registro
with st.form("delete"):
    st.write(f"Deletar um registro na tabela {tabela_escolhida}")
    
    if tabela_escolhida == 'Filme':
        num_filme = st.number_input('Numero único do filme a deletar')
        submit_delete = st.form_submit_button('Deletar')
        if submit_delete:
            conexao = conectar_db()
            delete(tabela_escolhida, 'num_filme', num_filme)
            st.success('Registro deletado com sucesso!')

    elif tabela_escolhida == 'Canal':
        num_canal = st.number_input('Número único do canal a deletar')
        submit_delete = st.form_submit_button('Deletar')
        if submit_delete:
            conexao = conectar_db()
            delete(tabela_escolhida, 'num_canal', num_canal)
            st.success('Registro deletado com sucesso!')

    elif tabela_escolhida == 'Exibicao':
        num_filme = st.number_input('Número do filme na exibição a deletar')
        num_canal = st.number_input('Número do canal na exibição a deletar')
        data_exibicao = st.text_input('Data de exibição do filme')
        submit_delete = st.form_submit_button('Deletar')

        if submit_delete:
            pk_valores = {
                'num_filme': num_filme,
                'num_canal': num_canal,
                'data_exibicao': data_exibicao
            }

            delete(tabela_escolhida, pk_valores )
            st.success('Registro deletado com sucesso!')