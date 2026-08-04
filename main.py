# Arquivo principal de orquestração
# Responsável por iniciar a aplicação

from storage import ler_arquivos
from gui import cabecalho
from gui import menu_lateral
from gui import corpo
from nicegui import ui

ler_arquivos() # Chama a função que lê os arquivos

cabecalho("Gerenciamento de Tarefas") # Inicia a aplicação
menu_lateral() # Renderiza o menu lateral
corpo() # Renderiza o corpo da aplicação
ui.run() # Roda a aplicação
