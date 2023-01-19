'''
Faça um algoritmo que leia
o preço de um produto e mostre
seu novo preço, com 5% de desconto.
'''

preco_sem_desconto = int(input('Digite o preço sem desconto: '))
desconto = (preco_sem_desconto * 5)/100
preco_com_desconto = preco_sem_desconto - desconto

print(f'O preço original é R${preco_sem_desconto:.2f} e com desconto de 5% é R${preco_com_desconto:.2f}')