"""
Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.
"""
def calcula_queima_calorias(horas_exercicio):
    
    conversao_para_minutos = horas_exercicio * 60
    queima_de_calorias = conversao_para_minutos * 5
    queima_no_mes = queima_de_calorias / 30
    
    return float(queima_no_mes)

try:
    qtde_horas_exercicio = int(input("Quantas horas você se exercita por semana? "))

    if qtde_horas_exercicio <= 0:
        print("O valor não pode ser igual ou menor que zero.")
        
    else:
        resultado = calcula_queima_calorias(qtde_horas_exercicio)

        print(f" Você queimou{resultado: .2f} calorias.")
    
except ValueError:
    print("O valor precisa ser um número inteiro.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")