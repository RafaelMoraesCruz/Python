lista = []
par = []
impar = []
while True:
    lista.append(int(input('Digite um número: ')))
    escolha = str(input('Deseja continuar: [S/N]'))
    if escolha in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(lista)
print(par)
print(impar)