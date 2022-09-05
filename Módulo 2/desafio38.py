n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
if n1 > n2 :
    print('{} é maior do que {}'.format(n1, n2))
elif n2 > n1 :
    print('{} é maior do que {}'.format(n2, n1))
else :
    print('Os valores {} e {} são iguais, não existe maior valor!!'.format(n1, n2))
print('Os valores foram comparados com sucesso')
