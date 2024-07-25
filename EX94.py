todos = list()
pessoa = dict()
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('Comando inválido!')
    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']
    todos.append(pessoa.copy())
    while True:
        op = str(input('Deseja Continuar? [S/N]: ')).upper()[0]
        if op in 'SN':
            break
        print('Comando inválido!')
    if op == 'N':
        break
print('=-' * 12, 'Resultado', '=-' * 12)
print(f'Foram cadastradas {len(todos)} pessoas.')
print(f'A media de idades foi {soma / len(todos)} anos')
print(f'As pessoas do sexo feminino cadastradas foram:', end='')
for i in todos:
    if i['sexo'] in "Ff":
        print(f'{i["nome"]}', end=', ')
print('')

print(f'As pessoas do sexo masculino cadastradas foram:', end='')
for i in todos:
    if i['sexo'] in "mM":
        print(f'{i["nome"]}', end=', ')
print('')

print(f'As pessoas do acima da média de idade:', end='')
for i in todos:
    if i["idade"] >= soma / len(todos):
        print(f'{i["nome"]}', end=', ')
print('')
