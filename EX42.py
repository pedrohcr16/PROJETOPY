r1 = int(input('Insira a comprimento da primeira reta: '))
r2 = int(input('Insira a comprimento da segunda reta: '))
r3 = int(input('Insira a comprimento da terceira reta: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('O comprimento das tres atendem a condição de existencia do triangulo')
    if (r1 == r2) and (r2 == r3) and (r3 == r1):
        print('É um tringulo Equilátero')
    elif (r1 == r2) or (r1 == r3):
        print('É um tringulo Isosceles')
    elif (r1 != r2) and (r1 != r3) and (r2 != r3):
        print('É um triangulo Escaleno')
else:
    print('O comprimento das tres não atendem a condição de existencia do triangulo')
print('Fim')
