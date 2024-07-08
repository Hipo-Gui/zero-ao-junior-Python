#Função variádicos quando existe a necessidade de ter uma variável que pode ou não ser utilizada, variável opcional no caso;
"""
args - Argumentos não nomeados
* - *args (empacotamento e desampacotamento)

# Lembre-te de desempacotamento
x, y *resto = 1, 2, 3, 4
print(x, y, resto)
"""

def soma(*args):
    soma = 0
    for total in args:
        soma + total
    return soma

print(sum((1, 2, 3, 5, 6, 7, 8, 9))) 

print(soma())   

# Usei a função "args" para passar uma quantidade de argumentos não nomeados. No caso "1, 2, 3, 5, 6, 7, 8, 9".

 
    
     



 