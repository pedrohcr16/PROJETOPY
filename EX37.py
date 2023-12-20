n1 = int(input('Digite um numero: '))
print('''Escolha a base de conversão:
[1] Converter para BINÁRIO
[2] Converter para OCTAL
[3] Converter para HEXADECIMAL''')

base = int(input('Digite a base de conversão: '))

if base == 1:
    print('O valor decimal é de {}\n'
          'A conversão binária é de {}'
          .format(n1, bin(n1)[2:]))
elif base == 2:
    print('O valor decimal é de {}\n'
          'A conversão octal é de {}'
          .format(n1, oct(n1)[2:]))
elif base == 3:
    print('O valor decimal é de {}\n'
          'A conversão hexadecimal é de {}'
          .format(n1, hex(n1)[2:]))
else:
    print('Você não informou a base conversora')
print('Fim do programa')
