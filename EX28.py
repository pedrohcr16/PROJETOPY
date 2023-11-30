import random
from time import sleep

y = int(input('Digite um numero inteiro de 0 a 5: '))
x = random.randint(0, 5)

print('Processando...')
sleep(2)

if y > 5:
    print('Você não digitou um numero entre 0 e 5')
elif x == y:
    print('Você digitou o numero {}\n'
          'O PC digitou o numero {}\n'
          'Parabens voce venceu'.format(y, x))
else:
    print('Você digitou o numero {}\n'
          'O PC digitou o numero {}\n'
          'Voce perdeu'.format(y, x))
print('Fim do programa')
