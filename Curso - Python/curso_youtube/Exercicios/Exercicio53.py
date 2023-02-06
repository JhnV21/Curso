'''
Crie um programa que leia uma frase qualquer e diga se ela
é palindromo, desconsiderando os espaços.
'''

frase = input('Digite uma frase: ').strip().upper()
juntado = frase.replace(' ','')
contrario = (juntado[::-1])

if juntado == contrario:
    print(f'A frase \033[31m{frase}\033[m é um Palindromo')
else:
    print(f'A frase \033[31m{frase}\033[m não é um Palindromo')
