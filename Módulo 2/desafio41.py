import datetime
anoatual = datetime.date.today().year
ano = int(input('Digite o ano do seu nascimento: '))
delta = anoatual - ano
if delta < 9:
    print(' Categoria: MIRIM')
elif 9 <= delta < 14:
    print(' Categoria: INFANTIL')
elif 14 <= delta < 19:
    print(' Categoria: JUNIOR')
elif 19 <= delta < 20:
    print(' Categoria: SÊNIOR')
else:
    print(' Categoria: MASTER')
