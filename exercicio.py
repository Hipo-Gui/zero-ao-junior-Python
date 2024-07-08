# Crie um função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor 
# da variável
"""
print('Tabela + soma:')
def soma(*args):
    total = 1
    for numero in args:
        print('Total:', total, numero)
        total = total * numero
        return total

soma(1 * 2 * 3 * 4 * 5)   
"""

# Crie uma função fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar 
def par_ímpar(numero):
    par = numero % 2 == 0

    if par:
        return f'{numero} é par'
    return f'{numero} é ímpar'
    
OutroParImpar = par_ímpar
doisEpar = OutroParImpar(2)
print(par_ímpar(2))
print(par_ímpar(14))
print(par_ímpar(16))

print(par_ímpar in OutroParImpar)
