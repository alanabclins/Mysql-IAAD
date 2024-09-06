import streamlit as st
import subprocess
import os

# Função para exportar o banco de dados
def exportar_banco():
    nome_do_banco = "programacoes_de_filmes"  # Substitua pelo nome do seu banco de dados
    usuario = "root"  # Usuário do MySQL
    senha = ""  # Senha do MySQL (deixe vazio se não houver senha)
    
    # Nome do arquivo de exportação
    arquivo_sql = "backup.sql"
    
    # Comando para exportar o banco de dados usando mysqldump
    comando = f"mysqldump -u {usuario} -p {nome_do_banco} > {arquivo_sql}"
    
    # Executando o comando
    subprocess.run(comando, shell=True)
    
    # Verificando se o arquivo foi criado e oferecendo para download
    if os.path.exists(arquivo_sql):
        with open(arquivo_sql, "rb") as file:
            st.download_button("Download Backup SQL", file, file_name=arquivo_sql)
    else:
        st.error("Erro ao exportar o banco de dados.")

st.title("Exportação de Banco de Dados")

if st.button("Exportar Banco de Dados"):
    exportar_banco()

# Função para importar o banco de dados
def importar_banco(file_path):
    nome_do_banco = "programacoes_de_filmes"  # Substitua pelo nome do seu banco de dados
    usuario = "root"  # Usuário do MySQL
    senha = ""  # Senha do MySQL (deixe vazio se não houver senha)
    
    # Comando para importar o banco de dados usando mysql
    comando = f"mysql -u {usuario} -p {nome_do_banco} < {file_path}"
    
    # Executando o comando
    subprocess.run(comando, shell=True)
    st.success("Banco de dados importado com sucesso!")

st.title("Importação de Banco de Dados")

uploaded_file = st.file_uploader("Faça upload do arquivo SQL", type="sql")

if uploaded_file is not None:
    # Salvando o arquivo enviado
    with open("backup.sql", "wb") as file:
        file.write(uploaded_file.getbuffer())
    
    if st.button("Importar Banco de Dados"):
        importar_banco("backup.sql")