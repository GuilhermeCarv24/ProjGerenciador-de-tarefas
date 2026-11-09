import json
import os

ARQUIVO = 'Tasks.json'

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'r') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO, 'w') as f:
        json.dump(tarefas, f, indent=4)

def adicionar_tarefa(tarefas):
    nome = input('Digite o nome da tarefa: ')
    tarefas.append({'descrição': nome, 'concluída': False})
    print('Tarefa adicionada!')

def listar_tarefas(tarefas):
    if not tarefas:
        print('Nenhuma tarefa encontrada!')
        return
    for i, tarefa in enumerate(tarefas, 1):
        status = '✅' if tarefa['concluída'] else '❌'
        print(f'{i}. {tarefa["descrição"]} [{status}]')

def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        i = int(input('Número da tarefa concluída:')) - 1
        if 0 <= i < len(tarefas):
            tarefas[i]['concluída'] = True
            print('Tarefa marcada como concluída!')
        else:
            print('Entrada inválida!')
    except ValueError:
        print('Entrada inválida!')

def remover_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        i = int(input('Número da tarefa a remover:')) - 1
        if 0 <= i < len(tarefas):
            removida = tarefas.pop(i)
            print(f"Tarefa '{removida['descrição']}' removida!")
        else:
            print('Número inválido!')
    except ValueError:
        print('Entrada inválida!')

def menu():
    tarefas = carregar_tarefas()
    while True:
        print('\n=== GERENCIADOR DE TAREFAS ===')
        print('1. Adicionar tarefa')
        print('2. Listar tarefas')
        print('3. Marcar como concluída')
        print('4. Remover tarefa')
        print('5. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            marcar_concluida(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao == '5':
            salvar_tarefas(tarefas)
            print('Tarefas salvas. Até mais!')
            break
        else:
            print('Opção inválida!')

if __name__ == '__main__':
    menu()
