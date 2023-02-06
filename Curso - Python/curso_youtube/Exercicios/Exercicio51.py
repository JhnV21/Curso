'''
Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''
# 4-7-10-13-16-19-22-25-28-31

termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
dez_termos = termo + (10-1) * razao
dez_termos = dez_termos + 1

for t in range(termo, dez_termos, razao):
    print(t)
