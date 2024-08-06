import time


def maior(*num):
    print('=-' * 40)
    print('Analisando os valores passados...')
    if len(num) > 0:
        for i in range(len(num)):
            print(f'{num[i]}', end=' ')
            time.sleep(1)
        print(f'Foram informados {len(num)} numeros')
        print(f'O maior valor informado foi {max(num)}')
    else:
        print('Valores nulos são inválidos')


maior(16, 7)
maior(25, 6, 99)
maior(7)
maior()
