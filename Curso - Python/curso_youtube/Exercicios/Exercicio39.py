'''
Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta
ou que passou do prazo.
'''
from datetime import date

nascimento = int(input('Digite seu ano de nascimento: '))
data_atual = date.today().year
idade = data_atual - nascimento

if idade <= 17:
    saldo = 18 - idade
    print(f'Voce ainda vai se alistar, faltam {saldo} ano(s).')
elif idade == 18:
    print('Voce esta no prazo de alistamento, se aliste JÁ!!!')
else:
    saldo = idade - 18
    print(f'Voce ja passou do tempo do alistamento, deveria ter se alistado a {saldo} ano(s).')
