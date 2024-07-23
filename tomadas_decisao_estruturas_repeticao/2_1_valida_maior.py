"""
1. Faça um Programa que peça dois números e imprima o maior deles.
"""

print("- - - PROGRAMA: Qual dos dois é o maior? - - - \n")

try:
    primeiro_numero = float(input("Por favor insira o primeiro número: "))

    segundo_numero = float(input("Por favor insira o segundo número: "))

    if primeiro_numero > segundo_numero:
        print(f"O número {primeiro_numero :.2f} é maior.")
        
    elif primeiro_numero < segundo_numero:
        print(f"O número {segundo_numero :.2f} é o maior.")
        
    elif primeiro_numero == segundo_numero:
        print("Os números são iguais.")
        
except ValueError:
    print("Valor inválido! É preciso que seja um valor numérico.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")