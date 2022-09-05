print('DESAFIO DOS NUMEROS INTEIROS')
s = 0
for c in range (1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s = s + n
    else:
        print('Número é ímpar e não será somado. ')
print('a soma total dos números inteiros pares é: {} '.format(s))
