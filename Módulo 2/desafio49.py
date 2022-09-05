print('DESAFIO TABUADA COM FOR')
n = int(input('Digite um número entre 1 e 10 para saber sua tabuada: '))
for c in range (1, 11):
    s = n * c
    print('{} * {} = {}'.format(n, c, s))
