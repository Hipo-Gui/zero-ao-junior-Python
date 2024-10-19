# def duplicar(num):
#    return num * 2

# def triplicar(num):
#    return num * 3

# def quadruplicar(num):
#    return num * 4

# Exemplos de uso:
#numero = 5
#print(f"Dobro de {numero}: {duplicar(numero)}")
#print(f"Triplo de {numero}: {triplicar(numero)}")
#print(f"Quadruplicado de {numero}: {quadruplicar(numero)}")

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))