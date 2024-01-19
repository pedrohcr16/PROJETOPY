import random
import time

jogador = str(input('Faça sua jogada: ')).strip().lower()
computador = ('pedra', 'papel', 'tesoura')
computador = random.choice(computador)

print('=-='*20)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
print('=-='*20)

if jogador == computador:
    print('O computador escolheu: {}\n'
          'E o jogador escolheu: {}\n'
          'Resultado: \033[33mVocês Empataram\033[m'.format(computador, jogador))
    print('=-=' * 20)
elif (jogador == 'pedra' and computador == 'tesoura'
      or jogador == 'tesoura' and computador == 'papel'
      or jogador == 'papel' and computador == 'pedra'):
    print('O computador escolheu: {}\n'
          'E o jogador escolheu: {}\n'
          'Resultado: \033[32mVocê Ganhou\033[m'.format(computador, jogador))
    print('=-=' * 20)
else:
    print('O computador escolheu: {}\n'
          'E o jogador escolheu: {}\n'
          'Resultado: \033[31mVocê Perdeu\033[m'.format(computador, jogador))
    print('=-=' * 20)
print('Fim do Programa')
