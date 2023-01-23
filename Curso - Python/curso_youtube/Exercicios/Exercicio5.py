'''
Faça um programa que leia um número
Inteiro e mostra na tela seu sucessor
e antecessor.
'''

numero_atual = int(input('Digite um número: '))
numero_antecessor = numero_atual - 1
numero_sucessor = numero_atual + 1

print(f'Voce digitou {numero_atual}, o antecessor é {numero_antecessor} e o sucessor é {numero_sucessor}.')