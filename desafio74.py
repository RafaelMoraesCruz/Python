import random
lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
valoressortidos = (random.choice(lista), random.choice(lista), random.choice(lista), random.choice(lista), random.choice(lista))
print(f'Os valores sorteados foram: {valoressortidos}')
print(f'o maior valor sorteado foi: {max(valoressortidos)}')
print(f'o menor valor sorteado foi: {min(valoressortidos)}')
