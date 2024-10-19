# exercícios - sistemas de oerguntas e respostas

perguntas = [
    {
        'pergunta': 'Quanto é 2+2',
        'Opções': ['1', '3', '4', '100'],
        'Resposta': '4',
    },
    {
        'pergunta': 'Quanto é 5*5',
        'Opções': ['25', '10', '12', '0'],
        'Resposta': '25',
    },
    {
        'pergunta': 'Quanto é 10/2',
        'Opções': ['66', '77', '5', '1'],
        'Resposta': '5',
    },
]
qtd_acertos = 0
for pergunta in perguntas:
    print('pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha um opção: ')    

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()

print('Você acertou', qtd_acertos) 
print('de', len(perguntas), 'Perguntas.')
                         
