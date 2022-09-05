import time


def maior(* num):
    cont = 0
    print('Analisando os valores passados:')
    time.sleep(2)
    for n in num:
        print(f'{n}', end=' ')
        cont += 1
    print(f'\n O Maior valor é de:{max(num)} e foram informados {cont} valores')


maior(8, 7, 2, 1, 10, 3, 5)
maior(2, 3)
maior(9, 3, 6, 8, 1, 10, 98, 100, 55, 54, 53, 24)