import random

numeros = list()


def sorteia():
    for i in range(5):
        numeros.append(random.randint(0, 100))
    print(f'Lista gerada: {numeros}')


sorteia()


def somapar():
    pares = list()
    for i in range(5):
        if numeros[i] % 2 == 0:
            pares.append(numeros[i])
    print(f'Lista de pares: {pares}')
    print(f'Soma dos pares: {sum(pares)}')


somapar()
