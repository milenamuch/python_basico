"""
4. Crie um programa que leia quanto dinheiro uma pessoa tem na
carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
Considere a tabela de conversão abaixo:
    Dólar Americano: R$ 4,91
    Peso Argentino: R$ 0,02
    Dólar Australiano: R$ 3,18
    Dólar Canadense: R$ 3,64
    Franco Suiço: R$ 0,42
    Euro: R$ 5,36
    Libra esterlina: R$ 6,21
"""

def converte_moedas(valor):
    
    taxas_cambio = {
        "Dólar" : 4.91,
        "Peso Argentino" : 0.02,
        "Dólar Australiano" : 3.18,
        "Dólar Canadense": 3.64,
        "Franco Suíço" : 0.42,
        "Euro" : 5.36,
        "libra Esterlina": 6.21
    }
    
    valores_convertidos = {}
    
    for moeda, taxa in taxas_cambio.items():
        conversao = valor / taxa
        valores_convertidos[moeda] = conversao
    
    return valores_convertidos
        

try:
    dinheiro = float(input("Por favor, insira quanto você tem em reais na carteira. Lembre-se de utilizar o '.' no lugar da vírgula: "))
    print(f"Você tem em sua carteira R$ {dinheiro}")
    resposta = converte_moedas(dinheiro)

    print("E para cada moeda os valores serão mostrados abaixo:")
    for moeda, valor_convertido in resposta.items():
        print(f"{moeda}: {valor_convertido:.2f}")

except ValueError:
    print("Valor inválido.")
