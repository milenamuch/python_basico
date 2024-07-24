"""
6. Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre-se que ao
informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas.
"""

try:
    
    nome = input("Por favor, digite o seu nome: ")
    
    if len(nome) < 2:
        print("O seu nome precisa conter mais de dois caracteres.")
    else:  
        nome = nome.upper()
        nome_invertido = nome[::-1]
        
        print(nome_invertido)
    
except ValueError:
    print("Valor inválido.")