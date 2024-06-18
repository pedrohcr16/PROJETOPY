tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um numero de 0 a 20: '))

while numero > 20 or numero < 0:
    numero = int(input('Numero inválido! Tente novamente escolhendo um numero de 0 a 20: '))
else:
    print(f'O numero digitado foi {numero} por extenso fica {tupla[numero]}')
