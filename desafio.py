
fluxo_caixa = []

print("-----------")
print("@ Fluxo caixa")
print("----------")
print("1 - adicionar receita")
print("2 - adicionar despesa")
print("\n# Digite outro numero para encerrar #\n")


def adicionar_transacao():
    nome = input('Nome: ')
    valor = float( input('Valor: '))
    fluxo_caixa.append({
        'nome': nome, 
        'valor': valor
    })

while True: 

    opcao = int( input('Digite a opção: '))

    if opcao == 1:
         adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao ()
    else:
        break

#nota fiscal
print("\n--- Resumo do Fluxo de Caixa ---")
total = 0
for transacao in fluxo_caixa:
    print(f"Nome: {transacao['nome']}, Valor: R$ {transacao['valor']:.2f}")
    total += transacao['valor']

print(f"\nSaldo atual: R$ {total:.2f}")