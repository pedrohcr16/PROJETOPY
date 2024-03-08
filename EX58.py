import random
computador = 0
jogador = 1
contaperde = 0
while jogador != computador:
    jogador = int(input('Digite um valor entre 0 e 10: '))
    computador = random.randint(1, 10)
    if jogador > 10:
        print('Valor inválido, tente novamente')
    elif jogador != computador:
        contaperde += 1
        print('O jogador jogou {}\n'
              'O computador jogou {}\n'
              '\033[31mO Jogador Perdeu, tente novamente !\033[m'.format(jogador, computador))
        print('=-'*20)
    else:
        print('O jogador jogou {}\n'
              'O computador jogou {}\n'
              '\033[32mO Jogador Ganhou\033[m\n'
              '\033[36mForam necessárias {} tentativas para acertar\033[m'.format(jogador, computador, contaperde+1))
        print('=-' * 20)
print('Fim do programa')
