'''
Crie um programa que leia
quanto dinheiro uma pessoa tem
na carteira e mostre quantos
Dólares ela pode comprar.
'''

real = int(input('Digite o valor que voce tem na carteira: '))
dolar = real / 5.21

print(f'Voce tem R${real} e convertido para dolar tem ${dolar:.2f}')