from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))
atual = int(date.today().year)
idade = atual - nascimento

if idade <= 9:
    print('O atleta tem {} anos e está na categoria mirim'.format(idade))
elif 9 < idade <= 14:
    print('O atleta tem {} anos e está na categoria infantil'.format(idade))
elif 14 < idade <= 19:
    print('O atleta tem {} anos e está na categoria junior'.format(idade))
elif 19 < idade <= 25:
    print('O atleta tem {} anos e está na categoria senior'.format(idade))
else:
    print('O atleta tem {} anos e está na categoria master'.format(idade))
print('Fim')
