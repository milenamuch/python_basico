"""
3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
mensagem caso o valor seja inválido e continue pedindo até que o usuário
informe um valor válido.
"""

try:

    while True:
        nota = int(input("Por favor, digite uma nota entre zero e dez: "))

        if nota > 10 or nota < 0:
            
            print("A nota precisa ser maior que 0 e menor que 10.\n")
            continue
        
        else:
            print(f"Você digitou a nota {nota}.")
            break
        
except ValueError:
    print("Valor inválido.")