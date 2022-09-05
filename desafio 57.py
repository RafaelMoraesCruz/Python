c = ''
while c != 'M' and c != 'F':
    c = str(input('Digite seu sexo: ')).upper().strip()
    if c != 'M' and c != 'F':
        print('Digite seu sexo novamente')
if c == 'M':
    c = 'M'
    print('Seu sexo é masculino')
elif c == 'F':
    c = 'F'
    print('Seu sexo é feminino')