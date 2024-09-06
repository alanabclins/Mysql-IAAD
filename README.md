# Mysql-IAAD

## Comandos iniciais
- python -m venv venv
- ative a venv antes dos próximos passos, o método depende do tipo de terminal;
- python -m pip install --upgrade pip
- pip install -r "requirements.txt" --upgrade

## Configuração banco de dados
nome_do_banco = "programacoes_de_filmes"
usuario = "root" 
senha = [sem senha]

## Interações com o banco
Execute o streamlit (streamlit run app.py);
Para puxar as atualizações no banco de dados importe o arquivo "backup.sql" do repositório;
Realize as modificações normalmente através do workbench;
Para salvar suas alterações para todos, pressione o botão exportar no streamlit;
Ao realizar as ações de importar e exportar a senha será solicitada no terminal, basta pressionar enter