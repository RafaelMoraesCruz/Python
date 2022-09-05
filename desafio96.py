def area(a, b):
    areaterreno = a * b
    print('Controle de Terrenos')
    print('_' * 20)
    print(f'O terreno tem {a}m de comprimento, {b}m de largura e sua área é de: {areaterreno}m² ')


a = float(input('Digite o comprimento em metros do terreno: '))
b = float(input('Digite a largura em metros do terreno: '))
area(a, b)
