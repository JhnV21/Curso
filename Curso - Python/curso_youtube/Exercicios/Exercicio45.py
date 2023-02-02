'''
Crie um programa que faça o computador jogar Jokenpo com voce.
'''

from random import randint
from time import sleep
mao = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('0 - Pedra\n1 - Papel\n2 - Tesoura\nEscolha sua opção: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('=-='* 10)
print(f'Computador escolheu {mao[computador]}')
print(f'Voce escolheu {mao[jogador]}')
print('=-='* 10)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU')
    elif jogador == 2:
        print('COMPUTADOR VENCEU')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU')
    elif jogador == 1:
        print('COMPUTADOR VENCEU')
    elif jogador == 2:
        print('EMPATE')
else:
    print('Opção invalida')