'''
Faça um programa que leia o comprimento do cateto
adjacente de um triangulo retangulo, calcule
e mostre o comprimento da hipotenusa.
'''
from math import hypot

cateto_oposto = float(input('Digite um valor: '))
cateto_adjacente = float(input('Digite outro valor: '))
# hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** 0.5
# print(f'A hipotenusa é {hipotenusa:.2f}')
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa é {hipotenusa:.2f}')


