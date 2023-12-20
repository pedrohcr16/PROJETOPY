valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Digite em quantos anos de financiamento: '))
mensalidade = (valor / anos) / 12

if mensalidade > salario * 0.3:
    print('Negado seu salário é de {:.2f} R$\n'
          'E a mensalidade é de {:.2f} R$\n'
          'Durante {} anos ultrapassando 30% do salário mensal'
          .format(salario, mensalidade, anos))
else:
    print('Aprovado seu salário é de {:.2f} R$\n'
          'E a mensalidade é de {:.2f} R$\n'
          'Durante {} anos compromete menos de 30% do salário mensal'
          .format(salario, mensalidade, anos))
print('Fim da simulação')
