frase = str(input('Digite algo: ')).lower().strip()
print('Essa frase tem {} letras a\n'
      'Sua primeira posição é no indice {}\n'
      'A sua ultima posição é no indice {}'
      .format(frase.count('a'), frase.find('a'), frase.rfind('a')))
