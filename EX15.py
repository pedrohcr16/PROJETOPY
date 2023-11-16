km = float(input('Digite quantos KM você percorreu: '))
dia = int(input('Informe quantos dias você utilizou: '))

print('Você percorreu com o carro por {} km\n'
      'O valor por km rodado é de 0,15 R$\n'
      'Portanto o valor total a pagar pelos km rodados é {} R$\n'
      'Você utilizou o carro por {} dias\n'
      'O valor por dia utilizado é de 60.0 R$\n'
      'Portanto o valor total a pagar pelos dias utilizados é {} R$\n'
      'O total a pagar é de {} R$'
      .format(km, km*0.15, dia, dia*60, ((km*0.15) + (dia*60))))
