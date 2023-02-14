'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
A) Apenas o 5 primeiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética.
D) Em que posição na tabela está o time da Chapecoense.
'''

brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG', 'Fortaleza',
 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba', 
 'Cuiabá', 'Ceara', 'Chapecoense', 'Avaí', 'Juventude',)

print('-' *50)
print(f'\033[32mOs 5 primeiros colocados do Brasileirão 2022\033[m {brasileirao[:5]}')
print('-' *50)
print(f'\033[31mOs últimos 4 colocados da tabela\033[m {brasileirao[-4:]}')
print('-' *50)
print(f'Times em ordem alfabética {sorted(brasileirao)}')
print('-' *50)
print(f'O time da Chapecoense esta na {brasileirao.index("Chapecoense")+1}ª posição')
print('-' *50)
