'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
'''
from datetime import date

nascimento = int(input('Ano de Nascimento: '))
idade = date.today().year - nascimento

if idade <= 9:
    print(f'Voce tem {idade} anos sua Categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print(f'Voce tem {idade} anos sua Categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print(f'Voce tem {idade} anos sua Categoria: JUNIOR')
elif idade > 19 and idade <= 20:
    print(f'Voce tem {idade} anos sua Categoria: SÊNIOR')
else:
    print(f'Voce tem {idade} anos sua Categoria: MASTER')