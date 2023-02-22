'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''

lista_numeros = []
while True:
    lista_numeros.append(int(input('Digite um número: ')))
    r = ' '
    while r != 'S' and r != 'N':
        r = input('Quer continuar? [S/N] ').upper().strip()
    if r == 'N':
        print('-' * 40)
        break

pares = []
impares = []
for n in lista_numeros: # PARA CADA VALOR DE N NA LISTA_NUMEROS ELE VERIFICA SE O VALOR É DIVISIVEL POR 2 E SOBRA 0 SE FOR É PAR, CASO CONTRARIO É IMPAR
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Números digitados: {lista_numeros}')
print(f'\033[32mNúmeros pares\033[m: {pares}')
print(f'\033[31mNúmeros impares\033[m: {impares}')
