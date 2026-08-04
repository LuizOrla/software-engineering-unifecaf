# Arquivo de classes principais
class Tarefa:
    '''
    Estrutura do dicionário:
    ```
    dict_tarefa = {
        id_tarefa: {
            "projeto": ID do projeto,
            "nome": Nome da Tarefa,
            "descricao": Descrição da Tarefa,
            "status": Status da Tarefa
        }
    }
    '''
    def __init__(self, id, id_projeto, nome, descricao, status="todo"): # Função inicializadora, com titulo, descrição, ID, ID do projeto e status
        self.id = id
        self.id_projeto = id_projeto
        self.nome = nome
        self.descricao = descricao
        self.status = status

    def dicionario_tarefa(self): # Função que cria entrada em dicionário
        id_dict = self.id
        dict = {
            "projeto": self.id_projeto,
            "nome": self.nome,
            "descricao": self.descricao,
            "status": self.status
        }
        return id_dict, dict
