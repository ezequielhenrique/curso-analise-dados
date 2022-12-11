import math


class Ponto():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distancia(self, ponto):
        return math.sqrt((ponto.x - self.x)**2 + (ponto.y - self.y)**2)

    def quadrante(self):
        if self.x > 0 and self.y > 0:
            return 1
        elif self.x < 0 and self.y > 0:
            return 2
        elif self.x < 0 and self.y < 0:
            return 3
        elif self.x > 0 and self.y < 0:
            return 4
        else:
            return 0


class Circunferencia():
    def __init__(self, ponto, raio):
        self.centro = ponto
        self.raio = raio

    def pertence(self, p):
        if self.centro.distancia(p) <= self.raio:
            return True
        else:
            return False


print('Cordenadas do ponto 1:')
x1 = int(input('x: '))
y1 = int(input('y: '))

print('Cordenadas do ponto 2:')
x2 = int(input('x: '))
y2 = int(input('y: '))

ponto1 = Ponto(x1, y1)
ponto2 = Ponto(x2, y2)

print(f'Quadrante do ponto 1: {ponto1.quadrante()}º')
print(f'Quadrante do ponto 2: {ponto2.quadrante()}º')

dist = ponto1.distancia(ponto2)
print(f'A distância entre os pontos é {dist:.2f}')

c = Circunferencia(ponto1, 2)
respo = c.pertence(ponto2)
print(respo)
