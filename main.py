import json

ARQUIVO_TAREFAS = "tarefas.json"


def carregar_tarefas():
    try:
        with open(ARQUIVO_TAREFAS, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)
