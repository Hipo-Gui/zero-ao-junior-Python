import random
import string

def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

def main():
    comprimento = int(input("Digite o comprimento da senha desejada: "))
    senha_gerada = gerar_senha(comprimento)
    print(f"A senha gerada é: {senha_gerada}")

if __name__ == "__main__":
    main()