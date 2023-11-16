altura = int(input('Insira o valor da altura: '))
largura = int(input('Insira o valor da altura: '))
area = (altura * largura)

print('A altura é {}m\n'
      'A largura é {}m\n'
      'A area é de {}m²'
      .format(altura, largura, area))
print('Considerando que para pintar cada m² necessitamos de 2 litros de tinta a quantia necessária é de: {} litros'
      .format(area / 2))
