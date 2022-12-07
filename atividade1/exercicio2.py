hora_inicial = int(input('Hora inicial: '))
while hora_inicial < 0 or hora_inicial > 24:
    print('Hora inválida, digite novamente')
    hora_inicial = int(input('Hora inicial: '))

minuto_inicial = int(input('Minuto inicial: '))
while minuto_inicial < 0 or minuto_inicial > 59:
    print('Minuto inválido, digite novamente')
    minuto_inicial = int(input('Minuto inicial: '))

hora_final = int(input('Hora final: '))
while hora_final < 0 or hora_final > 24:
    print('Hora inválida, digite novamente')
    hora_final = int(input('Hora final: '))

minuto_final = int(input('Minuto final: '))
while minuto_final < 0 or minuto_final > 59:
    print('Minuto inválido, digite novamente')
    minuto_final = int(input('Minuto final: '))

minuto_inicial += hora_inicial*60
minuto_final += hora_final*60

tempo_total = minuto_final - minuto_inicial

if tempo_total <= 0:
    tempo_total += 1440

horas = tempo_total // 60
minutos = tempo_total % 60


print(f'O jogo durou {horas} horas e {minutos} minutos')
