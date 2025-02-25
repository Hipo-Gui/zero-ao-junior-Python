import os

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefas)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para listar')
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefas)
    print()
  


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip() 
    if not tarefa:
        print('Você não digitou uma tarefa')
        return
    print(f'{tarefa=} adicionar na lista de tarefas.')
    tarefas.append(tarefa)
    print()

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: Lista, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando:')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue   
    
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue 
    elif tarefa == 'cls':
        os.system('cls')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue
