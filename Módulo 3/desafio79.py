lista = []
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    a = str(input('Deseja continuar? digite ''n'' para parar! : '))
    if a in 'Nn':
        break
lista.sort()
print(lista)
