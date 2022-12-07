senha_correta = 2002

senha_digitada = int(input('Digite a senha: '))

while senha_digitada != senha_correta:
    print('Senha inválida!')
    senha_digitada = int(input('Digite a senha: '))

print('Acesso permitido!')
