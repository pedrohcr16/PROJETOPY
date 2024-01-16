peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc <= 18.5:
    print("Seu imc é de {:.2f}, você está \033[31mAbaixo do Peso\033[m".format(imc))
elif 18.5 < imc < 25:
    print('Seu imc é de {:.2f}, você está no \033[32mPeso Ideal\033[m'.format(imc))
elif 25 < imc < 30:
    print('Seu imc é de {:.2f}, você está com \033[33mSobrepeso\033[m'.format(imc))
elif 30 < imc < 40:
    print('Seu imc é de {:.2f}, você está em \033[31mObesidade\033[m'.format(imc))
else:
    print('Seu imc é de {:.2f}, você está em \033[31mObesidade Morbida\033[m'.format(imc))
print('Fim do Programa')
