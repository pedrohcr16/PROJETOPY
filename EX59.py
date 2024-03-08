import time
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um valor: '))
menu = 0
while menu != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa''')
    menu = int(input('Digite sua opção: '))
    print('-='*20)
    if menu == 1:
        print('A soma de {} + {} = {}'.format(valor1, valor2, valor1 + valor2))
        print('-='*20)
    elif menu == 2:
        print('A multiplicação de {} * {} = {}'.format(valor1, valor2, valor1 * valor2))
        print('-='*20)
    elif menu == 3:
        print('O maior valor digitado foi {}'.format(max(valor1, valor2)))
        print('-='*20)
    elif menu == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite um valor: '))
    elif menu == 5:
        time.sleep(3)
        print('Fim do programa')
        print('-='*20)
    else:
        print('Opção Inválida, tente novamente!')
        print('-='*20)
