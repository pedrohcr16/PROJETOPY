a = int(input('Digite o valor do primeiro termo: '))
r = int(input('Digite o valor da razão: '))
cont = 1
total = 0
mais = 10

while mais != 0:  # ENQUANTO A VARIAVEL FOR DIFERENTE DE 0 DENTRO DA CONDIÇÃO ANINHADA O LOOPING SE REPETIRÁ #
    total = total + mais  # AQUI SERÁ PREDEFINIDO OS 10 PRIMEROS LOOPING DE REPETIÇÃO POIS TOTAL = 0 + MAIS = 10 INICIALMENTE #
    while cont <= total:
        a += r  # 1º TERMO + RAZÃO SOMADA NO LOOPING #
        cont += 1  # O CONTADOR DO LOOPING #
        print('{}'.format(a), end=' - ')
    print('Pausa')
    mais = int(input('Deseja inserir mais quantos termos?: '))
print('Foram mostradas {} P.As'.format(total))  # O TOTAL DE LOOPING TAMBEM É O TOTAL DE P.A #
