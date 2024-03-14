op = 0
contador = 0
soma = 0
while op != 999:
    op = int(input('Digite um numero [999 para parar]: '))
    soma += op
    contador += 1
    if op == 999:
        soma -= op
        contador -= 1
print('Foram digitados {} valores e a soma dentre ele é {}'.format(contador, soma))
