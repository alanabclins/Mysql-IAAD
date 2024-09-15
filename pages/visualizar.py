import pandas as pd
import streamlit as st
from mysql.connector import connect, Error
from utils.funcoes import get_dados

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

if tabela_escolhida == 'Filme':
    categoria = st.selectbox("Filtrar por categoria",get_dados('filme','categoria'),None, placeholder='Selecione uma categoria')
    dados = get_data_pandas('filme')
    if  not categoria:
        df = st.dataframe(dados,width=700,hide_index=True)
    else:
        dados_filtrado = dados[dados['categoria'] == str(categoria)]
        df = st.dataframe(dados_filtrado,width=700,hide_index=True)

elif tabela_escolhida == 'Canal':
    dados = get_data_pandas('Canal')
    df = st.dataframe(dados,width=700,hide_index=True)

elif tabela_escolhida == 'Exibicao':
    dados = get_data_pandas('Exibicao')
    df = st.dataframe(dados,width=700,hide_index=True)



