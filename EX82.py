par = []
impar = []
op = ''

while op != 'N':
    inserir = int(input('Digite um valor: '))
    op = str(input('Quer continuar? [S/N] ')).strip().upper()

    while op != 'S' and op != 'N':
        print('Opção inválida. Tente novamente.')
        inserir = int(input('Digite um valor: '))
        op = str(input('Quer continuar? [S/N] ')).strip().upper()

    if inserir % 2 == 0:
        par.append(inserir)
        print('O valor par foi adicionado a lista')
        print('=-=' * 12)

    else:
        impar.append(inserir)
        print('O valor impar foi adicionado a lista')
        print('=-=' * 12)

print(f'A lista completa é {par + impar}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
