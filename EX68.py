import random
vitoria = 0
while True:
    jogador = int(input('Digite um numero: '))
    computador = random.randint(0, jogador)
    escolha = str(input('Escolha [PAR/IMPAR]: ')).upper().strip()
    print('=-'*30)
    soma = jogador + computador
    if soma % 2 == 0:
        total = 'PAR'
    else:
        total = 'IMPAR'
    if escolha == total:
        vitoria += 1
        print('\033[32mJogador Venceu!\033[m\n'
              f'O jogador escolheu o número {jogador} e sua escolha foi {escolha}\n'
              f'O computador escolheu o número {computador}\n'
              f'A soma foi {soma} que é {total}')
        print('=-'*30)
    if escolha != total:
        print('\033[31mJogador Perdeu!\033[m\n'
              f'O jogador escolheu o número {jogador} e sua escolha foi {escolha}\n'
              f'O computador escolheu o número {computador}\n'
              f'A soma foi {soma} que é {total}')
        print('=-'*30)
        break
print(f'Game Over você venceu {vitoria} vezes')
print('=-'*30)
