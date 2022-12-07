def valorPagamento(valor_prestacao, dias_atraso):
    valor = 0
    if dias_atraso == 0:
        valor = valor_prestacao
    else:
        valor = valor_prestacao + (valor_prestacao*0.03) + (valor_prestacao*0.001*dias_atraso)

    return valor


valores = list()

while True:
    valor_prestacao = float(input('Valor da prestação: '))
    if valor_prestacao == 0:
        break

    dias_atraso = int(input('Dias de atraso: '))

    valor = valorPagamento(valor_prestacao, dias_atraso)

    valores.append(valor)
    print(f'O valor a ser pago é R$ {valor:.2f}')

print('========== RELATÓRIO DO DIA ==========')
print(f'Quantidade de prestações: {len(valores)}')
valor_total = 0
for i in valores:
    valor_total += i
print(f'O valor total das prestações é R$ {valor_total:.2f}')
