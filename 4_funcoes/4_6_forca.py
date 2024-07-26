"""
6. Vamos construir um jogo de forca. 
O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. - FEITO!
A palavra secreta será representada por espaços em branco, um para cada letra da palavra. - FEITO!
O jogador terá um número limitado de 6 tentativas. - FEITO!
Em cada tentativa, o jogador pode fornecer uma letra. - FEITO!
Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. 
Se a letra não estiver na palavra, uma mensagem de erro deverá ser informada. - FEITO!
Após um número máximo de erros, o jogador perde. 
O jogo continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.

Dica: Você precisará importar uma biblioteca para resolver esse exercício
"""
import random

# - - - DECLARAÇÃO DE VARIÁVEIS - - - 
palavras = [
    "amorosa",
    "autoconfiante",
    "bondosa",
    "carinhosa",
    "criativa",
    "confiante",
    "corajosa",
    "decidida",
    "dedicada",
    "determinada",
    "elegante",
    "energizante",
    "feliz",
    "forte",
    "generosa",
    "harmoniosa",
    "inteligente",  
    "incrível",
    "legal",
    "linda",
    "maravilhosa",
    "persistente",
    "próspera",
    "resiliente",
    "talentosa",
]

palavra_escolhida = random.choice(palavras)
palavra_escondida = [" "] * len(palavra_escolhida)
tentativas_letras = []
tentativas = 6

# - - - INTRODUÇÃO AO JOGADOR E REGRAS - - - 
print("- - - Seja bem vindo(a) ao jogo da forca das palavras positivas! - - - ")
print("A palavra da forca, completará ao final a frase: 'Você é uma pessoa ________!' ")
print("Regras do jogo: \n"
        "-> Você tem direito a 6 tentativas \n"
        "-> Você só pode digitar uma letra por vez \n"
        "Boa sorte!")

while True: #O jogador terá um número limitado de 6 tentativas.

    letra = input("Por favor digite a letra: ")
    letra = letra.lower() #Para deixar todas as letras digitas em minúsculo para facilitar a comparação
    
    # - - - VALIDAÇÕES DE USO - - -
    
    if len(letra) > 1: #Em cada tentativa, o jogador pode fornecer uma letra.
        print("Erro: Você só poderá digitar uma letra por vez. ")
        continue
    
    elif letra.isdigit():
        print("Erro: Você só pode digitar letras.")
        continue
    
    elif letra in tentativas_letras:
        print(f"Você já digitou a letra {letra}, por favor, tente novamente. ")
        continue
    
    tentativas_letras.append(letra)

    # - - - VALIDAÇÃO DA PALAVRA E ERROS - - - 
    if letra in palavra_escolhida:
            for i in range(len(palavra_escolhida)):
                if palavra_escolhida[i] == letra:
                    palavra_escondida[i] = letra
            print("".join(palavra_escondida))
            
    else:
        print("Desculpe, esta letra não está na palavra.")
        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}\n")
        
    # - - - FINALIZAÇÃO DO JOGO - - - 
    if " " not in palavra_escondida:
        print(f"Parabéns! Você ganhou! A palavra era '{palavra_escolhida}'.")
        print(f"Aqui está a frase: Você é uma pessoa {palavra_escolhida}!")
        break
    elif tentativas == 0:
        print(f"Que pena! Você perdeu! A palavra era '{palavra_escolhida}'.")
        break

    