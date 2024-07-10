lista = [[], []]

for i in range(7):
    valor = (int(input(f'Digite o {i + 1}º valor: ')))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print('=-'*20)
print(f'Os valores pares digitados foram: {sorted(lista[0])}\n'
      f'Os valores impares digitados foram: {sorted(lista[1])}')
