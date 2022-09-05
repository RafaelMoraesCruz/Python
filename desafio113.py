def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mErro!! por favor digite um número válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mErro!! por favor digite um número válido!\033[m')
            continue
        else:
            return n 


num = leiaint('Digite um valor: ')
print(f'O valor digitado foi {num}')
