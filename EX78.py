lista = []

for posicao in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {posicao+1}: ')))
print(f'A lista digitada foi: {lista}')

for posicao, valor in (enumerate(lista)):
    if valor == max(lista):
        print(f'O maior valor digitado foi {valor} na posição {posicao+1}')
    elif valor == min(lista):
        print(f'O menor valor digitado foi {valor} na posição {posicao+1}')

print('Fim do programa!')
