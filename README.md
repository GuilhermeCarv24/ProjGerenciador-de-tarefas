# 📝 Gerenciador de Tarefas

Um gerenciador de tarefas desenvolvido em **Python**, com interface via terminal, que permite adicionar, visualizar, concluir e remover tarefas de maneira simples e organizada.

O projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais de programação, manipulação de dados e persistência de informações utilizando arquivos JSON.

## 🚀 Funcionalidades

- **Adicionar tarefas:** permite cadastrar novas tarefas.
- **Listar tarefas:** exibe todas as tarefas cadastradas.
- **Concluir tarefas:** permite marcar tarefas como concluídas.
- **Remover tarefas:** possibilita excluir tarefas da lista.
- **Salvar automaticamente ao sair:** armazena as informações em um arquivo JSON para que permaneçam disponíveis na próxima execução.

## 🛠️ Tecnologias utilizadas

- **Python 3** — Linguagem utilizada no desenvolvimento.
- **JSON** — Armazenamento e persistência dos dados.
- **Biblioteca `os`** — Verificação da existência do arquivo de dados.

## 📂 Estrutura do projeto

```text
Gerenciador-de-Tarefas/
│
├── main.py
├── Tasks.json
└── README.md
```

> O arquivo `Tasks.json` é criado automaticamente quando as tarefas são salvas pela primeira vez.

## ⚙️ Como executar

**1. Clone o repositório:**

```bash
git clone URL_DO_SEU_REPOSITORIO
```

**2. Entre na pasta do projeto:**

```bash
cd Gerenciador-de-Tarefas
```

**3. Execute o programa:**

```bash
python main.py
```

Não é necessário instalar bibliotecas externas, pois o projeto utiliza apenas módulos nativos do Python.

## 💻 Funcionamento

Ao executar o programa, será apresentado um menu interativo no terminal:

```text
=== GERENCIADOR DE TAREFAS ===

1. Adicionar tarefa
2. Listar tarefas
3. Marcar como concluída
4. Remover tarefa
5. Sair

Escolha uma opção:
```

O usuário pode escolher uma das opções para gerenciar suas tarefas.

## 📚 Aprendizados

Durante o desenvolvimento deste projeto, foram trabalhados conceitos importantes:

- Criação e utilização de funções.
- Manip
