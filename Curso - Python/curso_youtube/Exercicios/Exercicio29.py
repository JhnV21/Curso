'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''
import random
velocidade = random.randint(60, 130)
# velocidade = float(input('Digite a velocidade do carro: '))
radar = 80
multa = 7.00
calculo_multa = (velocidade - radar) * multa

if velocidade > radar:
    print(f'Voce ultrapassou o limite de {radar}Km/h, \ne foi multado no valor de R${calculo_multa:.2f}')
else:
    print('Voce estava dentro do limite de velocidade.')
print(f'Voce estava a {velocidade}Km/h')