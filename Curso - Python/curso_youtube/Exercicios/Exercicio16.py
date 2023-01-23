'''
Crie um programa que leia um número Real
qualquer pelo teclado e mostre na tela a sua
porção inteira.
'''
from math import floor
numero = float(input('Digite um número: '))
arredondado = floor(numero)
print(f'Seu número arredondado é {floor(numero)}')
