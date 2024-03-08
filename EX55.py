peso = [float(input('Digite o peso da {} ª pessoa: '.format(i))) for i in range(1, 6)]
print('O menor peso foi {} Kg\n'
      'O maior peso  foi {} Kg'.format(min(peso), max(peso)))
