gols = []
jogador = {'nome': str(input('Digite o nome do jogador: ')),
           'partidas': int(input('Digite a quantidade de partidas: '))}

for i in range(jogador['partidas']):
    gols.append(int(input(f'Quantos gols na {i + 1}ª partida?: ')))
    jogador['gols'] = gols[:]
jogador['total'] = sum(gols)

print('=-'*35)
print(jogador)
print('=-'*35)

for chave, valor in jogador.items():
    print(f'O campo {chave} tem valor {valor}')
print('=-'*35)

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')

for chave, valor in enumerate(jogador['gols']):
    print(f'Na partida {chave+1}, fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
