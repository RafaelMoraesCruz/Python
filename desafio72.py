tupla = ('zero','um' , 'dois','três', 'quatro', 5, 6, 7, 8, 9, 10, 11 ,12 ,13, 14 ,15, 16, 17, 18, 19, 20)
while True:
    numerodigitado = int(input('Digite um número de 0 a 20: '))
    if 20 >= numerodigitado >= 0:
        print(f'Você digitou o número {tupla[numerodigitado]}')
        break
    else:
        print(f'O número {numerodigitado} é invalido, tente novamente')
# VER COMO COLOCAR EM EXTENSO!!


