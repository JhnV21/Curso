'''
Desenvolva um programa que leia quatro valores
pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''

numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o ultimo número: ')))

print(f'Voce digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
print(f'O valor 3 apareceu na {numeros.index(3)+ 1}ª posição.' if 3 in numeros else 'O número 3 não foi digitado.')
print(f'Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
