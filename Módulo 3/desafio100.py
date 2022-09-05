import time
from random import randint
listapar = list()
lista = list()

def sorteia(lista):
    print('Sorteando 5 valores da lista: ')
    for n in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ', flush=True)
        time.sleep(0.4)
    print(f'\nSorteando os 5 valores da lista: {lista}')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            listapar.append(valor)
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma} dos valores {listapar}')


sorteia(lista)
somapar(lista)
