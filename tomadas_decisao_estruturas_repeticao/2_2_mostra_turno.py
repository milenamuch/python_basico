"""
2. Faça um Programa que pergunte em que turno você estuda. Peça para
digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom
Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

try:
    turno = input("""
    Olá! Em qual turno você estuda?
    [M] para matutino,
    [V] para vespertino,
    [N] para noturno: 
    """)

    turno = turno.upper()

    if len(turno) > 1:
        print("Você precisa digitar apenas a letra correspondente ao seu turno: M, V ou N.")

    elif turno != 'M' and turno != 'V' and turno != 'N':
        print("Você precisa digitar apenas a letra correspondente ao seu turno: M, V ou N.")
        
    elif turno == 'M':
        print("Bom dia!")
        
    elif turno == 'V':
        print("Boa tarde!")
        
    elif turno == 'N':
        print("Boa noite!")

except ValueError:
    print("Valor inválido.")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")


