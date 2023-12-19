salario = float(input('Digite o valor do seu salário: '))

if salario > 1250:
    print('Seu aumento será de 10% passando para {} R$\n'
          .format(salario + (salario * 0.10)))
else:
    print('Seu aumento será de 15% passando para {} R$'
          .format(salario + (salario * 0.15)))
print('Fim do programa')
