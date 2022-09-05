def voto (ano = 0):
    from _datetime import datetime
    """ ANO: ano do seu nascimento
    Será feita então a diferença entre o ano atual com o ano do seu nascimento, para que então
    seja feito o cálculo da idade. Depois de realizado o cálculo da idade, será feita uma análise para que então
    retorne se o candidato possa ou não votar! """
    anoatual = datetime.today().year
    idade = anoatual - ano
    if 60 > idade >= 18:
        return f'Sua idade é de: {idade} e o seu voto é OBRIGATÓRIO!'
    elif idade >= 60:
        return f'Sua idade é de {idade} e seu voto é opcional'
    else:
        return f'Sua idade é de {idade} e seu voto é NEGADO'


ano = int(input('Digite o ano do seu nascimento: '))
print(voto(ano))




