print('Desafio da PA')
r = int(input('Digite a razão da PA: '))
n = int(input('Digite o primeiro número da PA: '))
d = n + 10 * r
print('O 1 número é: {}'.format(n))
for c in range(n, d, r) :
    print('{}'. format(c), end='----')

