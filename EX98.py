import time


def contador(i, f, p):
    print(f'De {i} até {f} de {p} em {p}: ', end='')
    for c in range(i, f + p, p):
        time.sleep(1)
        print(c, end=' ')
    print('FIM')
    print('-' * 60)


contador(1, 10, 1)
contador(10, 0, -2)

inicio = int(input('Digite o valor inicial: '))
fim = int(input('Digite o valor final: '))
passo = int(input('Digite o valor do passo: '))

contador(inicio, fim, passo)
