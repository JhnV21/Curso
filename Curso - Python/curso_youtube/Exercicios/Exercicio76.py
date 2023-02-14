'''
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados
em forma tabular.
'''
print('-'*30)
print(f'\033[32m{"COMPRAS" :^30}\033[m')
print('-'*30)
produtos = ('Salgadinho', 6, 'Coca-Cola', 12.5, 'Pão', 5.75, 'Ração', 12.9, 'Amaciante', 11)
for c in range(0, len(produtos), 2):
    print(f'{produtos[c]:.<17}R$ {produtos[c+1]:>7.2f}')
print('-'*30)
