'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''
maior = 0
menor = 0
for pessoas in range (1, 6):
    peso = float(input('Digite seu peso: '))
# RESOLUÇAO PROFESSOR
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}Kg')
print(f'O menor peso é {menor}Kg')
