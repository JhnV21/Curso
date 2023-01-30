'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
Primeiro: Ana
Ultimo: Souza
'''

nome_completo = input('Digite seu nome completo: ').strip()
dividido = nome_completo.split()
print(f'Seu primeiro nome é {dividido[0]}')
print(f'Seu ultimo nome é {dividido[-1]}')
