'''
Escreva um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuario tentar descobrir
qual foi o número escolhido pelo computador.
O programa devera escrever na tela se o usuario venceu ou perdeu.
'''
import random
numero = random.randint(0,5)
adivinhar = int(input('Tente adivinhar o número: '))
if adivinhar == numero:
    print('Voce ganhou, PARABENS!!!')
else:
    print(f'Voce perdeu o numero era {numero}, HAHAHAHA!!!!.')
print('Acabou.')