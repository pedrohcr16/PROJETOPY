nome = input('Digite seu nome: ')
verde = '\033[0;32m'

# Forma1 #
print('É um prazer te conhecer,', nome, '!')

# Forma2 #
print('É um prazer te conhecer, {}!'.format(nome))

# Forma3 com cor#
print('É um prazer te conhecer, {}{}!'.format(verde, nome))
