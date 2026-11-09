
class Tarefa:

    def __init__(
        self,
        descricao,
        detalhes="",
        prioridade="Média",
        categoria="Pessoal",
        prazo="",
        concluida=False
    ):
        self.descricao = descricao
        self.detalhes = detalhes
        self.prioridade = prioridade
        self.categoria = categoria
        self.prazo = prazo
        self.concluida = concluida

    def concluir(self):
        self.concluida = True

    def reabrir(self):
        self.concluida = False

    def para_dicionario(self):
        return {
            "descricao": self.descricao,
            "detalhes": self.detalhes,
            "prioridade": self.prioridade,
            "categoria": self.categoria,
            "prazo": self.prazo,
            "concluida": self.concluida
        }

    @classmethod
    def de_dicionario(cls, dados):
        return cls(
            descricao=dados.get("descricao", ""),
            detalhes=dados.get("detalhes", ""),
            prioridade=dados.get("prioridade", "Média"),
            categoria=dados.get("categoria", "Pessoal"),
            prazo=dados.get("prazo", ""),
            concluida=dados.get("concluida", False)
        )
