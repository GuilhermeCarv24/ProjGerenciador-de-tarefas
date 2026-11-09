
import json
from pathlib import Path


CAMINHO_ARQUIVO = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "tarefas.json"
)


def carregar_tarefas():

    if not CAMINHO_ARQUIVO.exists():
        return []

    try:
        with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        return dados if isinstance(dados, list) else []

    except (json.JSONDecodeError, OSError):
        return []


def salvar_tarefas(tarefas):

    CAMINHO_ARQUIVO.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    dados = [
        tarefa.para_dicionario()
        for tarefa in tarefas
    ]

    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            ensure_ascii=False,
            indent=4
        )
