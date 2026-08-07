import pytest
from nicegui import ui
from nicegui.testing import User
import gui  # Importa o seu arquivo de interface
import config

# Configura uma fixture para montar a interface antes de cada teste
@pytest.fixture(autouse=True)
def setup_interface():
  
    # Inicializa os dicionários do seu arquivo config para não quebrar a renderização
    config.dict_projetos = {}
    config.dict_tarefas = {}
    config.projeto_ativo = ""
    
    # Renderiza os componentes principais que você criou
    gui.cabecalho("Testando App")
    gui.menu_lateral()
    gui.corpo()

@pytest.mark.asyncio
async def test_fluxo_inicial_e_dialogos(user: User):
    # 1. Abre a página do app rodando em segundo plano
    await user.open('/')
    
    # 2. Verifica se o cabeçalho e o menu lateral foram renderizados
    await user.should_see('Testando App')
    await user.should_see('Menu')
    await user.should_see('Projetos Salvos')

    # 3. Testa o clique no botão "Nova Tarefa" e valida se a janela de diálogo abriu
    await user.click('Nova Tarefa')
    await user.should_see('Nome da Tarefa')
    await user.should_see('Criar Tarefa')
    
    # 4. Clica em cancelar para fechar o diálogo
    await user.click('Cancelar')

@pytest.mark.asyncio
async def test_aviso_criar_tarefa_sem_projeto(user: User):
    await user.open('/')
    
    # Abre o diálogo de nova tarefa
    await user.click('Nova Tarefa')
    
    # Preenche os campos criados no seu gui.py
    # O NiceGUI associa o label ao input interno
    await user.type('Nome da Tarefa', 'Minha Tarefa de Teste')
    await user.type('Descrição', 'Testando automação no GitHub')
    
    # Tenta criar a tarefa sem um projeto ativo
    await user.click('Criar Tarefa')
    
    # Valida se a sua função gui.nova_tarefa disparou a notificação de erro corretamente
    await user.should_see('Crie ou selecione um projeto antes de criar uma tarefa.')
