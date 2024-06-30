lista = []
for i in range(5):
    numero = int(input('Digite um valor: '))
    for posicao, valor in (enumerate(lista)):
        if numero < valor:
            lista.insert(posicao, numero)
            break
    else:
        lista.append(numero)
print(f'Os valores digitados em ordem: {lista}')
