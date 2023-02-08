'''
Escreva um programa que leia um número n inteiro qualquer e mostre
na tela os n primeiros elementos de uma sequencia de Fibonacci.
Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

n = n - 1 + n - 2
'''

# numero = int(input('Digite um número: '))
# contador = 0

# while contador < numero:
#     contador += 1
#     calculo = numero - contador + numero - contador
# print(calculo)

n = int(input('Quantos termos voce quer mostrar? '))# QUANTIDADE DE TERMOS
t1 = 0 # OS TERMOS SEMPRE INICIAM COM 0 E 1 - TERMO 1
t2 = 1 # TERMO 2
print(f'{t1} - {t2}', end='') # ELE MOSTRA OS PRIMEIROS TERMOS
cont = 3 # CONTADOR INICIA DE 3 PORQUE JA MOSTROU O 1 E O 2
while cont <= n: # ENQUANTO O CONTADOR FOR MENOR OU IGUAL A QUANTIDADE DE TERMOS QUE O USUARIO ESCOLHER ELE VAI RODAR.
    t3 = t1 + t2 # O TERMO 3 É O TERMO 1 + TERMO 2
    print(f' - {t3}', end='') # AQUI ELE MOSTRA O 3 TERMO
    t1 = t2 # O TERMO 2 PASSA A SER O TERMO 1
    t2 = t3 # O TERMO 3 PASSA A SER O TERMO 2
    cont += 1 # CONTADOR SEMPRE ADICIONANDO MAIS TERMOS ATE SER MENOR OU IGUAL AO NUMERO DE TERMOS ESPECIFICADO.
print(' - FIM')