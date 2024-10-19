def contar_palavras(texto):
    # Converter todas as palavras para minúsculas
    texto = texto.lower()
    # Dividir o texto em palavras
    palavras = texto.split()
    # Inicializar um dicionário para contar as palavras
    contagem = {}
    # Contar as ocorrências de cada palavra
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

# Exemplo de uso:
texto = "Python é uma linguagem de programação Python"
print(contar_palavras(texto))  
# Saída esperada: {'python': 2, 'é': 1, 'uma': 1, 'linguagem': 1, 'de': 1, 'programação': 1}

       




       
