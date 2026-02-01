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


def mostrar_menu():
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("4 - Remover tarefa")
    print("0 - Sair")

def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {
        "descricao": descricao,
        "concluida": False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso.")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["concluida"] else "✖"
        print(f"{indice}. [{status}] {tarefa['descricao']}")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        tarefas[indice]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa marcada como concluída.")
    except (IndexError, ValueError):
        print("Opção inválida.")

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
        tarefas.pop(indice)
        salvar_tarefas(tarefas)
        print("Tarefa removida com sucesso.")
    except (IndexError, ValueError):
        print("Opção inválida.")

def main():
    tarefas = carregar_tarefas()

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)
        elif opcao == "2":
            listar_tarefas(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            remover_tarefa(tarefas)
        elif opcao == "0":
            confirmar = input("Deseja realmente sair? (s/n): ").lower()
            if confirmar == "s":
            print("Saindo do sistema.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()


