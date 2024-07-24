"""
Faça um Programa que utilize 4 variáveis como preferir e no final print
uma mensagem amigável utilizando as variáveis criadas.
"""
from time import sleep

def input_tratado(mensagem, tipo="texto"):
    while True:
        entrada = input(mensagem)
        if not entrada:
            print("Ops... Este campo não pode estar vazio.")
        elif tipo == "texto" and not entrada.replace(" ", "").isalpha():
            print("Entrada deve conter apenas letras.")
        elif len(entrada) <= 2:
            print("O valor precisa conter 3 ou mais caracteres.")
        else:
            return entrada
try:
    print("- - - VAMOS CRIAR UMA PERSONAGEM DE CONTOS DE FADA - - -")


    local = input_tratado("Digite um local (Ex: floresta): ")
    nome_feminino = input_tratado("Digite um nome feminino: ")
    cor = input_tratado("Digite uma cor: ")
    animal = input_tratado("Digite um animal: ")

    print("Construindo seu personagem...")

    print(3)
    sleep(1)
    print(2)
    sleep(1)
    print(1)
    sleep(1)


    print(f"""Em um(a){local} muito distante, havia uma princesa chamada {nome_feminino}. Ela usava um vestido {cor}, que é a sua cor favorita, e seu animal de estimação era um {animal}.""")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")