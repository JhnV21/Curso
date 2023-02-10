'''
Faça um programa que jogue par ou ímpar com o computador. O jogo
só será interrompido quando o jogador PERDER, mostrando o total de vitórias
consecutivas que ele conquistou no final do jogo.
'''
from random import randint
from time import sleep

v = 0 # VITORIAS

while True:
    c = randint(0, 10) # COMPUTADOR
    n = int(input('Escolha um número: ')) # USUARIO
    s = c + n
    par_impar = s % 2 # CALCULO PAR IMPAR
    p_i = input('Escolha Par ou Impar: [P/I] ').upper()
    while p_i != 'I' and p_i != 'P':
        p_i = input('Opção invalida. Escolha Par ou Impar: [P/I] ').upper()

    sleep(0.5)
    if par_impar == 1:
        if p_i == 'I':
            par_impar = 'Impar'
            print(f'Voce jogou {n} e o Computador jogou {c}. Total é {s} e deu {par_impar}')
            print('Ganhou')
            v += 1
    if par_impar == 0:
        if p_i == 'P':
            par_impar = 'Par'
            print(f'Voce jogou {n} e o Computador jogou {c}. Total é {s} e deu {par_impar}')
            print('Ganhou')
            v += 1
    if par_impar == 1:
        if p_i == 'P':
            par_impar = 'Impar'
            print(f'Voce jogou {n} e o Computador jogou {c}. Total é {s} e deu {par_impar}')
            print('Voce PERDEU')
            break
    if par_impar == 0:
        if p_i == 'I':
            par_impar = 'Par'
            print(f'Voce jogou {n} e o Computador jogou {c}. Total é {s} e deu {par_impar}')
            print('Voce PERDEU')
            break
    
print(f'Ganhou {v}x seguidas.')



### RESOLUÇÃO PROFESSOR SIMPLIFICADA
# if p_i == 'P':
#     if s % 2 == 0:
#         print('Voce VENCEU')
#         v += 1
#     else:
#         print('Voce PERDEU')
#         break
# elif p_i == 'I':
#     if s % == 1:
#         print('Voce VENCEU')
#         v += 1
#     else:
#         print('Voce PERDEU')
#         break