'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120
'''
# fatorial = int(input('Escolha o fatorial: '))
# contador = 0

# while contador < fatorial:
#     calculo = fatorial * (fatorial - contador)
#     contador += 1

# print(contador)
# print(calculo)

# "n! = n · (n-1) · (n-2) … 3 · 2 · 1"

### RESOLUÇÃO PROFESSOR
n = int(input('Digite um número para calcular seu Fatorial: ')) # n é = ao fatorial que quer calcular.
c = n # C é = ao contador q é igual ao N
f = 1 # 
print(f'Calculando {n}! = ', end='')
while c > 0: # Enquanto C for menor que 0, o WHILE É TRUE.
    print(f'{c}', end='') # CONTADOR DE LADO
    print(' x ' if c > 1 else ' = ', end='') # x ENTRE OS NUMEROS DO CONTADOR
    f *= c # CALCULO DE TODOS OS NUMEROS DO FATORIAL
    c -= 1 # CONTADOR REGRESSIVO
print(f'{f}')