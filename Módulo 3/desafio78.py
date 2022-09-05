lista = []
c = 0
while True:
    if c != 5:
        n1 = int(input('Digite um valor: '))
        lista.append(n1)
        c += 1
    elif c == 5:
        break
print(lista)
print(f'O maior valor foi: {max(lista)} com posição {lista.index(max(lista))} e o menor valor foi: {min(lista)} na posição: {lista.index(min(lista))}')