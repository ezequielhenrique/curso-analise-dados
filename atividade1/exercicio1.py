pares = 0

for i in range(5):
    num = int(input('Digite um número inteiro: '))

    if num % 2 == 0:
        pares += 1

print(f'Foram digitados {pares} números pares')
