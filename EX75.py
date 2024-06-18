tupla = (int(input('Digite um valor: '))), (int(input('Digite um valor: '))), (int(input('Digite um valor: '))), (
    int(input('Digite um valor: ')))

print(f'Tupla digita foi: {tupla}')

print(f'O numero 9 apareceu: {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O numero 3 foi localizado primeiro no indice: {(tupla.index(3) + 1)}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=', ')
print('\nFim da operação!')
