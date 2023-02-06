'''
Crie um programa que leia dois valores e mostre um menu na tela:

1 - somar
2 - multiplicar
3 - maior
4 - novos números
5 - sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep

valor_1 = int(input('Digite um número: '))
valor_2 = int(input('Digite outro número: '))
opcao = 0
while opcao != 5:
    opcao = int(input('[1] - Somar\n[2] - Multiplicar\n[3] - Maior\n[4] - Novos números\n[5] - Sair do programa\nEscolha uma das opções: '))
    if opcao == 1:
        print('CALCULANDO...')
        sleep(1)
        print(f'A soma de {valor_1} + {valor_2} é \033[32m{valor_1 + valor_2}\033[m')
        sleep(1)
    elif opcao == 2:
        print('CALCULANDO...')
        sleep(1)
        print(f'A multiplicação de {valor_1} x {valor_2} é \033[32m{valor_1 * valor_2}\033[m')
        sleep(1)
    elif opcao == 3:
        sleep(1)
        if valor_1 > valor_2:
            print(f'O \033[32m{valor_1}\033[m é o maior')
        elif valor_2 > valor_1:
            print(f'O \033[32m{valor_2}\033[m é o maior')
        else:
            print(f'Os números {valor_1} e {valor_2} são iguais.')
        sleep(1)
    elif opcao == 4:
        sleep(1)
        print('Escolha novos números.')
        valor_1 = int(input('Digite um número: '))
        valor_2 = int(input('Digite outro número: '))
        sleep(1)
    elif opcao == 5:
        sleep(0.5)
        print('Fim do programa')
    else:
        print('Escolha uma opção valida')
        sleep(0.5)