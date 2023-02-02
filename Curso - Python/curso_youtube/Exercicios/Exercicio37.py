'''
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
'''

# numero = int(input('Digite qualquer número: '))
# ...

numero = int(input('Digite um número inteiro: '))
conversao = int(input('Escolha o metodo de conversão\n1 - \033[32mBinário\033[m\n2 - \033[34mOctal\033[m\n3 - \033[31mHexadecimal\033[m\nPara qual voce quer converter: '))

if conversao == 1:
    print(f'O número {numero} convertido para Binário é \033[32m{numero:b}\033[m')
elif conversao == 2:
    print(f'O número {numero} convertido para Octal é \033[34m{numero:o}\033[m')
elif conversao == 3:
    print(f'O número {numero} convertido para Hexadecimal é \033[31m{numero:X}\033[m')
else:
    print('Número invalido')