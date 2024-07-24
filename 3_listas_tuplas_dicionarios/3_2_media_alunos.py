"""
2. 
- Faça um Programa que peça as quatro notas de 5 alunos, 
- calcule e armazene numa lista a média de cada aluno,
- imprima o número de alunos com média maior ou igual a 7.0.
"""

try:
    alunos = [
        'Maria',
        'João',
        'Ana',
        'Pedro',
        'Joana'
    ]
    
    medias = []
    
    for aluno in alunos:
        nota = 0
        for i in range(4): #para cada aluno da minha lista de alunos, eu vou digitar 4 notas, por isso o range(4)
            nota_aluno = float(input(f"Por favor digite a nota de {aluno}: "))
            nota = nota + nota_aluno
            
        media = nota / 4
        medias.append(media)
    
    
    media_maior_que_sete = []
    
    for m in medias:
        if m >= 7.0:
             media_maior_que_sete.append(m)
             
    print(f"O número de alunos com média maior do que 7.0 é: {len(media_maior_que_sete)}")
            
except ValueError:
    print("Valor inválido.")
    
except Exception as e:
    print(f"Ocorreu um erro: {e}")