distancia = float(input('Digite a distancia da viagem: '))

if distancia <= 200:
    print('A distancia percorrida é de {} KM\n'
          'O valor a ser cobrado é de {:.2f} R$'.format(distancia, distancia * 0.5))
else:
    print('A distancia percorrida é de {} KM\n'
          'O valor a ser cobrado é de {:.2f} R$'.format(distancia, distancia * 0.45))
print('Fim do Programa')
