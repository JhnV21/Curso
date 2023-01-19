'''
Escreva um programa que leia um
valor em metros e o exiba convertido
em centrimetros e milimetros.
'''

metros = int(input('Digite o valor: '))
cm = metros * 100
milimetros = metros * 1000

print(f'Seu valor em metros era {metros}, em centimetros é {cm} cm e milimetros {milimetros} milimetros')