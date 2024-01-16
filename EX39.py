from datetime import date

nascimento = int(input('Digite o ano do seu nascimento: '))
atual = int(date.today().year)
idade = atual - nascimento

if idade < 18:
    print('Você tem {} anos e está fedendo a leite ainda não chegou a hora de se alistar\n'
          'Faltam {} anos para o alistamento\n'
          'Sua data de alistamento é em: {}'.format(idade, 18 - idade, nascimento + 18))
elif idade == 18:
    print("Você tem {} anos e chegou a hora de se alistar meu consagrado pegue a enchada"
          .format(idade))
else:
    print('Você tem {} anos e passou {} anos da hora vagabundo passe no RH\n'
          'Sua data de alistamento foi em: {}'.format(idade, idade - 18, nascimento + 18))
print('Fim do programa')
