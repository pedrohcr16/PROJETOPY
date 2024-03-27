total = contmil = menor = contmenor = 0
prodbarato = ''
print('-=' * 20)
print('Pedrão Mega Store')
print('-=' * 20)
while True:
    nomeproduto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$: '))
    opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    contmenor += 1
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    print('-=' * 20)
    total += preco
    if preco >= 1000:
        contmil += 1
    if contmenor == 1:  # AQUI O LOOPING ATRIBUI O PRIMEIRO PRECO AO MENOR PRECO#
        menor = preco
        prodbarato = nomeproduto
    else:
        if preco < menor:  # CASO O PROXIMO PRECO SEJA MENOR ESSE ENTAO SERA O MENOR#
            menor = preco
            prodbarato = nomeproduto
    if opcao == 'N':
        break
print(f'O total de compras foi de {total}')
print(f'Temos {contmil} produtos custando acima de R$ 1000,00')
print(f'O produto mais barato foi {prodbarato} e custa R$: {menor}')
