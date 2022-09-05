import datetime
jovem = 0
adultas = 0
for c in range(0, 7):
    n = int(input('Digite o ano de nascimento da pessoa: '))
    if  datetime.date.today().year - n >= 18:
        adultas += 1
    else:
        jovem += 1
print('Temos {} pessoas jovens no grupo e {} pessoas adultas no grupo!!'.format(jovem, adultas))
