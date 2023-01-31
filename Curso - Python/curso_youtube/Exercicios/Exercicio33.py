'''
Faça um programa que leia três números e mostre qual é o
maior e qual é o menor.
'''
# TENTATIVA
numero_1 = float(input('Número um: '))
numero_2 = float(input('Número dois: '))
numero_3 = float(input('Número tres: '))

# if numero_1 > numero_2 and numero_1 > numero_3:
#     print(f'{numero_1} é o maior')
# elif numero_2 > numero_1 and numero_2 > numero_3:
#     print(f'{numero_2} é o maior')
# else:
#     print(f'{numero_3} é o maior.')


# CORREÇÃO
menor = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3

maior = numero_1
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')