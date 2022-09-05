n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro valor inteiro: '))
t = 0
while True:
    s = n1 + n2
    mult = n1 * n2
    maior = max(n1, n2)
    print('Digite [1] para mostrar a soma')
    print('Digite [2] para mostrar a multiplicação')
    print('Digite [3] para mostrar o maior dos números')
    print('Digite [4] para escolher novos números')
    print('Digite [5+] para finalizar os programas')
    print('')
    t = int(input('Digite um número para escolher uma das opções acima: '))
    if t == 1:
        print('A soma é: {}'.format(s))
    elif t == 2:
        print('A multiplicação foi {}'.format(mult))
    elif t == 3:
        print('O maior entre os dois números é {}'.format(maior))
    elif t == 4:
        n1 = int(input('Digite um número inteiro: '))
        n2 = int(input('Digite outro valor inteiro: '))
    elif t > 4:
        break



