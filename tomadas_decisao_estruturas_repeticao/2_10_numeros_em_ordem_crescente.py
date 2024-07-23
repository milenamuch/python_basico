"""
10. Faça um programa que lê três números inteiros e os mostra em ordem crescente.
"""

try:
    numeros = []
    
    for i in range(3):
        entrada_numeros = int(input("Digite o número: "))
        numeros.append(entrada_numeros)

    print(f"Os números em ordem ficam: {sorted(numeros)}")
    
except ValueError:
    print("Valor inválido.")

except Exception as e:
    print("Ocorreu um erro: {e}.")