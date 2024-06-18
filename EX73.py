brasileirao = 'Palmeiras', 'Atletico_MG', 'Flamengo', 'Gremio', 'Botafogo', 'Bragantino', 'Fluminense', 'Atletico_PR', \
              'Internacional', 'Fortaleza', 'Sao_Paulo', 'Cuiaba', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia', \
              'Vitoria', 'Juventude', 'Criciúma', 'Atletico_GO'

print(f'Os 5 primeiros são: {brasileirao[0:5]}')
print(f'Os 4 ultimos são: {brasileirao[-4:]}')
print(f'Times por ordem alfabetica: {sorted(brasileirao)}')
print("O Flamengo esta em", brasileirao.index('Flamengo')+1, "ª posição")
