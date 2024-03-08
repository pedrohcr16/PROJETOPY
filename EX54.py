import datetime

atual = datetime.date.today().year
maioridade = 0
menoridade = 0
for i in range(1, 8):
    ano = int(input('Ano da {}ª pessoa: '.format(i)))
    if ano >= 21:
        maioridade += 1
    else:
        menoridade += 1
print('{} pessoas atingiram a maior idade\n'
      '{} pessoas estão na menor idade'.format(maioridade, menoridade))
