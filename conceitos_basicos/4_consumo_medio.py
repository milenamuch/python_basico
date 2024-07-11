"""
4. Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.
"""

litros = int(input("Quantos litros de combustível você consumiu neste percurso? "))
distancia = int(input("Qual foi a distância percorrida? "))

media = distancia/litros

print(f"O seu veículo fez uma média de {media}km/L")