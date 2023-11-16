salario = float(input('Digite o seu salário: '))
print('O seu salário é de {:.2f} R$\n'
      'Com aumento de 15% vai para {:.2f} R$'
      .format(salario, (salario + (salario * 0.15))))
