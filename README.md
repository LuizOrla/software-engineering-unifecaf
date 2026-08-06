# Kanban GUI com NiceGUI
## Descrição
Este projeto consiste em uma aplicação web desenvolvida em Python utilizando a biblioteca **NiceGUI**. Seu objetivo é fornecer um quadro Kanban simples para gerenciamento de tarefas.
A aplicação permite:
* Criar novas tarefas;
* Mover tarefas entre as colunas **A Fazer**, **Em Andamento** e **Concluído**;
* Excluir tarefas;
* Salvar automaticamente as alterações realizadas.

## Tecnologias utilizadas
* Python 3
* NiceGUI

## Estrutura do projeto

```text
.
├── data/
  └── terefas.json
├── main.py
├── gui.py
├── storage.py
├── config.py
├── requirements.txt
└── README.md
```

## Instalação
1. Clone este repositório:
```bash
git clone <url-do-repositorio>
```

2. Acesse a pasta do projeto:
```bash
cd <nome-do-projeto>
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Execução
Execute o arquivo principal:
```bash
python main.py
```

Após iniciar a aplicação, abra o navegador no endereço informado pelo NiceGUI (normalmente `http://localhost:8080`).

## Funcionalidades

* Cadastro de tarefas
* Movimentação entre colunas
* Exclusão de tarefas
* Interface gráfica web desenvolvida com NiceGUI

## Autor
Luiz Orlando
Desenvolvido como projeto de estudo da disciplina Software Engineering, do curso Análise e Desenvolvimento de Sistemas.

# V2
A segunda versão da aplicação contará com Projetos, que terão tarefas atreladas a si.
Esta adição conta com uma nova configuração de arquivos, tendo um arquivo adicional para salvamento de Projetos. As tarefas possuirão IDs de Projeto atreladas, para recuperação e exibição.

A nova estrutura contará com:
```text
.
├── data/
  └── terefas.json
  └── projetos.json
├── main.py
├── gui.py
├── storage.py
├── config.py
├── requirements.txt
└── README.md
```

A interface GUI contará com apresentação de projeto e descrição no corpo da aplicação, e com uma listagem de Projetos na barra lateral.
