ano = int(input('Digite o ano: '))
bissexto = ano % 4

if bissexto == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano normal')
print('Fim do programa')
