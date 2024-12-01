import os 

mensagens = []

nome = input('Nome:')

while True: 
    # limpando terminal
    os.system('cls')

    if len(mensagens) > 0:
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print('__________')

    # Obtendo texto 
    texto = input('Mensagem: ') 
    if texto == 'fim':
        break

    # adicinando mensagem na lista

    mensagens.append({
        'nome': nome, 
        'texto': texto
})
        