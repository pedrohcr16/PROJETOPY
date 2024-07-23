import random
import time

jogo = {'1º Jogador': random.randint(1, 6), '2º Jogador': random.randint(1, 6), '3º Jogador': random.randint(1, 6),
        '4º Jogador': random.randint(1, 6)}

for chave, valor in jogo.items():
    time.sleep(1)
    print(f'{chave} tirou: {valor}')
print('=-' * 1, 'Ranking Ordenado por valor', '=-' * 1)

for i in sorted(jogo, key=jogo.get, reverse=True):
    print(i, jogo[i])
