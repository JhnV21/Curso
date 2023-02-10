'''
Crie um programa que leia vários números inteiros pelo teclado. O programa
só vai parar quando o usuário digitar o valor 999, que é a condição
de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.(Desconsiderando a flag.)
'''
n = s = c = 0 # N é numeros digitados, S é a soma deles e C é o contador que vai mostrar quantos numeros foram digitados.
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} e a soma entre todos é {s}')