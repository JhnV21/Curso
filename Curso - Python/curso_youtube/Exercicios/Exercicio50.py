'''
Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
'''
soma = 0
for i in range(0, 6):
    numero = int(input('Digite um número: '))
    par = numero % 2
    if par == 0:
        soma += numero
print(soma)