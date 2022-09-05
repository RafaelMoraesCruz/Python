from tkinter import END


media = 0
maioridade = 0
nomemaioridade = ''
mulhermenos20 = 0
for c in range(1, 6):
    print('----- {} PESSOA-----'.format(c))
    n = input('Digite o seu nome: ').strip()
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite F para mulher e M para homem: ').strip().upper()
    media = (media * (c - 1) + idade)/c
    print(media)
    if idade > maioridade:
        maioridade = idade
        nomemaioridade = n
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1
print('A média de idade do grupo é de {:.2f} anos'.format(media))
print('a pessoa mais velha tem {} anos e se chama {}.'.format(maioridade, nomemaioridade))
print('Ao todo são {} com menos de 20 anos'.format(mulhermenos20))
