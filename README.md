# 🚀 TaskFlow V2 — Gerenciador de Tarefas

Um gerenciador de tarefas desenvolvido em **Python**, com interface gráfica utilizando **Tkinter**, projetado para facilitar a organização e o acompanhamento de atividades do dia a dia.

O TaskFlow evoluiu de uma aplicação executada pelo terminal para uma aplicação desktop com interface visual, permitindo gerenciar tarefas de maneira mais intuitiva e organizada.

## ✨ Funcionalidades

- **Cadastro de tarefas:** crie tarefas com título e descrição.
- **Categorias:** organize atividades entre Pessoal, Estudos, Trabalho, Lazer e Outros.
- **Prioridades:** classifique tarefas como Baixa, Média ou Alta.
- **Prazos:** defina datas para suas atividades.
- **Conclusão de tarefas:** marque atividades como concluídas.
- **Reabertura:** recupere tarefas já concluídas.
- **Exclusão:** remova tarefas com confirmação.
- **Painel de acompanhamento:** visualize estatísticas das tarefas.
- **Persistência de dados:** as informações são armazenadas em JSON, permanecendo disponíveis ao reabrir o programa.

## 🛠️ Tecnologias utilizadas

- **Python 3** — Linguagem principal.
- **Tkinter** — Desenvolvimento da interface gráfica.
- **JSON** — Armazenamento e persistência dos dados.
- **Git e GitHub** — Versionamento e hospedagem do projeto.

## 📂 Estrutura do projeto

```text
ProjGerenciador-de-tarefas/
│
├── main.py
├── gerenciador.py
├── README.md
├── .gitignore
│
├── models/
│   └── tarefa.py
│
├── storage/
│   └── armazenamento.py
│
├── ui/
│   ├── janela_principal.py
│   └── janela_cadastro.py
│
├── services/
│
└── data/
    └── tarefas.json
```

> O arquivo `tarefas.json` é criado automaticamente durante a utilização do programa, quando necessário. Os dados locais são ignorados pelo Git.

## ⚙️ Como executar

**1. Clone o repositório:**

```bash
git clone https://github.com/GuilhermeCarv24/ProjGerenciador-de-tarefas.git
```

**2. Entre na pasta do projeto:**

```bash
cd ProjGerenciador-de-tarefas
```

**3. Execute a aplicação:**

```bash
python main.py
```

Não é necessário instalar bibliotecas externas. O projeto utiliza recursos nativos do Python.

## 🖥️ Interface e funcionamento

O TaskFlow V2 possui uma interface gráfica desenvolvida com Tkinter, com painel principal para acompanhamento das tarefas e uma janela específica para cadastrar novas atividades.

O programa permite organizar compromissos, acompanhar prioridades, controlar prazos e atualizar o status das atividades.

## 📌 Evolução do projeto

- **V1:** primeira versão executada pelo terminal, com funcionalidades básicas de gerenciamento de tarefas.
- **V2:** reformulação da aplicação com interface gráfica, organização em módulos, cadastro detalhado e armazenamento em JSON.
- **V3:** melhorias planejadas para ampliar a navegação e a organização das tarefas.

## 📚 Aprendizados

Durante o desenvolvimento, foram trabalhados conceitos importantes:

- Programação orientada a objetos.
- Organização de projetos em módulos.
- Desenvolvimento de interfaces gráficas.
- Manipulação de arquivos JSON.
- Persistência de dados.
- Tratamento de informações e validações.
- Versionamento de código com Git.

## 👨‍💻 Desenvolvedor

**Guilherme Carvalho**

Estudante de Engenharia de Software e desenvolvedor em formação.

- GitHub: [GuilhermeCarv24](https://github.com/GuilhermeCarv24)
- Repositório: [ProjGerenciador-de-tarefas](https://github.com/GuilhermeCarv24/ProjGerenciador-de-tarefas)

---

*Projeto desenvolvido para fins de aprendizado e evolução prática em desenvolvimento de software.*
