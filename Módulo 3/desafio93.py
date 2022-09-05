#desafio 93
import time
dicionario = dict()
listadegols = []
listainfo = []
dicionario['jogador'] = str(input('Digite o nome do jogador: '))
dicionario['jogos'] = int(input('Digite quantos jogos: '))
for i in range(0, dicionario['jogos']):
    listadegols.append(int(input(f'Quantos gols ele fez na {i} partida? ')))
dicionario['gols'] = listadegols
dicionario['total de gols'] = sum(listadegols)
print(dicionario)
print('_' * 25)
for k, v in dicionario.items():
    print(f'O campo {k} tem o valor {v}')
print('_' * 25)
for c in range(0, dicionario['jogos']):
    print(f'Na partida {c}, fez {listadegols[c]}')
    time.sleep(1)
print('FINAL DA QUESTÃO')
