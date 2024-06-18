import random
tupla = tuple(random.randint(0, 9) for i in range(0, 5))
print(f'Os 5 numeros aleatórios da Tupla são: {tupla}\n'
      f'O maior encontrado {max(tupla)}\n'
      f'O menor encontrado {min(tupla)}')
