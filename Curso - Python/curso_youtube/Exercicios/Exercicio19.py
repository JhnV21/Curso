'''
Um professor que sortear um dos seus
quatro alunos para apagar o quadro. Faça
um programa que ajude ele, lendo o nome deles
e escrevendo o nome do escolhido.
'''

import random

aluno_1 = input('Digite o nome do primeiro aluno: ')
aluno_2 = input('Digite o nome do segundo aluno: ')
aluno_3 = input('Digite o nome do terceiro aluno: ')
aluno_4 = input('Digite o nome do quarto aluno: ')

alunos = aluno_1, aluno_2, aluno_3, aluno_4
sorteador = random.choice(alunos)
print(f'O aluno escolhido foi {sorteador}')