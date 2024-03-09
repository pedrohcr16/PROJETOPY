n = int(input('Digite um numero para saber seu fatorial: '))
fat = 1
for i in range(n, 0, -1):
    fat *= i
print('O fatorial de {}! = {}'.format(n, fat))
