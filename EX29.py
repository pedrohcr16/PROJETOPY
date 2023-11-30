from time import sleep

velocidade = float(input('Digite a sua velocidade atual: '))

print('Processando aguarde...')
sleep(2)

if velocidade > 80:
    print('Sua velocidade é {} KM\h e você será multado em {:.2f} R$'.format(velocidade, (velocidade - 80) * 7))
else:
    print('Sua velocidade é de {} KM\h e você não será multado'.format(velocidade))
print('Fim do Programa')
