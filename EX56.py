mi = 0
fe = 0
mih = []
nv = ''
for i in range(1, 5):
    nome = str(input('Digite o {}º nome: '.format(i))).strip().lower()
    idade = int(input('Digite a {}ª idade: '.format(i)))
    mi += idade
    sexo = str(input('Digite o [M] para Masculino e [F] para Feminino: ')).upper()
    if i == 1 and sexo == 'M':
        mih = idade
        nv = nome
    if sexo in 'M' and idade > mih:
        mih = idade
        nv = nome
    if sexo == 'F' and idade < 20:
        fe += 1
print('A media de idade do grupo é {} anos\n'
      'O homem de maior idade é o {} com {} anos\n'
      'Existe {} mulheres com idade menor que 20 anos'.format(mi / 4, nv, mih, fe))
