"""
8. Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado.
"""

try:
    
    primeiro_valor = float(input("Digite o primeiro número: "))
    segundo_valor = float(input("Digite o segundo número: "))
    terceiro_valor = float(input("Digite o terceiro número: "))
    
    if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
        print(f"O número {primeiro_valor} é o maior.")
    elif primeiro_valor < segundo_valor and segundo_valor > terceiro_valor:
        print(f"O número {segundo_valor} é o maior.")
    elif terceiro_valor > segundo_valor and primeiro_valor < terceiro_valor:
        print(f"O número {terceiro_valor} é o maior.")
    elif terceiro_valor == segundo_valor and primeiro_valor == terceiro_valor:
        print("Os valores digitados são iguais.")
    
except ValueError:
    print("O valor é inválido.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")