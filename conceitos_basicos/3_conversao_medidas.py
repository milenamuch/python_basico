"""
3. Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros
"""
try:
    quilometros = float(input("Digite a quantidade de quilômetros: "))

    metros = quilometros * 1000
    centimetros = quilometros * 100000
    milimetros = quilometros * 1000000

    print(f"{quilometros} quilômetros é igual a:")
    print(f"{quilometros}km, é igual a {metros}m")
    print(f"{quilometros}km, é igual a {centimetros}cm")
    print(f"{quilometros}km, é igual a {milimetros}mm")

except ValueError:
    print("O valor inserido é inválido.")
