import pandas as pd
import streamlit as st
from mysql.connector import connect, Error

def conectar():
    return connect(
        host="localhost",
        user="root",
        password="",
        database="programacoes_de_filmes"
    )

def get_data_pandas(table):
    conexao = conectar()
    df = pd.read_sql(f"select * from {table}",conexao, parse_dates={'ano_lancamento':'%Y'})
    return df

st.subheader("Visualização de tabelas")

tabela_escolhida = st.selectbox("Escolha a tabela que deseja visualizar",("Filme", "Canal", "Exibicao"))

df = st.dataframe(get_data_pandas(str(tabela_escolhida)),hide_index=True)