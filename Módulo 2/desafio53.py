frase = (input('Digite uma frase ou uma palavra: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print(' {} e {}'.format(junto, inverso))
if inverso == junto:
    print('a frase é um palíndromo! ')
else:
    print('A frase não é um palíndromo! ')
