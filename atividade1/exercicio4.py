soma_idade = qtd = idade = 0

while idade >= 0:
    idade = int(input('Idade: '))

    if idade < 0:
        break

    soma_idade += idade
    qtd += 1

print(f'A media de idade do grupo é de {soma_idade/qtd:.2f} anos')
