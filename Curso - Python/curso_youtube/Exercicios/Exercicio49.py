'''
Refaça o Exercicio 9, mostrando a tabuada de um número que o usúario
escolher, só que agora utilizando um laço FOR.
'''

tabuada = int(input('Qual tabuada voce quer? '))
for n in range(0, 11):
    print(f'{tabuada} x {n} = {tabuada * n}')
print('Fim!!')