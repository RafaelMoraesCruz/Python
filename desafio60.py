n = int(input('Digite um número: '))
a = n - 1
f = 0
while a != 0:
    r = a * n
    print('{} * {} = {}'.format(n, a, r))
    a += - 1
    f += r
print('Resultado do fatorial de {} é: {}'.format(n, f))
