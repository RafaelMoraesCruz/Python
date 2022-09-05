s = -999
q = -1
n1 = 0
while n1 != 999:
    n1 = int(input('Se quiser encerrar o programa digite 999, senão, Digite um número: '))
    q += 1
    s += n1
print('A quantidade de números digitados foi: {} e a soma entre os números foi: {}'.format(q, s))
