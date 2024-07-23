"""
6. Crie um programa que solicite ao usuário um login e uma senha. O
programa deve permitir o acesso apenas se o usuário for "admin" e a senha
for "admin123", caso contrário imprima uma mensagem de erro.

"""
try:
    usuario = input('Digite seu nome de usuário: ')
    senha_digitada = input('Digite sua senha: ')

    usuario_permitido = "admin"
    senha_permitida = "admin123"

    if usuario == usuario_permitido and senha_digitada == senha_permitida:
        print('Você entrou no sistema!')
    else:
        print('ERRO: Seu usuário ou senha estão incorretos.')
    
except Exception as e:
    print("Ocorreu um erro: {e}")

