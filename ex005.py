d = int(input('Digite a distância da viagem em kilometros: '))
if d<=200:
    d1=d*0.5
    print('O valor da passagem vai ficar: {}'.format(d1))
else:
    d2=d*0.45
    print('O valor da passagem vai ficar: {}'.format(d2))
