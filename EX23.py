num = int(input('Digite um numero: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print('O numero digitado tem {} unidade\n'
      'O numero digitado tem {} dezenas\n'
      'O numero digitado tem {} centenas\n'
      'O numero digitado tem {} milhares'
      .format(unidade, dezena, centena, milhar))
