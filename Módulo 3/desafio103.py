def ficha(jog='<desconhesido>', gol=0):
  print(f'0 jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa principal
n = str(input("Nome do Jogador: "))
g = str(input("Núnero de Gols: "))
if g.isnumeric():
  g = int(g)
else:
  g = 0
if n.strip() == '':
  ficha(gol = g)
else:
  ficha(n, g)