nome = str(input("Insira um nome: "))
print('O nome é {}\n'
      'Em maiusculo é {}\n'
      'Em minusculo é {}\n'
      'Tem {} letras\n'
      'O primeiro nome tem {} letras'
      .format(nome, nome.upper(), nome.lower(), len(nome) - nome.count(' '), nome.split()[0].__len__()))
