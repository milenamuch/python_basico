"""
2. Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.
"""


ano = int(input('Digite seu ano de nascimento: '))

calculo_idade_com_aniversario = 2024 - ano
calculo_idade_sem_aniversario = 2023 - ano

print(f'Se você já fez aniversário neste ano então a sua idade é: {calculo_idade_com_aniversario}')
print(f'Se você ainda não fez aniversário neste ano então a sua idade é: {calculo_idade_sem_aniversario}')