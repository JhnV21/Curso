'''
Desenvolva um programa que leia o nome, idade e sexo
de 4 pessoas. No final do programa, mostre:
> A média de idade do grupo.
> Qual é o nome do homem mais velho.
> Quantas mulheres tem menos de 20 anos.
'''
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
menos_vinte = 0
for i in range(1,4+1):
    nome = input('Digite seu Nome: ')
    idade = int(input('Digite sua Idade: '))
    sexo = input('[1] - Homem\n[2] - Mulher\nEscolha seu sexo: ')
    somaidade += idade
    if i == 1 and sexo == 1:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 1 and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 2 and idade < 20:
        menos_vinte += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.')
print(f'Ao todo são {menos_vinte} mulheres com menos de 20 anos.')

'''
USAR VARIAVEIS NO INICIO DO CODIGO PARA DEFINIR VALORES, E USAREM DEPOIS PARA MANIPULAR MELHOR NO MEIO DO CODIGO
PARA ADICIONAR VALORES A ESSAS VARIAVEIS E USA-LAS.
'''