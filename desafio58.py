import random
lista = [0, 1, 2 , 3 ,4 ,5 ,6 ,7 ,8 ,9 , 10]
a = random.choice(lista)
c = 11
r = 0
while c != a:
    c = int(input(('Digite um número inteiro: ')))
    r += 1
    if c != a:
        print('tente novamente, os números não correspondem!')
if c == a:
    print('O número escolhido foi o mesmo sorteado do computador que foi {}!!!'.format(a))
print('Você tentou {} vezes antes de acertar.'.format(r))