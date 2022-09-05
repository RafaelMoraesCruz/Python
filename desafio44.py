preço_do_produto = float(input('Digite o preço do produto: '))
print('escolha um método de pagamento: dinheiro, cheque, cartão, 2x no cartão e 3x+ no cartão')
escolha = input('Informe o método de pagamento: ')
if escolha == 'dinheiro' or escolha == 'cheque':
    print('O preço do item fica: {} reais'.format(preço_do_produto * 0.9))
elif escolha == 'cartão':
    print('O preço do item fica: {} reais'.format(preço_do_produto * 0.95))
elif escolha == '2x no cartão':
    print('O preço do item fica: {} reais'.format(preço_do_produto))
elif escolha == '3x+ no cartão':
    print('O preço do item fica: {} reais'.format(preço_do_produto * 1.2))
else:
    print('Digite um método de pagamento disponível!!')
