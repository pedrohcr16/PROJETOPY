n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota nota: '))
media = (n1 + n2) / 2

if media < 5:
    print('Sua media é de {} você está:\033[31m Reprovado\033[m'.format(media))
elif media >= 7:
    print('Sua media é de {} você está:\033[32m Aprovado\033[m'.format(media))
else:
    print("Sua media é de {} você está:\033[33m 6Recuperação\033[m".format(media))
print('Fim do programa')
