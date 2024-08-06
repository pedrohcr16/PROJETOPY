def escreva(msg):
    print('-' * (len(msg) + 4))
    print(f'  {msg}')
    print('-' * (len(msg) + 4))


mensagem = str(input('Escreva uma mensagem: '))
escreva(mensagem)
