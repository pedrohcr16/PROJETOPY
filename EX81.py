op = ''
lista = []
while op != "N":
    insercao = int(input('Digite um número: '))
    op = str(input('Quer continuar ? [Y/N]: ')).upper().strip()
    lista.append(insercao)
print('-='*20)

print(f'A {len(lista)} elementos na lista')
print(f'A lista decrescente é: {sorted(lista, reverse=True)}')

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
