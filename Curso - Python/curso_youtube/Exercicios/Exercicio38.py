'''
Escreva um programa que leia dois números inteiros e
compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior.
- Não existe valor maior, os dois são iguais.
'''

numero_1 = float(input('Digite um número: '))
numero_2 = float(input('Digite outro número: '))

if numero_1 > numero_2:
    print(f'{numero_1} é maior que {numero_2}.')
elif numero_2 > numero_1:
    print(f'{numero_2} é maior que {numero_1}.')
else:
    print('Não existe valor maior, os dois são iguais.')