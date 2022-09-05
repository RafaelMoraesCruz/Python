from random import choice
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = 0
while True:
    a = choice(lista)
    n1 = int(input('Digite um valor: '))
    e = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
    if (n1 + a) % 2 == 0 and e =='P':
        print(f'Voce venceu, o computador jogou {a} e você jogou {n1},tente novamente')
        r += 1
        print('-' * 20)
    else:
        print(f'Voce perdeu, o computador jogou {a} e você jogou {n1}!')
        print('-' * 20)
        break
print(f'Você venceu {r} vezes consecutivas')
