'''
Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "SANTO".
'''

cidade = input('Digite o nome da sua cidade: ').strip()
dividido = cidade.split()
cidade_true = dividido[0].upper() == 'SANTO'
print(cidade_true)
