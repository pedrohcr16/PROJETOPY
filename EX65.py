op = ''
count = media = maior = menor = 0

while op != "N":
    a = int(input('Digite um número: '))
    op = str(input('Quer continuar ? [Y/N]: ')).upper().strip()
    count += 1
    media += a
    media = media / count
    if count == 1:
        maior = menor
        menor = a
        a = maior
    else:
        if a > maior:
            maior = a
            if a < menor:
                menor = a
print('Você digitou {} numeros e a media foi {:.2f}\n'
      'O maior valor digitado foi {} e o menor {}'.format(count, media, maior, menor))
