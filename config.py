# Arquivo de constantes e configurações da aplicação
import os # Importa pacote os, para acessar informações do Sistema Operacional

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # Função que retorna o caminho para este arquivo em format "str"

# Adiciona ao caminho coletado a finalização que aponta para os arquivos projetos.json e tarefas.json
ARQUIVO_PROJETO = os.path.join(BASE_DIR, "data", "projetos.json") 
ARQUIVO_TAREFAS = os.path.join(BASE_DIR, "data", "tarefas.json")

# Dicionários onde são guardadas as informações retiradas dos arquivos
dict_projetos = {}
dict_tarefas = {}

# Variável que guarda o ID do projeto ativo, que está sendo mostrado na tela
projeto_ativo = ""
