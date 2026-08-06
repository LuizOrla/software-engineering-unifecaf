# Arquivo de armazenamento de projetos, com suas respectivas tarefas

# Importação de classes Projeto e Tarefa, e pacotes pertinentes
from classes import Projeto
from classes import Tarefa
import config
import json
from json import JSONDecodeError
import uuid
import os


# ========== Funções de Arquivos ==========
def ler_arquivos(): # Lê os arquivos e atualiza variáveis de dicionário globais
    try:
        with open(config.ARQUIVO_PROJETO, "r", encoding="utf-8") as arquivo:
            config.dict_projetos = json.load(arquivo)
    except (JSONDecodeError, FileNotFoundError):
        dict = {}
        salvar_projetos_arquivo(dict)
    try:
        with open (config.ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
            config.dict_tarefas = json.load(arquivo)
    except (JSONDecodeError, FileNotFoundError):
        dict = {}
        salvar_tarefas_arquivo(dict)  
def salvar_projetos_arquivo(dict_projeto): # Atualiza o arquivo de projetos a partir do dicionário
    with open(config.ARQUIVO_PROJETO, "w", encoding="utf-8") as arquivo:
        conteudo = json.dumps(dict_projeto, indent=4, ensure_ascii=False)
        arquivo.write(conteudo)
        arquivo.flush()
        os.fsync(arquivo.fileno())
def salvar_tarefas_arquivo(dict_tarefa): # Atualiza o arquivo de tarefas a partir do dicionário
    with open(config.ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        conteudo = json.dumps(dict_tarefa, indent=4, ensure_ascii=False)
        arquivo.write(conteudo)
        arquivo.flush()
        os.fsync(arquivo.fileno())

# ========== Funções de Projetos ==========
def apagar_projeto(id_projeto): # Exclui projeto do dicionário
    del config.dict_projetos[id_projeto]
    for id_tarefa, tarefa in list(config.dict_tarefas.items()):
        if tarefa["projeto"] == id_projeto:
            del config.dict_tarefas[id_tarefa]
    salvar_projetos_arquivo(config.dict_projetos)
    salvar_tarefas_arquivo(config.dict_tarefas)
def criar_projeto(titulo, descricao, id_projeto=""): # Cria um novo projeto e adiciona no dicionário
    if id_projeto == "":
        id_projeto = str(uuid.uuid4())
    projeto = Projeto(id_projeto, titulo, descricao)
    id_projeto, dict_projeto = projeto.dicionario_projeto()
    config.dict_projetos[id_projeto] = dict_projeto
    salvar_projetos_arquivo(config.dict_projetos)
    config.projeto_ativo = id_projeto

# ========== Funções de Tarefas ==========
def criar_tarefa(nome, descricao): # Cria uma nova tarefa e a adiciona no dicionário
    id_tarefa = str(uuid.uuid4()) # Atribui um ID único à tarefa
    tarefa = Tarefa(id_tarefa, config.projeto_ativo, nome, descricao) # Cria um objeto Tarefa com informações fornecidas
    id_tarefa, dict_tarefa = tarefa.dicionario_tarefa() # Cria nova entrada a aprtir de objeto
    config.dict_tarefas[id_tarefa] = dict_tarefa # Adiciona Tarefa a dicionário global
    salvar_tarefas_arquivo(config.dict_tarefas) # Salva arquivo de Tarefas
def avancar_tarefa(id_tarefa): # Altera o status de uma tarefa para trás, baseado em seu status atual
    for id_task, tarefa in config.dict_tarefas.items():
        if id_task == id_tarefa:
            match tarefa["status"]:
                case "todo": tarefa["status"] = "doing"
                case "doing": tarefa["status"] = "done"
    salvar_tarefas_arquivo(config.dict_tarefas)
def retornar_tarefa(id_tarefa): # Altera o status de uma tarefa para trás, baseado em seu status atual
    for id_task, tarefa in config.dict_tarefas.items():
        if id_task == id_tarefa:
            match tarefa["status"]:
                case "doing": tarefa["status"] = "todo"
                case "done": tarefa["status"] = "doing"
    salvar_tarefas_arquivo(config.dict_tarefas)
def apagar_tarefa(id_tarefa): # Exclui uma tarefa do dicionário
    del config.dict_tarefas[id_tarefa]
    salvar_tarefas_arquivo(config.dict_tarefas)
