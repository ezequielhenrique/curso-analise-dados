def calculaSalario(salario_bruto):
    salario_liquido = salario_bruto - (salario_bruto*0.11)
    salario_liquido -= salario_liquido*0.15

    return salario_liquido


salario = float(input('Digite o valor do salário: '))
print(f'O valor do salário com descontos é {calculaSalario(salario):.2f}')
