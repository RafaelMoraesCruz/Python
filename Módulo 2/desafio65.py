min = 9999999999999
d1 = 'S'
n2 = a = med = max = 0
while d1 == 'S':
    n1 = float(input('Digite um número: '))
    a += 1
    n2 += n1
    med = n2 / a
    if n1 > max:
        max = n1
    if n1 < min:
        min = n1
    d1 = str(input('Quer continuar? [S/N] ')).upper().strip()
print(f'Você digitou {a} números e a média foi {med} ')
print('O maior valor foi {} e o menor foi {} '.format(max, min))
