"""
5. Crie uma função chamada contar_vogais que recebe uma string como parâmetro. 
Implemente a lógica para contar o número de vogais na string e retorne o total de vogais. 
Solicite ao usuário para inserir uma frase e utilize a função para contar as vogais.
"""

def contar_vogais(frase):
    vogais = ['a', 'e', 'i', 'o', 'u']
    conta_vogais = 0
    frase.split()
    for letra in frase:
        if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
            conta_vogais += 1
        
    return conta_vogais

frase_usuario = input("Insira a sua frase para contarmos a quantidade de vogais. ")

resultado = print(f"A sua frase contém {contar_vogais(frase_usuario)}")