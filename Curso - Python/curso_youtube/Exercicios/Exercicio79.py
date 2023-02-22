'''
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista.
Caso o número ja exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

numeros = []

while True:
    n = int(input('Digite um valor: '))
    if n in numeros: # SE O VALOR DIGITADO NO INPUT JA FOI DIGITADO ANTERIORMENTE ELE NAO VAI DAR APPEND NO VALOR
        print('Valor ja adicionado anteriormente, excluido.')
    else: # SE O VALOR NAO FOI DIGITADO AINDA ELE DA APPEND.
        numeros.append(n)
    r = ' '
    while r != 'S' and r != 'N':
        r = input('Quer continuar ? [S/N] ').upper().strip()
    if r == 'N':
        break

numeros.sort()
print(f'Números em Ordem Crescente: {numeros}')
