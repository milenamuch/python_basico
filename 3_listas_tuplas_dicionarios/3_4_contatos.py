"""
4. Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome.
"""

try:
    
    contatos = {
        "Maria": "(93) 3458-4231",
        "João": "(53) 3648-3903",
        "Alice": "(12) 3708-3522",
        "Pedro": "(85) 3671-4434",
        "Sofia": "(82) 2564-8513",
        "Victor": "(69) 2349-9531",
        "Clarice": "(84) 3787-6839",
        "Rafael": "(16) 2046-8447",
        "Melissa": "(47) 3622-1513",
        "Marcos": "(66) 3345-4106",
    }

    nome_contato = input("Por favor, digite o nome do contato que você está procurando: ")
     
    if nome_contato in contatos:
        print(f"O telefone de {nome_contato} é: {contatos[nome_contato]}")
    elif len(nome_contato) < 2:
        print("O nome precisa ter mais de 2 caracteres.")
    elif nome_contato.isdigit:
        print("O nome do contato precisa conter somente letras.")
    else:
        print("Contato não encontrado.")
    
except ValueError:
    print("Valor inválido.")
