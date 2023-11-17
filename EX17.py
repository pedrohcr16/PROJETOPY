import math

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
hipotenusa = (((ca ** 2) + (co ** 2)) ** (1 / 2))
print('O valor do cateto adjacente é {}\n'
      'O valor do cateto oposto é {}\n'
      'O valor da hipotenusa é {:.2f}'
      .format(ca, co, hipotenusa))  # Aqui foi utilizado o conceito matematico#

# Aqui foi utilizado a função da biblioteca hypot#

print('O valor do cateto adjacente é {}\n'
      'O valor do cateto oposto é {}\n'
      'O valor da hipotenusa é {:.2f}'
      .format(ca, co, math.hypot(ca, co)))
