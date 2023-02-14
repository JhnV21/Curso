'''
Crie um programa que vai gerar cinco números aleatórios
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indique o menor e o maior valor que estão na tupla.
'''

from random import sample

numeros = tuple(sample(range(10), 5))
print(numeros)
print(f'O maior número é o {max(numeros)}')
print(f'O menor número é o {min(numeros)}')

'''só colocar o prefixo tuple() para encapsular as instruções que o sucedem... sample, é como um "looping",
logo ele gera uma lista dos elementos escolhidos através da função range(). Portanto deve-se converter essa lista para tupla.'

É como se fosse um CHOICE em LOOP... Enquanto o CHOICE escolhe somente um único valor do intervalo (ou lista),
o sample você tem a opção de determinar o número de vezes que o mesmo vai te retornar um valor aleatório extraído da lista
'''
