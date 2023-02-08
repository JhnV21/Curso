'''
Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando a flag).
'''

digitados = numero = soma = 0

while numero < 999:
    numero = int(input('Digite um número: '))
    digitados += 1
    soma += numero

print(f'Foram digitados {digitados} números e a soma entre todos os eles é {soma}')

### RESOLUÇÃO PROFESSOR
# digitados = numero = soma = 0
# numero = int(input('Digite um numero: '))
# while numero != 999:
#     digitados += 1
#     soma += numero
#     numero = int(input('Digite um numero: '))
# print(f'Voce digitou {digitados} números e a soma entre eles é {soma}.')
