n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
if m < 5.0:
    print ('REPROVADO!')
elif 5.0 <= m <7.0:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
