def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: número a ser cálculado
    :param show: mostrar a memória de cálculo
    :return: valor do resultado do fatorial do num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))