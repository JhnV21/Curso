'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o
recurso de mostrar que tipo de triângulo será formado:

- Equilatero: todos os lados iguais.
- Isósceles: dois lados iguais.
- Escaleno: todos os lados diferentes.
'''

reta_1 = int(input('Digite o primeiro segmento: '))
reta_2 = int(input('Digite o segundo segmento: '))
reta_3 = int(input('Digite o terceiro segmento: '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:
    print('Os segmentos acima pode formar um triangulo ', end='')
    if reta_1 == reta_2 == reta_3:
        print('Equilátero')
    elif reta_1 != reta_2 != reta_3 != reta_1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Os segmentos acima não podem formar um triangulo.')
