'''
Crie um programa que leia varios números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores.
'''

numeros_digitados = soma = media = maior = menor = 0

continuar = 'S'

while continuar == 'S':
    numeros = int(input('Digite um número qualquer: '))
    continuar = input('Quer continuar? [S/N] ').upper()
    numeros_digitados += 1
    soma += numeros
    if numeros_digitados == 1:
        maior = menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
media = soma / numeros_digitados
print(f'O maior número é {maior} e o menor é {menor},\na média entre todos os números digitados é {media:.2f}')