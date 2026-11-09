
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from models.tarefa import Tarefa


class JanelaCadastro:

    def __init__(self, janela_pai, ao_salvar):

        self.ao_salvar = ao_salvar

        self.cores = {
            "fundo": "#191C24",
            "card": "#20242E",
            "azul": "#5278E8",
            "azul_claro": "#7896FF",
            "texto": "#F1F3F8",
            "secundario": "#9299A9"
        }

        self.janela = tk.Toplevel(janela_pai)
        self.janela.title("Nova tarefa | TaskFlow")
        self.janela.geometry("500x720")
        self.janela.resizable(False, False)
        self.janela.configure(bg=self.cores["fundo"])

        self.janela.transient(janela_pai)
        self.janela.grab_set()

        self.criar_interface()

    def criar_interface(self):

        container = tk.Frame(
            self.janela,
            bg=self.cores["fundo"],
            padx=30,
            pady=25
        )

        container.pack(fill="both", expand=True)

        # Cabeçalho
        tk.Label(
            container,
            text="Nova tarefa",
            font=("Segoe UI", 21, "bold"),
            bg=self.cores["fundo"],
            fg=self.cores["texto"]
        ).pack(anchor="w")

        tk.Label(
            container,
            text="Preencha as informações da sua atividade.",
            font=("Segoe UI", 9),
            bg=self.cores["fundo"],
            fg=self.cores["secundario"]
        ).pack(anchor="w", pady=(5, 22))

        # Nome
        self.criar_label(container, "Nome da tarefa")

        self.entrada_descricao = tk.Entry(
            container,
            font=("Segoe UI", 10),
            bg=self.cores["card"],
            fg=self.cores["texto"],
            insertbackground="white",
            relief="flat"
        )

        self.entrada_descricao.pack(
            fill="x",
            ipady=10,
            pady=(6, 16)
        )

        # Descrição
        self.criar_label(container, "Descrição adicional")

        self.entrada_detalhes = tk.Text(
            container,
            height=4,
            font=("Segoe UI", 10),
            bg=self.cores["card"],
            fg=self.cores["texto"],
            insertbackground="white",
            relief="flat",
            wrap="word"
        )

        self.entrada_detalhes.pack(
            fill="x",
            pady=(6, 16)
        )

        # Prioridade
        self.criar_label(container, "Prioridade")

        self.prioridade = ttk.Combobox(
            container,
            values=["Baixa", "Média", "Alta"],
            state="readonly",
            font=("Segoe UI", 10)
        )

        self.prioridade.set("Média")

        self.prioridade.pack(
            fill="x",
            ipady=5,
            pady=(6, 16)
        )

        # Categoria
        self.criar_label(container, "Categoria")

        self.categoria = ttk.Combobox(
            container,
            values=[
                "Pessoal",
                "Estudos",
                "Trabalho",
                "Lazer",
                "Outros"
            ],
            state="readonly",
            font=("Segoe UI", 10)
        )

        self.categoria.set("Pessoal")

        self.categoria.pack(
            fill="x",
            ipady=5,
            pady=(6, 16)
        )

        # Prazo
        self.criar_label(container, "Prazo (DD/MM/AAAA)")

        self.entrada_prazo = tk.Entry(
            container,
            font=("Segoe UI", 10),
            bg=self.cores["card"],
            fg=self.cores["texto"],
            insertbackground="white",
            relief="flat"
        )

        self.entrada_prazo.pack(
            fill="x",
            ipady=10,
            pady=(6, 22)
        )

        # Botões
        botoes = tk.Frame(
            container,
            bg=self.cores["fundo"]
        )

        botoes.pack(fill="x", pady=(5, 0))

        tk.Button(
            botoes,
            text="Cancelar",
            font=("Segoe UI", 10, "bold"),
            bg=self.cores["card"],
            fg=self.cores["texto"],
            activebackground="#303542",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.janela.destroy
        ).pack(
            side="left",
            expand=True,
            fill="x",
            padx=(0, 8),
            ipady=12
        )

        tk.Button(
            botoes,
            text="Salvar tarefa",
            font=("Segoe UI", 10, "bold"),
            bg=self.cores["azul"],
            fg="white",
            activebackground=self.cores["azul_claro"],
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.salvar
        ).pack(
            side="right",
            expand=True,
            fill="x",
            padx=(8, 0),
            ipady=12
        )

        self.entrada_descricao.focus_set()

    def criar_label(self, pai, texto):

        tk.Label(
            pai,
            text=texto,
            font=("Segoe UI", 9, "bold"),
            bg=self.cores["fundo"],
            fg=self.cores["texto"]
        ).pack(anchor="w")

    def salvar(self):

        descricao = self.entrada_descricao.get().strip()
        detalhes = self.entrada_detalhes.get(
            "1.0",
            "end-1c"
        ).strip()

        prioridade = self.prioridade.get()
        categoria = self.categoria.get()
        prazo = self.entrada_prazo.get().strip()

        if not descricao:

            messagebox.showwarning(
                "Campo obrigatório",
                "Digite o nome da tarefa.",
                parent=self.janela
            )

            self.entrada_descricao.focus_set()
            return

        if prazo:

            try:
                data = datetime.strptime(
                    prazo,
                    "%d/%m/%Y"
                )

                if data.date() < datetime.today().date():

                    messagebox.showwarning(
                        "Prazo inválido",
                        "A data não pode estar no passado.",
                        parent=self.janela
                    )

                    return

            except ValueError:

                messagebox.showwarning(
                    "Data inválida",
                    "Digite uma data válida no formato DD/MM/AAAA.",
                    parent=self.janela
                )

                return

        tarefa = Tarefa(
            descricao=descricao,
            detalhes=detalhes,
            prioridade=prioridade,
            categoria=categoria,
            prazo=prazo
        )

        self.ao_salvar(tarefa)
        self.janela.destroy()
