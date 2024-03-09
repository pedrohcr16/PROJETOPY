a = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
cont = 1

while cont <= 10:
    a += r  # 1º TERMO + RAZÃO SOMADA NO LOOPING 10 VEZES #
    cont += 1  # QUANDO O CONTADOR CHEGAR A 10 O LOOPING PARA ATINGINDO A CONDIÇÃO DO WHILE #
    print('{}'.format(a), end=' - ')
print('Fim')
