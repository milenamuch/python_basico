"""
Solicite ao usuário o peso em kg e a altura em metros. 
Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).
"""

try:
    altura = float(input("Digite a sua altura em metros: "))
    peso = int(input("Digite o seu peso: "))

    if altura <= 0 or peso <= 0: 
            raise ValueError("O valor deve ser positivo.")
        
    imc = int(peso / (altura * altura))
        
    if imc <= 16:
        print(f"O seu imc é de {imc}, você possui magreza grave.")
    elif imc >= 16 and imc <= 16.9:
        print(f"O seu imc é de {imc}, você possui magreza moderada.")
    elif imc >= 17 and imc <= 18.5:
        print(f"O seu imc é de {imc}, você possui magreza leve.")
    elif imc >= 18.6 and imc <= 24.9:
        print(f"O seu imc é de {imc}, você está no peso ideal.")
    elif imc >= 25 and imc <= 29.9:
        print(f"O seu imc é de {imc}, você possui sobrepeso.")
    elif imc >= 30 and imc <= 34.9:
        print(f"O seu imc é de {imc}, você possui obesidade grau I.")
    elif imc >= 35 and imc <= 39.9:
        print(f"O seu imc é de {imc}, você possui obesidade grau II ou severa.")
    elif imc >= 40:
        print(f"O seu imc é de {imc}, você possui obesidade grau III ou mórbida.")

except ValueError as value:
    print(f"Entrada inválida: {value}")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
