#função com retorno nomeado
print('Tabela + soma:')
def soma(*args):
    total = 0
    for numero in args:
        print('Total:', total, numero)
        total = total + numero
        print('Total =', total)
    print('Valor final =',total)

soma(1, 2, 3, 4, 5, 6, 7)   

# RETORNO NOMEADOS SERVI PARA AJUDAR NA INTERPRETAÇÃO DE UM OU MAIS VALORES RETORNADOS. FACILITANDO A VIDA DO USUÁRIO. 
