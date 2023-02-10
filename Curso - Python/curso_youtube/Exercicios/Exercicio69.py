'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada
pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A> Quantas pessoas tem mais de 18 anos.
B> Quantos homems foram cadastrados.
C> Quantas mulheres tem menos de 20 anos.
'''

menos_20 = homens = mais_18 = 0
continuar = 'S'

while continuar == 'S':
    idade = int(input('Digite sua Idade: '))
    sexo = int(input('[1] - Homem\n[2] - Mulher\nEscolha seu sexo: '))
    if idade >= 18:
        mais_18 += 1
    if sexo == 1:
        homens += 1
    if sexo == 2 and idade < 20:
        menos_20 += 1
    continuar = input('Quer Continuar? [S/N] ').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Quer Continuar? [S/N] ').upper()

print(f'{mais_18} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{menos_20} mulheres tem menos de 20 anos.')