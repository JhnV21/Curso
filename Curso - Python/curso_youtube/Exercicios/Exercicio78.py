'''
Faça um programa que leia 5 valores númericos e guarde-os
em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e
as suas respectivas posições na lista.
'''

valores = []
for v in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {v}: ')))

print(f'O maior valor foi {max(valores)} na posição {valores.index(max(valores))}')
print(f'O menor valor foi {min(valores)} na posição {valores.index(min(valores))}')
