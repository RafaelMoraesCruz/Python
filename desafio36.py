vc = float(input('Digite o valor da casa desejada: '))
salario = float(input('Digite sua renda mensal: '))
t = float(input('Em quanto tempo deseja pagar a casa: '))
prestacao = vc/(t*12)
if prestacao >=salario*0.3:
    print('O emprestimo será negado, pois a prestação representa mais de 30% de seu salário mensal!!')
else:
    print('O empréstimo foi aprovado pois a prestação representa menos de 30% do seu salário!!')
print('\033[0:31:42m Obrigado por escolher o Banco do Brasil como seu banco!!')
