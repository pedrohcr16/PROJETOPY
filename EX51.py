a = int(input('Digite um valor para 1º termo: '))
r = int(input('Digite um valor para razão: '))
n = int(input('Digite o valor do enésimo termo: '))
n = a + (n - 1) * r  # FORMULA DO ENESIMO TERMO#
for i in range(a, n + r, r):
    print(i, end=' ')
