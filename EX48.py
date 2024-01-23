n = 0
count = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        n += i
        count = count + 1
        print(i, end=' ')
print('\nA soma de todos os {} números múltiplos de 3 no intervalo de 1 a 500 é {}'.format(count, n))
