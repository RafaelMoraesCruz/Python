import random
lista = [0,1,2,3,4,5]
escolhaPC = random.choice(lista)
escolha = int(input('Digite um número entre 0 e 5: '))
if escolha == escolhaPC:
    print('O número escolhido foi igual ao sorteado pelo computador!! ')
else:
    print('O número não foi o mesmo do que o computador!!')
print('Seu número foi: {}'.format(escolha))
print('O número sorteado pelo computador foi: {}'.format(escolhaPC))