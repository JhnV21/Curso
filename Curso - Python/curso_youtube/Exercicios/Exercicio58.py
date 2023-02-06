'''
Melhore o jogo do DESAFIO 28 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.
'''

from random import randint
numero = randint(0,10)
adivinhar = 0
tentativas = 0

while numero != adivinhar:
    adivinhar = int(input('Tente adivinhar o número entre 0 e 10: '))
    if numero == adivinhar:
        print('Voce conseguiu')
    tentativas += 1

print(f'O número que o computador escolheu foi {numero}')
print(f'O seu número de tentativas foi {tentativas}')