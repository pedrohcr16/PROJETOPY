palavra = str(input('Digite uma palavra: ')).lower().replace(' ', '')
invertido = palavra[::-1]

if palavra == invertido:
    print('A palavra digitada foi {}\n'
          'A palavra digitada invertida fica {}\n'
          'Após inverter continua sendo escrito da mesma forma de trás para frente\n'
          'Categorizando um Palindromo'.format(palavra, invertido))
else:
    print('A palavra digitada foi {}\n'
          'A palavra digitada invertida fica {}\n'
          'Após inverter não é escrito da mesma forma de trás para frente\n'
          'Não categorizando um Palindromo'.format(palavra, invertido))
print('Fim')
