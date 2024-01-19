valor = float(input('Insira o valor do produto: '))
pagamento = int(input('''FORMA DE PAGAMENTO
[1] dinheiro
[2] cartão a vista
[3] cartão 2x
[4] cartão 3x
Escolha a forma de pagamento:'''))

if pagamento == 1:
    print('O valor do produto é {:.2f} R$ e com desconto 10% fica em {:.2f} R$'.format(valor, valor - valor * 0.1))
elif pagamento == 2:
    print('O valor do produto é {:.2f} R$ e com desconto 5% fica em {:.2f} R$'.format(valor, valor - valor * 0.05))
elif pagamento == 3:
    print('O valor do produto é {:.2f} R$ em parcelado 2x cada fica {:.2f} R$'.format(valor, valor / 2))
elif pagamento == 4:
    print('O valor do produto é {:.2f} R$ e com juros 20% o total fica em {:.2f} R$'.format(valor, valor + valor * 0.2))
else:
    print('OPÇÃO INVÁLIDA')
print('Fim')
