print('-=' * 15)
print('Sequência de Fibonacci')
print('-=' * 15)
termos = int(input('Digite quantos termos você quer mostrar: '))
ultimo = 1
penultimo = 1

if termos == 1 or termos == 2:
    print("O primeiro e o segundo termo da sequência de Fibonacci é  igual á 1")
else:
    for i in range(2, termos):
        fib = ultimo + penultimo  # vale ressaltar que aqui a sequência começa no 3º termo de fibonacci 1 + 1 #
        penultimo = ultimo  # aqui o penultimo valor passa a ser o ultimo valor que vai no proximo looping #
        ultimo = fib  # aqui o ultimo valor passa a ser a soma de fib que vai no proximo looping #
        print('{}'.format(fib), end=' - ')
