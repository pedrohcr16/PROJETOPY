city = str(input('Digita o nome da sua cidade: ')).upper().strip()
print('O nome da cidade é {}\n'
      'E é {} que começa com o nome Santo'
      .format(city, 'SANTO' in city.split()[0]))
