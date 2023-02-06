'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas
ja são maiores.
considerando 21 como maior idade
'''
from datetime import date

maior = 0
menor = 0
for ano in range(1, 8):
    nascimento = int(input('Ano de nascimento: '))
    idade = date.today().year - nascimento
    if idade >= 21: 
        maior += 1
    else:
        menor += 1
print(f'{maior} Pessoa(s) é/são maior(es) de 21 anos')
print(f'{menor} Pessoa(s) é/são menor(es) de 21 anos')