carteira = int(input('Insira quantos reais você tem na carteira: '))
conversao = (carteira / 4.86)
print('Com esse valor de R${:.2f} você pode comprar {:.2f} U$'
      .format(carteira, conversao))
