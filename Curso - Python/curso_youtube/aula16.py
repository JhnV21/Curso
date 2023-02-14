lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são imutáveis
# for comida in lanche:
#     print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

# print(sorted(lanche))
# print(lanche)

# a = (2, 5 ,4)
# b = (5, 8, 1, 2)
# c = b + a
# print(c)
# print(c.index(5, 1)) # DESLOCAMENTO # O INDEX MOSTRA A POSIÇÃO DO ELEMENTO ESCOLHIDO ENTRE OS PARENTESES ()

# pessoa = ('João', 20, 'M', 82.23)
# print(pessoa)
# TUPLA É IMUTAVEL ATE SER APAGADA