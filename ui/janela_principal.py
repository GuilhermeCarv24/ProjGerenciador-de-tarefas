
import tkinter as tk
from tkinter import messagebox

from ui.janela_cadastro import JanelaCadastro
from models.tarefa import Tarefa
from storage.armazenamento import carregar_tarefas, salvar_tarefas


class JanelaPrincipal:

    def __init__(self):

        self.cores = {
            "fundo": "#111318",
            "sidebar": "#191C24",
            "card": "#20242E",
            "card_hover": "#292E3A",
            "azul": "#5278E8",
            "azul_claro": "#7896FF",
            "texto": "#F1F3F8",
            "texto_secundario": "#9299A9",
            "borda": "#303542",
            "verde": "#48C78E",
            "amarelo": "#E9B85D",
            "vermelho": "#E36B75"
        }

        self.tarefas = [
            Tarefa.de_dicionario(dados)
            for dados in carregar_tarefas()
        ]

        self.janela = tk.Tk()
        self.janela.title("TaskFlow | Gerenciador de Tarefas")
        self.janela.geometry("1100x700")
        self.janela.minsize(900, 600)
        self.janela.configure(bg=self.cores["fundo"])

        self.criar_interface()
        self.atualizar_dashboard()

        self.janela.mainloop()

    # ==========================================
    # INTERFACE PRINCIPAL
    # ==========================================

    def criar_interface(self):

        self.sidebar = tk.Frame(
            self.janela,
            bg=self.cores["sidebar"],
            width=220
        )

        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        self.conteudo = tk.Frame(
            self.janela,
            bg=self.cores["fundo"]
        )

        self.conteudo.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.criar_sidebar()
        self.criar_conteudo()

    # ==========================================
    # MENU LATERAL
    # ==========================================

    def criar_sidebar(self):

        tk.Label(
            self.sidebar,
            text="◆  TASKFLOW",
            font=("Segoe UI", 17, "bold"),
            bg=self.cores["sidebar"],
            fg=self.cores["azul_claro"]
        ).pack(pady=(35, 45), padx=20, anchor="w")

        tk.Label(
            self.sidebar,
            text="MENU PRINCIPAL",
            font=("Segoe UI", 9, "bold"),
            bg=self.cores["sidebar"],
            fg=self.cores["texto_secundario"]
        ).pack(anchor="w", padx=22, pady=(0, 12))

        self.botoes_menu = {}

        opcoes = [
            ("▦", "Dashboard"),
            ("☷", "Minhas tarefas"),
            ("◷", "Pendentes"),
            ("✓", "Concluídas")
        ]

        for icone, nome in opcoes:

            botao = tk.Button(
                self.sidebar,
                text=f"   {icone}   {nome}",
                font=("Segoe UI", 10),
                bg=self.cores["azul"] if nome == "Dashboard"
                else self.cores["sidebar"],
                fg=self.cores["texto"],
                activebackground=self.cores["card_hover"],
                activeforeground=self.cores["texto"],
                relief="flat",
                bd=0,
                anchor="w",
                padx=12,
                pady=12,
                cursor="hand2",
                command=lambda n=nome: self.selecionar_pagina(n)
            )

            botao.pack(fill="x", padx=12, pady=3)
            self.botoes_menu[nome] = botao

        rodape = tk.Frame(
            self.sidebar,
            bg=self.cores["sidebar"]
        )

        rodape.pack(side="bottom", fill="x", pady=20, padx=20)

        tk.Frame(
            rodape,
            bg=self.cores["borda"],
            height=1
        ).pack(fill="x", pady=(0, 15))

        tk.Label(
            rodape,
            text="TASKFLOW V2.0",
            font=("Segoe UI", 9, "bold"),
            bg=self.cores["sidebar"],
            fg=self.cores["texto_secundario"]
        ).pack(anchor="w")

        tk.Label(
            rodape,
            text="Gerenciador de tarefas",
            font=("Segoe UI", 8),
            bg=self.cores["sidebar"],
            fg=self.cores["texto_secundario"]
        ).pack(anchor="w", pady=(4, 0))

    # ==========================================
    # CONTEÚDO PRINCIPAL
    # ==========================================

    def criar_conteudo(self):

        cabecalho = tk.Frame(
            self.conteudo,
            bg=self.cores["fundo"]
        )

        cabecalho.pack(
            fill="x",
            padx=35,
            pady=(30, 25)
        )

        tk.Label(
            cabecalho,
            text="Olá, seja bem-vindo!",
            font=("Segoe UI", 21, "bold"),
            bg=self.cores["fundo"],
            fg=self.cores["texto"]
        ).pack(anchor="w")

        tk.Label(
            cabecalho,
            text="Aqui está um resumo das suas atividades.",
            font=("Segoe UI", 10),
            bg=self.cores["fundo"],
            fg=self.cores["texto_secundario"]
        ).pack(anchor="w", pady=(5, 0))

        self.criar_estatisticas()
        self.criar_area_tarefas()

    # ==========================================
    # ESTATÍSTICAS
    # ==========================================

    def criar_estatisticas(self):

        area = tk.Frame(
            self.conteudo,
            bg=self.cores["fundo"]
        )

        area.pack(fill="x", padx=35, pady=(0, 25))

        self.valores_estatisticas = {}

        estatisticas = [
            ("TOTAL DE TAREFAS", "▦", self.cores["azul_claro"]),
            ("CONCLUÍDAS", "✓", self.cores["verde"]),
            ("PENDENTES", "◷", self.cores["amarelo"])
        ]

        for coluna, (titulo, icone, cor) in enumerate(estatisticas):

            card = tk.Frame(
                area,
                bg=self.cores["card"],
                padx=20,
                pady=16,
                highlightbackground=self.cores["borda"],
                highlightthickness=1
            )

            card.grid(
                row=0,
                column=coluna,
                sticky="nsew",
                padx=(0, 12) if coluna < 2 else (0, 0)
            )

            tk.Label(
                card,
                text=icone,
                font=("Segoe UI", 19, "bold"),
                bg=self.cores["card"],
                fg=cor
            ).pack(anchor="w")

            valor = tk.Label(
                card,
                text="0",
                font=("Segoe UI", 25, "bold"),
                bg=self.cores["card"],
                fg=self.cores["texto"]
            )

            valor.pack(anchor="w", pady=(6, 2))

            self.valores_estatisticas[titulo] = valor

            tk.Label(
                card,
                text=titulo,
                font=("Segoe UI", 9, "bold"),
                bg=self.cores["card"],
                fg=self.cores["texto_secundario"]
            ).pack(anchor="w")

            area.grid_columnconfigure(coluna, weight=1)

    # ==========================================
    # ÁREA DE TAREFAS
    # ==========================================

    def criar_area_tarefas(self):

        area = tk.Frame(
            self.conteudo,
            bg=self.cores["fundo"]
        )

        area.pack(
            fill="both",
            expand=True,
            padx=35,
            pady=(0, 30)
        )

        cabecalho = tk.Frame(
            area,
            bg=self.cores["fundo"]
        )

        cabecalho.pack(fill="x", pady=(0, 18))

        tk.Label(
            cabecalho,
            text="Minhas tarefas",
            font=("Segoe UI", 15, "bold"),
            bg=self.cores["fundo"],
            fg=self.cores["texto"]
        ).pack(side="left")

        tk.Button(
            cabecalho,
            text="+ Nova tarefa",
            font=("Segoe UI", 9, "bold"),
            bg=self.cores["azul"],
            fg="white",
            activebackground=self.cores["azul_claro"],
            activeforeground="white",
            relief="flat",
            bd=0,
            padx=16,
            pady=9,
            cursor="hand2",
            command=self.adicionar_tarefa
        ).pack(side="right")

        self.quadro_tarefas = tk.Frame(
            area,
            bg=self.cores["card"],
            highlightbackground=self.cores["borda"],
            highlightthickness=1
        )

        self.quadro_tarefas.pack(fill="both", expand=True)

    # ==========================================
    # ATUALIZAÇÃO DO DASHBOARD
    # ==========================================

    def atualizar_dashboard(self):

        total = len(self.tarefas)
        concluidas = sum(1 for tarefa in self.tarefas if tarefa.concluida)
        pendentes = total - concluidas

        self.valores_estatisticas["TOTAL DE TAREFAS"].config(text=str(total))
        self.valores_estatisticas["CONCLUÍDAS"].config(text=str(concluidas))
        self.valores_estatisticas["PENDENTES"].config(text=str(pendentes))

        for widget in self.quadro_tarefas.winfo_children():
            widget.destroy()

        if not self.tarefas:

            tk.Label(
                self.quadro_tarefas,
                text="Nenhuma tarefa cadastrada",
                font=("Segoe UI", 14, "bold"),
                bg=self.cores["card"],
                fg=self.cores["texto"]
            ).pack(pady=(65, 10))

            tk.Label(
                self.quadro_tarefas,
                text="Clique em '+ Nova tarefa' para começar.",
                font=("Segoe UI", 9),
                bg=self.cores["card"],
                fg=self.cores["texto_secundario"]
            ).pack()

            return

        for tarefa in self.tarefas:
            self.criar_cartao_tarefa(tarefa)

    # ==========================================
    # CARTÃO INDIVIDUAL DA TAREFA
    # ==========================================

    def criar_cartao_tarefa(self, tarefa):

        card = tk.Frame(
            self.quadro_tarefas,
            bg=self.cores["card_hover"],
            padx=15,
            pady=12
        )

        card.pack(fill="x", padx=15, pady=7)

        informacoes = tk.Frame(
            card,
            bg=self.cores["card_hover"]
        )

        informacoes.pack(side="left", fill="both", expand=True)

        cor_titulo = (
            self.cores["texto_secundario"]
            if tarefa.concluida
            else self.cores["texto"]
        )

        titulo = tarefa.descricao

        if tarefa.concluida:
            titulo = "✓  " + titulo

        tk.Label(
            informacoes,
            text=titulo,
            font=("Segoe UI", 11, "bold"),
            bg=self.cores["card_hover"],
            fg=cor_titulo,
            anchor="w"
        ).pack(anchor="w")

        detalhes = (
            f"{tarefa.categoria}  •  Prioridade: {tarefa.prioridade}"
        )

        if tarefa.prazo:
            detalhes += f"  •  Prazo: {tarefa.prazo}"

        tk.Label(
            informacoes,
            text=detalhes,
            font=("Segoe UI", 8),
            bg=self.cores["card_hover"],
            fg=self.cores["texto_secundario"],
            anchor="w"
        ).pack(anchor="w", pady=(5, 0))

        if tarefa.detalhes:

            tk.Label(
                informacoes,
                text=tarefa.detalhes,
                font=("Segoe UI", 9),
                bg=self.cores["card_hover"],
                fg=self.cores["texto_secundario"],
                anchor="w",
                wraplength=450,
                justify="left"
            ).pack(anchor="w", pady=(5, 0))

        botoes = tk.Frame(
            card,
            bg=self.cores["card_hover"]
        )

        botoes.pack(side="right", padx=(10, 0))

        texto_botao = "Reabrir" if tarefa.concluida else "Concluir"

        tk.Button(
            botoes,
            text=texto_botao,
            font=("Segoe UI", 8, "bold"),
            bg=self.cores["azul"],
            fg="white",
            relief="flat",
            cursor="hand2",
            command=lambda t=tarefa: self.alternar_conclusao(t)
        ).pack(side="left", padx=4)

        tk.Button(
            botoes,
            text="Excluir",
            font=("Segoe UI", 8, "bold"),
            bg="#63343B",
            fg="white",
            relief="flat",
            cursor="hand2",
            command=lambda t=tarefa: self.excluir_tarefa(t)
        ).pack(side="left", padx=4)

    # ==========================================
    # CADASTRO E GERENCIAMENTO
    # ==========================================

    def adicionar_tarefa(self):

        JanelaCadastro(
            self.janela,
            self.receber_tarefa
        )

    def receber_tarefa(self, tarefa):

        self.tarefas.append(tarefa)
        salvar_tarefas(self.tarefas)
        self.atualizar_dashboard()

    def alternar_conclusao(self, tarefa):

        if tarefa.concluida:
            tarefa.reabrir()
        else:
            tarefa.concluir()

        salvar_tarefas(self.tarefas)
        self.atualizar_dashboard()

    def excluir_tarefa(self, tarefa):

        confirmar = messagebox.askyesno(
            "Excluir tarefa",
            f"Deseja realmente excluir '{tarefa.descricao}'?"
        )

        if not confirmar:
            return

        self.tarefas.remove(tarefa)
        salvar_tarefas(self.tarefas)
        self.atualizar_dashboard()

    # ==========================================
    # NAVEGAÇÃO
    # ==========================================

    def selecionar_pagina(self, pagina):

        for nome, botao in self.botoes_menu.items():

            cor = (
                self.cores["azul"]
                if nome == pagina
                else self.cores["sidebar"]
            )

            botao.configure(bg=cor)

        if pagina != "Dashboard":

            messagebox.showinfo(
                "TaskFlow",
                f"A seção '{pagina}' será implementada em uma próxima versão."
            )
