'''
Faça um algoritmo que leia o salário
de um funcionário e mostre seu novo salário,
com 15% de aumento.
'''

salario_atual = int(input('Digite seu salário atual: '))
aumento = (salario_atual * 15)/100
salario_novo = salario_atual + aumento

print(f'Seu antigo salário era de R${salario_atual:.2f} e com aumento de 15% foi para R${salario_novo:.2f}')