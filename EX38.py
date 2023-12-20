n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

if n1 > n2:
    print('O primeiro valor {} e maior'.format(n1))
elif n2 > n1:
    print('O segundo valor {} e maior'.format(n2))
else:
    print('O primeiro valor {} e o segundo valor {}, são iguais'.format(n1, n2))
print('Fim do Programa')
