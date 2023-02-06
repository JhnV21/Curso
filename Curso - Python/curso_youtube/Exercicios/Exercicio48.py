'''
Faça um programa que calcule a soma entre todos os
números impares que são múltiplos de três e que se
encontram no intervalo de 1 até 500.
'''
soma = 0
for i in range(1, 500, 2):
    impar = i % 3
    if impar == 0:
        soma += i
print(soma)

# CALCULOS
# n = qualquer numero
# t = n % 3
# if t == 0:
#     print(t)

# 3,6,9,12,15, 18, 21, 24, 27, 30, 33, 36, 39