lista = []

while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a 1ª nota: '))
    nota2 = float(input('Digite a 2ª nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    opcao = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    print('=-' * 20)

    if opcao == 'N':
        break
for posicao, valor in enumerate(lista):
    print(F'Nº{posicao}, NOME: {valor[0].upper()}, MEDIA: {valor[2]}')

while True:
    opcao2 = int(input('Deseja saber a nota de qual aluno? [999 finaliza o programa]: '))
    if opcao2 == 999:
        print('Fim do Programa')
        break
    else:
        print(f'Aluno {lista[opcao2][0].upper()} nota:{lista[opcao2][1]}')
    print('=-'*35)
