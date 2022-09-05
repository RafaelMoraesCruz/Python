v = int(input('Digite a velocidade do carro: '))
if v>80:
    m=7*(v-80)
    print('a multa vai ser de R${}'.format(m))
else:
    print('a velocidade está nos limites permitidos pelo trecho, o senhor(a) não irá ser multado! ')
