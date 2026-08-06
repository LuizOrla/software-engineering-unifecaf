import pytest
import os
import json
import config
import storage

# Configuração para redirecionar os arquivos para uma pasta temporária em cada teste
@pytest.fixture(autouse=True)
def configurar_arquivos_temporarios(tmp_path):
    # Cria caminhos temporários isolados para os testes
    arquivo_proj_temp = tmp_path / "projetos_teste.json"
    arquivo_tarefas_temp = tmp_path / "tarefas_teste.json"
    
    # Substitui as variáveis do config para usar os arquivos temporários
    config.ARQUIVO_PROJETO = str(arquivo_proj_temp)
    config.ARQUIVO_TAREFAS = str(arquivo_tarefas_temp)
    
    # Reseta os dicionários globais antes de cada teste
    config.dict_projetos = {}
    config.dict_tarefas = {}
    config.projeto_ativo = ""
    
    yield

def test_ler_arquivos_inexistentes_cria_arquivos_vazios():
    # Executa a leitura quando os arquivos ainda não existem
    storage.ler_arquivos()
    
    # Verifica se os arquivos físicos foram criados no disco
    assert os.path.exists(config.ARQUIVO_PROJETO)
    assert os.path.exists(config.ARQUIVO_TAREFAS)
    
    # Garante que foram criados com dicionários vazios
    with open(config.ARQUIVO_PROJETO, "r", encoding="utf-8") as f:
        assert json.load(f) == {}

def test_criar_e_apagar_projeto():
    # Cria um projeto
    storage.criar_projeto("Projeto Alfa", "Descrição do Alfa", id_projeto="123")
    
    # Verifica se salvou no dicionário global e ativou o projeto
    assert "123" in config.dict_projetos
    assert config.projeto_ativo == "123"
    
    # Verifica se persistiu no arquivo JSON
    with open(config.ARQUIVO_PROJETO, "r", encoding="utf-8") as f:
        dados_salvos = json.load(f)
        assert dados_salvos["123"]["titulo"] == "Projeto Alfa"

    # Cria uma tarefa atrelada a este projeto
    storage.criar_tarefa("Tarefa 1", "Fazer o deploy")
    id_tarefa_criada = list(config.dict_tarefas.keys())[0]
    
    # Apaga o projeto e garante que a tarefa vinculada também sumiu (cascata)
    storage.apagar_projeto("123")
    
    assert "123" not in config.dict_projetos
    assert id_tarefa_criada not in config.dict_tarefas

def test_avancar_e_retornar_status_tarefa():
    # Configura cenário: projeto ativo e dicionário com uma tarefa mockada
    config.projeto_ativo = "999"
    id_fake = "task-001"
    config.dict_tarefas[id_fake] = {
        "projeto": "999",
        "nome": "Testar CI",
        "descricao": "Rodar GitHub Actions",
        "status": "todo"
    }
    # Salva o estado inicial
    storage.salvar_tarefas_arquivo(config.dict_tarefas)
    
    # Avança para 'doing'
    storage.avancar_tarefa(id_fake)
    assert config.dict_tarefas[id_fake]["status"] == "doing"
    
    # Avança para 'done'
    storage.avancar_tarefa(id_fake)
    assert config.dict_tarefas[id_fake]["status"] == "done"
    
    # Retorna para 'doing'
    storage.retornar_tarefa(id_fake)
    assert config.dict_tarefas[id_fake]["status"] == "doing"
