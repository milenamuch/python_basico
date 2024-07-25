"""
2. Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
"""

def inverte_valor(valor):
    int_para_string = str(valor)
    valor_invertido = int_para_string[::-1]
    string_para_int = int(valor_invertido)
    
    return string_para_int
    
    
numero = 123456789

resultado = inverte_valor(numero)


print(f"O número {numero} invertido é: {resultado}")