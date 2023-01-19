'''
Faça um programa que leia a largura e a 
altura de uma parede em metros, calcule a
sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta,
pinta uma área de 2m².
'''

parede_altura = int(input('Digite a altura da parede em metros: '))
parede_largura = int(input('Digite a largura da parede em metros: '))
area_parede = parede_altura * parede_largura
quantidade_tinta = area_parede / 2

print(quantidade_tinta)


