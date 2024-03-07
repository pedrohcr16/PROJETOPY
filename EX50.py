s = 0
cont = 0
for i in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
print('Foi informado {} nº pares e a soma deles foi {}'.format(cont, s))
