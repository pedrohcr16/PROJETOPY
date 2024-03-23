while True:
    multiplicando = int(input('Digite o valor do multiplicando: '))
    multiplicador = int(input('Digite o valor do multiplicador: '))
    if multiplicando < 0 or multiplicador < 0:
        break
    else:
        for multiplicador in range(1, multiplicador+1):
            print(f'O produto da tabuada de {multiplicando} x {multiplicador} = {multiplicando * multiplicador}')
        print('=-'*20)
print('Acabou!')
