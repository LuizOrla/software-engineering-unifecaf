# Interface GUI da aplicação
from nicegui import ui
import config
import storage

def cabecalho(titulo):  # Cria um cabeçalho com o texto enviado centralizado
    with ui.header().classes("bg-blue items-center justify-center text-white py-6"):
        ui.label(titulo).classes("text-3xl font-bold absolute-center")

def menu_lateral():  # Cria um menu lateral aberto, com os botões de ação
    with ui.left_drawer(value=True).classes("bg-slate-100 p-4"):
        # Objeto left_drawer configurado para estar sempre aberto
        ui.label("Menu").classes("text-lg mb-1")
        # Botão chama a função janela_nova_tarefa, que abre uma janela solicitando informações
        ui.button("Nova Tarefa", icon="add", on_click=janela_nova_tarefa,).props("flat").classes("w-full justify-start")

@ui.refreshable  # Tag do pacote NiceGui que torna conteúdo recarregável, sem recarregar aplicação toda
def corpo():  # Cria os componentes do corpo da aplicação, com as colunas e os cards de tarefa
    with ui.row().classes("w-full justify-center"):
        with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
            ui.label("A Fazer").classes("text-lg font-semibold")
            for id_tarefa, tarefa in config.dict_tarefas.items():
                if tarefa["status"] == "todo":
                    card_tarefa(id_tarefa, tarefa["nome"], tarefa["descricao"], tarefa["status"])

        with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
            ui.label("Em Andamento").classes("text-lg font-semibold")
            for id_tarefa, tarefa in config.dict_tarefas.items():
                if tarefa["status"] == "doing":
                    card_tarefa(id_tarefa, tarefa["nome"], tarefa["descricao"], tarefa["status"])
        with ui.card().classes("bg-gray-100 p-4 rounded-lg shadow-none border border-gray-200 w-2/8 h-[700px] overflow-y-auto items-start"):
            ui.label("Concluído").classes("text-lg font-semibold")
            for id_tarefa, tarefa in config.dict_tarefas.items():
                if tarefa["status"] == "done":
                    card_tarefa(id_tarefa, tarefa["nome"], tarefa["descricao"], tarefa["status"])

def card_tarefa(id, nome, descricao, status):  # Cria o card para cada tarefa, com Nome, ID, descrição e botões de ação
    with ui.card().classes("w-full p-2 gap-0.5 justify-between") as card:
        ui.label(nome).classes("text-base font-semibold")
        ui.label(f"ID: {id}").classes("text-xs text-gray-400")
        ui.label(descricao).classes("text-sm")

        with ui.row().classes("w-full justify-between items-center"):
            if status in ["doing", "done"]:
                ui.button(icon="arrow_back", on_click=lambda: move_tarefa(id, "retorna")).props("flat dense")
            else:
                ui.element("div").classes()
                ui.button(icon="delete", on_click=lambda: excluir_tarefa(id, card)).props("flat dense color=red")
            if status in ["doing", "todo"]:
                ui.button(icon="arrow_forward", on_click=lambda: move_tarefa(id, "avanca")).props("flat dense")
            else:
                ui.element("div").classes()

def janela_nova_tarefa():  # Cria uma janela para criação de nova tarefa, solicitando nome e descrição
    with ui.dialog() as dialogo, ui.card().classes("w-2/5"):
        ui.label("Nova Tarefa")
        nome_tarefa = ui.input(label="Nome da Tarefa").classes("w-full")
        desc_tarefa = ui.input(label="Descrição").classes("w-full")
        with ui.row().classes("w-full justify-end"):
            ui.button("Cancelar", on_click=dialogo.close).props("flat")
            ui.button("Criar Tarefa", on_click=lambda: nova_tarefa(nome_tarefa.value, desc_tarefa.value, dialogo))
    dialogo.open()

def move_tarefa(id, direcao):  # Função responsável por mover uma tarefa
    match direcao:
        case "avanca": storage.avancar_tarefa(id)
        case "retorna": storage.retornar_tarefa(id)
    corpo.refresh()

def nova_tarefa(nome, descricao, dialogo):  # Função responsável por criar uma nova tarefa
    storage.criar_tarefa(nome, descricao)
    dialogo.close()
    corpo.refresh()

def excluir_tarefa(id, card):  # Função responsável por excluir uma tarefa
    storage.apagar_tarefa(id)
    card.delete()
