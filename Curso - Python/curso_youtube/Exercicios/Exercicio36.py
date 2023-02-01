'''
Escreva um programa para aprovar o empréstimo bancário para
a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então
o emprestimo será negado.
'''

valor_casa = float(input('Digite o valor da casa: ').strip())
salario = float(input('Digite seu sálario: ').strip())
anos = int(input('Em quantos anos pretende pagar? ').strip()) * 12

prestacao_mensal = valor_casa / anos
if prestacao_mensal > salario * 0.3:
    print(f'Seu emprestimo foi negado, pois o valor da prestação mensal excedeu os 30% do seu salario R${salario:.2f}.')
else:
    print(f'PARABENS!!!, Seu emprestimo foi aprovado, no valor de R${prestacao_mensal:.2f} todo mes.')