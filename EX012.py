preco = float(input('Digite o preço do produto: '))

print('O preço digitado foi de {:.2f} R$\n'
      'O preço com desconto é de 5% é de {:.2f} R$'
      .format(preco, (preco - (preco * 0.05))))
