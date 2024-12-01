def triangulo_retangulo(*args):
    global a, b, c
    if len(args) == 3:
        a, b, c = args
    else:
        print("Forneça exatamente três valores para os lados do triângulo.")
        return
    
    # Encontrando o lado que representa a hipotenusa (lado mais longo)
    hipotenusa = max(a, b, c)
    
    # Usando um loop para imprimir o triângulo retângulo
    for i in range(1, hipotenusa + 1):
        linha = ''
        for j in range(1, i + 1):
            if i <= min(a, b):
                linha += '* '
            else:
                linha += '  '
        print(linha)

# Exemplo de uso
triangulo_retangulo(5, 3, 4)
