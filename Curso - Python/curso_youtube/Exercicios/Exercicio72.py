'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo
por extenso.
'''

numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 
'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

escolha = 0
while True:
    escolha = int(input('Digite um número entre 0 e 20: '))
    if escolha < 0 or escolha > 20:
        print('Número invalido.')  
    elif escolha in range(0, 21):
        print(f'Voce digitou o número {numeros[escolha]}')

