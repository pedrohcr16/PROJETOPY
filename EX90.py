nota = {'Nome': str(input("Nome: ").upper()), 'Media': float(input("Media: "))}

if nota['Media'] >= 6:
    nota['situação'] = 'Aprovado'
else:
    nota['situação'] = 'Reprovado'
print('=-'*30)
for chave, valor in nota.items():
    print(f'{chave}: {valor}')
