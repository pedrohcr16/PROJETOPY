pessoas18 = homem = mulhermenor18 = 0
while True:
    print('=-' * 20)
    print('CADASTRE UMA PESSOA')
    print('=-' * 20)
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    idade = int(input('Idade: '))
    opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if idade > 18:
        pessoas18 += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulhermenor18 += 1
    if opcao == 'N':
        break
print('=-' * 20)
print(f'Total de pessoas com mais de 18 anos: {pessoas18}\n'
      f'Ao todo temos {homem} homem cadastrado\n'
      f'E temos {mulhermenor18} mulher com menos de 20 anos')
