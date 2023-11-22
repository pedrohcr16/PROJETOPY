preco = float(input('Digite o preço do produto: '))

print('O preço digitado foi {:.2f} R$\n'
      'O preço com desconto é de 5% é {:.2f} R$'
      .format(preco, (preco - (preco * 0.05))))
