'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
digitados = 0

while True:
    lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r != 'S' and r != 'N':
        r = input('Quer continuar? [S/N] ').upper()
    if r == 'N':
        break

print(f'Quantidade de números digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista em Ordem Decrescente\n{lista}')
if 5 in lista:
    print(f'O número 5 foi digitado e esta na posição {lista.index(5)}')
else:
    print('O número 5 não esta na lista')