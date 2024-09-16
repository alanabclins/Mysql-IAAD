import pandas as pd
import streamlit as st
from mysql.connector import connect, Error

# Função para conectar ao banco de dados
def conectar():
    return connect(
        host="localhost",
        user="root",
        password="",
        database="programacoes_de_filmes"
    )

# Função para obter o resultado da consulta
def get_filmes_canais():
    query = """
        SELECT 
            c.nome AS "Canal",
            COUNT(f.num_filme) AS "Total de Filmes Exibidos",
            AVG(f.duracao) AS "Duração Média (minutos)",
            MAX(f.duracao) AS "Duração Máxima (minutos)",
            MIN(f.duracao) AS "Duração Mínima (minutos)"
        FROM 
            exibicao e
        JOIN 
            filme f ON e.num_filme = f.num_filme
        JOIN 
            canal c ON e.num_canal = c.num_canal
        WHERE 
            f.duracao > 60 
            AND e.data_exibicao BETWEEN '2024-07-01' AND '2024-10-31'
        GROUP BY 
            c.nome
        HAVING 
            COUNT(f.num_filme) > 1
        ORDER BY 
            AVG(f.duracao) DESC;
    """
    try:
        conexao = conectar()
        df = pd.read_sql(query, conexao)
        return df
    except Error as e:
        st.error(f"Erro ao conectar ao banco de dados: {e}")
    finally:
        if conexao.is_connected():
            conexao.close()

# Configuração da nova página do Streamlit
st.title("Consulta de Programação de Filmes por Canal")
st.write("Esta consulta tem como objetivo analisar os filmes exibidos nos canais e suas durações médias. Estamos interessados em filmes com mais de 60 minutos de duração e exibidos entre julho e outubro de 2024.")

# Botão para carregar os dados
if st.button("Carregar Dados"):
    df = get_filmes_canais()

    if df is not None and not df.empty:
        # Exibir a tabela com os resultados
        st.dataframe(df)
    else:
        st.write("Nenhum resultado encontrado.")

# Opcional: Adicionar filtros de exibição
