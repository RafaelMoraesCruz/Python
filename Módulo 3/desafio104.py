def leiaint(n):
    while True:
        n = input('Digite um número: ')
        a = n.isnumeric()
        if a == False:
            print('\033[1;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO!!\033[m')
        else:
            print(f'Você acabou de digitar o número: {n}')
            break


n = leiaint('Digite um número: ')
