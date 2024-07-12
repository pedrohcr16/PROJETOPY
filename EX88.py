import random
import time

lista = []

qtd = int(input('Quantos jogos serão sorteados?: '))
dzn = int(input('Digite quantas dezenas?: '))
print('=-' * 5, 'Gerando os Jogos', '=-' * 5)

for i in range(qtd):
    for jogo in range(dzn):
        numeros = random.randint(1, 60)
        lista.append(numeros)
    time.sleep(2)
    print(f'Jogo {i + 1}: {sorted(lista)}')
    lista.clear()
print('Fim')
