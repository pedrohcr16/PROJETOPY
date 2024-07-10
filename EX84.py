dados = []
lista = []
op = ''
countpessoas = 0
maior = 0
menor = 0

while True:
    dados.append((str(input('Digite o nome: '))))
    dados.append((int(input('Digite o peso: '))))

    if len(dados) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    lista.append(dados[:])
    dados.clear()

    countpessoas += 1

    op = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    print('=-'*20)

    if op == 'N':
        break

print(f'Foram cadastrados: {countpessoas} pessoas')

for i in lista:
    if i[1] == maior:
        print(f'O maior peso encontrado foi de {i[0].upper()} com {i[1]} Kg')
print()
for i in lista:
    if i[1] == menor:
        print(f'O menor peso encontrado foi de {i[0].upper()} com {i[1]} Kg')
print()
