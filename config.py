# Arquivo de constantes e configurações da aplicação
import os # Importa pacote os, para acessar informações do Sistema Operacional

# Função que retorna o caminho para este arquivo em format "str"
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 

# Adiciona ao caminho coletado a finalização que aponta para os arquivo tarefas.json
ARQUIVO_TAREFAS = os.path.join(BASE_DIR, "data", "tarefas.json") 

# Dicionários onde são guardadas as informações retiradas dos arquivos
dict_tarefas = {}
