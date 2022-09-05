salario = float(input('Digite o salário do funcionário: '))
if salario>1250.00:
    print('O novo salário desse funcionário é de {:.2f}'.format(salario*1.1))
else:
    print('O novo salário desse funcionário é de {:.2f}'.format(salario * 1.15))
