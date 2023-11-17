import math

n1 = int(input('Digite o angulo: '))
print('O angulo digitado foi {}\n'
      'O seno é {:.2f}\n'
      'O cosseno é {:.2f}\n'
      'A tangente é {:.2f}'
      .format(n1, math.sin(math.radians(n1)), math.cos(math.radians(n1)), math.tan(math.radians(n1))))
