import datetime

ano = datetime.date.today().year

carteira = {'Nome': str(input("Digite o nome: ").upper()),
            'Ano de Nascimento': int(input("Digite o ano de nascimento: ")),
            'Carteira de Trabalho': int(input("Digite o nº carteira de trabalho: ")),
            'Contratação': int(input('Digite o ano de contratação: ')), 'Salário': int(input('Digite o salário: '))}

print('=-'*20)

if carteira['Carteira de Trabalho'] == 0:
    print(f"Nome: {carteira['Nome']}\n"
          f"Idade: {ano - carteira['Ano de Nascimento']}\n"
          f"Carteira: {carteira['Carteira de Trabalho']}")
else:
    for chave, valor in carteira.items():
        print(f'{chave}: {valor}')
    if carteira['Contratação'] <= 0:
        print('Sem contribuição')
    else:
        print(f'Aposentadoria tem : {ano - carteira["Contratação"]} anos de contribuição')
