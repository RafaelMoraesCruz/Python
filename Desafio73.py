tabela = ('atletico-mg', 'flamengo', 'palmeiras', 'fortaleza', 'corinthans', 'bragantino', 'fluminense',
          'america-mg', 'atletico-go', 'santos', 'ceara sc', 'internacional', 'sao paulo', 'athletico-pr',
          'cuiaba', 'juventude', 'gremio', 'bahia', 'sport recife', 'chapecoense')
print('a tabela está desse jeito:', end=' ')
print(tabela)
print(f'Os 5 primeiros colocados sâo: {tabela[0: 5]}')
print(f'Os 4 últimos colocados são{tabela[16:20]}')
print(f'A lista em ordem alphabética é: {sorted(tabela[:])}')
print(f'A posição da chapecoense é : {tabela.index("chapecoense") + 1}')

