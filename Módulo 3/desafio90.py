dicionario = dict()
alunos = []
while True:
    dicionario['Aluno'] = str(input('Digite o nome do aluno: '))
    dicionario['media'] = float(input('Digite a média do aluno: '))
    if dicionario['media'] >= 7:
        dicionario['situacao'] = 'Aprovado'
    elif 7 >= dicionario['media'] >= 5:
        dicionario['situacao'] = 'Recuperação'
    elif dicionario['media'] < 5:
        dicionario['situacao'] = 'Reprovado'
    alunos.append(dicionario.copy())
    decisao = str(input('Deseja continuar? [S/N]'))
    if decisao in 'Nn':
        break
print('-=' * 25) #visual
for p in alunos:
    print('-=' * 25)  # visual
    for k, v in p.items():
        print(f'{k} é igual a {v}')
print('=' * 25) #visual
