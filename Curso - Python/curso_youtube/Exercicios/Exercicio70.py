'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
A> Qual é o total gasto na compra.
B> Quantos produtos custam mais de R$1000.
C> Qual é o nome do produto mais barato.
'''

total = produtos = 0
lista = [] 
barato = [] 
continuar = 'S'

while continuar == 'S':
    nome = input('Digite o nome do produto: ').strip()
    lista.append(nome) 
    preco = float(input('Digite o preço do produto: \033[32mR$\033[m'))
    total += preco 
    barato.append(preco) 
    if preco > 1000:
        produtos += 1
    mais_barato = barato.index(min(barato)) 
    continuar = input('Digite novamente, Quer continuar? [S/N] ').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Digite novamente, Quer continuar? [S/N] ').upper()

print(f'O total gasto na compra foi de \033[32mR$\033[m{total:.2f}')
print(f'{produtos} produto(s) custa(m) mais de \033[32mR$\033[m1000.00')
print(f'O produto mais barato é {lista[mais_barato]} custou \033[32mR$\033[m{min(barato):.2f}') 
# lista[mais_barato] PEGA O INDEX DA LISTA E O min(barato) PEGA O MENOR VALOR
# O INDEX RETORNA O PRIMEIRO VALOR, VOU DESCOBRIR AINDA.
# .APPEND DENOVO PARA ADICIONAR CADA PREÇO NA LISTA BARATO
# O .APPEND ADICIONA CADA ITEM ESCRITO NA VARIAVEL NOME DENTRO DA LISTA
# LISTA PARA DEFINIR OS PREÇOS, PARA SABER O MAIS BARATO = barato[]
# LISTA PARA ADICIONAR OS PRODUTOS = lista[]
