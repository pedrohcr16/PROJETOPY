time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    jogador['partidas'] = int(input('Digite a quantidade de partidas: '))
    partidas.clear()
    for i in range(jogador['partidas']):
        partidas.append(int(input(f'Quantos gols na {i + 1}ª partida?: ')))
        jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        op = str(input('Deseja Continuar? [S/N]: ')).upper()[0]
        if op in 'SN':
            break
        print('Comando inválido!')
    if op == 'N':
        break
print('=-' * 35)

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 70)
for chave, valor in enumerate(time):
    print(f'{chave + 1:>3}', end='')
    for i in valor.values():
        print(f' {str(i):<15}', end='')
    print()
print('-' * 70)
while True:
    busca = int(input('Insira o codigo do jogador que deseja buscar [999 encerrar]: '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com o codigo: {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for chave, valor in enumerate(time[busca]['gols']):
            print(f'   No jogo {chave+1} marcou {valor} gol.')
    print('-' * 70)
print('<<FIM DO PROGRAMA>>')
