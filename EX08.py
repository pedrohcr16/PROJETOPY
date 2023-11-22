metros = int(input('Digite um valor: '))

print("O valor inserido em metros é {} metros"
      "\nO valor em centimetros é {} centimetros"
      "\nO valor em milimetros é {} milimetros"
      .format(metros, (metros * 100), (metros * 1000)))
