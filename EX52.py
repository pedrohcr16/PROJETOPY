n = int(input('Digite um número: '))
t = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[34m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(i), end='')
print('\n\033[mO numero {} é divisivel por {} numeros'.format(n, t))

if t == 2:
    print('\033[mÉ nº primo')
else:
    print('\033[mNão é nº primo')
