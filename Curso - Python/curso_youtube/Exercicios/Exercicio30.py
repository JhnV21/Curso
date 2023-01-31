'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
'''

numero = int(input('Digite um número: '))
par_impar = numero % 2

if par_impar == 0:
    print('Este número é par')
else:
    print('Este número é impar')