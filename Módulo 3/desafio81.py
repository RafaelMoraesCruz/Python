lista = []
c = 0
while True:
    n = int(input('Digite um número: '))
    c += 1
    lista.append(n)
    escolha = str(input('Deseja continuar? (n para parar): '))
    if escolha in 'Nn':
        break
print(f'Foram digitados {c} números')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O número 5 está presente na lista!')
else:
    print('O número 5 não está presente na lista!')
