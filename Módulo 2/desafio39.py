import datetime
year = datetime.date.today().year
ano = int(input('Digite o ano de nascimento: '))
idade = (year - ano)
if idade < 18 :
    print('O senhor so tem {}, irá precisar se alistar quando fizer 18 anos!!'.format(idade))
elif idade == 18 :
    print('O senhor possui idade de alistamento, por favor realizar o cadastro para o seu alistamento!! ')
else:
    print('O senhor ja passou da idade de alistamento!')
