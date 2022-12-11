import math

def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print('Cordenadas do ponto 1:')
x1 = int(input('x: '))
y1 = int(input('y: '))

print('Cordenadas do ponto 2:')
x2 = int(input('x: '))
y2 = int(input('y: '))

print(f'A distãncia entre os pontos é {distancia(x1, y1, x2, y2):.2f}')
