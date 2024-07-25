"""
3. Escreva um script que pergunta ao usuário se ele deseja converter
uma temperatura de grau Celsius para Fahrenheit ou vice-versa. 
Para cada opção, crie uma função.

Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
desejada, onde esse menu chama a função de conversão correta.
"""

def celsius_para_fahrenheit(valor_celsius):
    conversao = (valor_celsius * 9/5) + 32
    return conversao

def fahrenheit_para_celsius(valor_fahrenheit):
    conversao = (valor_fahrenheit -32) * 9/5
    return conversao

def menu_usuario(escolha, valor_temperatura):
    
    escolha = escolha.upper()
    
    if escolha == 'C':
        return fahrenheit_para_celsius(valor_temperatura)
        
    elif escolha == 'F':
        return celsius_para_fahrenheit(valor_temperatura)
        
    else:
        print("Valor inválido.")
        
    
try:
    print("Bem vindo ao conversor de temperaturas!")
    entrada_menu = input("Qual é a sua escolha? Para converter uma temperatura para Celsius digite 'C' e para converter para Fahrenheit digite 'F': ")
    entrada_menu = entrada_menu.upper()

    if entrada_menu == 'F':
        entrada_temperatura = float(input("Agora digite a temperatura em Fahrenheit a ser convertida para Celsius: "))
        resposta = menu_usuario(entrada_menu, entrada_temperatura)
        print(f"O valor {entrada_temperatura}°F convertido é: {resposta}°C")    

    if entrada_menu == 'C':
        entrada_temperatura = float(input("Agora digite a temperatura em Celsius a ser convertida para Fahrenheit: "))
        resposta = menu_usuario(entrada_menu, entrada_temperatura)
        print(f"O valor {entrada_temperatura}°C convertido é: {resposta}°F")    

except ValueError:
    print("Valor inválido.")
    
    
    