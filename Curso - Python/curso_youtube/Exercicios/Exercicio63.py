'''
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma sequencia de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

Fn = Fn - 1 + Fn - 2
'''

numero = int(input('Digite um número: '))
contador = 0

while contador < numero:
    contador += 1
    calculo = numero - contador + numero - contador
print(calculo)
