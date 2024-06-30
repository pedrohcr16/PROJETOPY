count1 = 0
count2 = 0

exp = str(input('Digite sua expressao: '))

for simbolo in exp:
    if simbolo == '(':
        count1 += 1
    if simbolo == ')':
        count2 += 1
if exp == '0':
    print('Expressao está zerada')
else:
    if count1 == count2:
        print('A expressao é valida')
    else:
        print('A expressao não é valida')
print('Fim do Programa')
