import time


def contador(a, b, c):
    print(f'Contagem de {a} até {b} de {c} a {c}')
    for p in range(a, b, c):
        print(p, end=' ')
        time.sleep(0.3)
    print('')


contador(1, 10, 1)
contador(10, 0, -2)
a = int(input('Digite o número inicial: '))
b = int(input('Digite o número final: '))
c = int(input('Progressão: '))
contador(a, b, c)



