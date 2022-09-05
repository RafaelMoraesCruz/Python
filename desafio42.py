r1 = float(input('Digite o comprimento do primeiro segmento de reta: '))
r2 = float(input('Digite o comprimento do segundo segmento de reta: '))
r3 = float(input('Digite o comprimento do terceiro segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('O triângulo existe!!')
    if r1 == r2 and r2 == r3:
        print('O triângulo é equilátero')
    elif r1 == r2:
         print('O triângulo é isósceles')
    elif r2 == r3:
        print('O triângulo é isósceles')
    elif r3 == r1:
        print('O triângulo é isósceles')
    else:
            print('O triângulo é escaleno')
else:
    print('As retas não conseguem formar um triângulo! ')
