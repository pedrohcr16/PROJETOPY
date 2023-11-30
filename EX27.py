nome = str(input('Digite seu nome completo: '))
print('O seu primeiro nome é: {}\n'
      'O seu ultimo nome é: {}'
      .format(nome.split()[0], nome.split()[-1]))
