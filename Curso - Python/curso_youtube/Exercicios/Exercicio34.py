'''
Escreva um programa que pergunte o salario de  um funcionario
e calcule o valor do seu aumento.
Para salarios superiores a R$1,250.00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('Digite seu salário R$'))
aumento_10 = (salario * 10)/100
aumento_15 = (salario * 15)/100

if salario > 1250:
    novo_salario_10 = salario + aumento_10
    print(f'Seu novo salário sera R${novo_salario_10:.2f}')
else:
    novo_salario_15 = salario + aumento_15
    print(f'Seu novo salário sera R${novo_salario_15:.2f}')