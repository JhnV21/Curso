'''
Faça um programa que leia um ano e mostre se ele é BISSEXTO.
'''
ano = int(input('Digite um ano para saber se é bissexto: '))
calculo = ano % 4
# calculo_2 = ano % 100
# calculo_3 = ano % 400

if calculo == 0:
    print(f'O ano de {ano} é bissexto.')
else:
    print(f'O ano de {ano} não é bissexto.')

'''
CORREÇAO: calculo == 0 and calculo_2 != 0 or calculo_3 == 0
'''