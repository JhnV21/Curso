'''
Desenvolva um programa que pergunte a distancia de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de ate 200Km
e R$0,45 para viagens mais longas.
'''

distancia = float(input('Digite a distancia em KM: '))
distancia_200 = distancia * 0.5
distancia_maior = distancia * 0.45

if distancia <= 200:
    print(f'O valor da sua passagem é R${distancia_200:.2f}')
else:
    print(f'O valor da sua passagem é R${distancia_maior:.2f}')