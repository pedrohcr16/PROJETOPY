op = ''
lista = []
while op != "N":
    insercao = int(input('Digite um número: '))
    op = str(input('Quer continuar ? [Y/N]: ')).upper().strip()

    if insercao in lista:
        del insercao
        print('Valor duplicado não adicionado!')
        print('=-'*20)
    else:
        lista.append(insercao)
        print('Valor adicionado com sucesso!')
        print('=-'*20)

    print(sorted(lista))
print('Fim do Programa!')
