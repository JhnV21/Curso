'''
Desenvolva um programa que leia o comprimento de tres retas
e diga ao usuario se elas podem ou nao formar um triangulo.
'''

reta_1 = int(input('Digite o comprimento da Reta 1: '))
reta_2 = int(input('Digite o comprimento da Reta 2: '))
reta_3 = int(input('Digite o comprimento da Reta 3: '))

# TENTATIVA
# calculo_1 = reta_1 + reta_2
# calculo_2 = reta_1 + reta_3
# calculo_3 = reta_3 + reta_2

# if calculo_1 > reta_3:
#     print('Isto é um triangulo.')
# if calculo_2 > reta_2:
#     print('Isto é um triangulo.')
# if calculo_3 > reta_1:
#     print('Isto é um triangulo.')
# else:
#     print('Isto não é um triangulo.')

# CORREÇÃO
if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Isto é um triangulo.')
else:
    print('Isto não é um triangulo.')