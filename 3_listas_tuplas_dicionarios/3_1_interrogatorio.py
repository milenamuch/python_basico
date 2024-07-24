"""
1. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    ""Telefonou para a vítima?""
    ""Esteve no local do crime?""
    ""Mora perto da vítima?""
    ""Devia para a vítima?""
    ""Já trabalhou com a vítima?""
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como ""Suspeita"", entre 3 e 4 como ""Cúmplice"" e 5 como
""Assassino"".

- 2 questões : Suspeita,
- 3 e 4 questões: Cúmplice,
- 5: Assassino
Caso contrário,ele será classificado como""Inocente"".
"""

try:
    
    perguntas_interrogatorio = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]
    
    resposta_positiva = 0
    
    for pergunta in perguntas_interrogatorio:
        
        print(pergunta)
        resposta = (input("Digite 'S' para sim e 'N' para não: "))
        resposta = resposta.upper()
        
        if resposta == "S":
            resposta_positiva += 1
            
        elif resposta == "N":
            pass
        
        else:
            print("Digite um valor válido. ")
            break
    else:
        
        if resposta_positiva == 2:
            print("Você é suspeito pelo crime.")
            
        elif resposta_positiva >= 3 and resposta_positiva <= 4:
            print("Você é cúmplice do crime!")
            
        elif resposta_positiva == 5:
            print("Prendam ele! É o assassino!")
            
        else:
            print("Você é inocente.")
            
except ValueError:
    print("Valor inválido. ")
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")