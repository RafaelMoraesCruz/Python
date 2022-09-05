from random import choice
print('========== JOKENPÔ ==========')
LISTA = choice(['PEDRA', 'PAPEL', 'TESOURA'])
escolha = input('Escolha entre PEDRA, PAPEL E TESOURA e digite a opção escolhida: ')
print('Você escolheu {}'.format(escolha))
print('O computador escolheu: {}' .format(LISTA))
if escolha == 'PEDRA' and LISTA == 'PAPEL':
    print('O Computador ganhou!!')
elif escolha == 'PAPEL' and LISTA == 'TESOURA':
    print('O Computador ganhou!!')
elif escolha == 'TESOURA' and LISTA == 'PEDRA':
    print('O Computador ganhou!!')
elif escolha == 'TESOURA' and LISTA == 'PAPEL':
    print('Você ganhou!!')
elif escolha == 'PEDRA' and LISTA == 'TESOURA':
    print('Você ganhou!!')
elif escolha == 'PAPEL' and LISTA == 'PEDRA':
    print('Você ganhou!!')
else:
    print('EMPATE')

