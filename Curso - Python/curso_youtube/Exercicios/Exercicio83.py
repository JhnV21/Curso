'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta.
'''

expr = input('Digite a expressão: ')
pilha = []
for símb in expr:
    if símb == '(':  # SE O SIMBOLO FOR '('  ELE ADICIONA NA LISTA.
        pilha.append('(')
    elif símb == ')': # SE O SIMBOLO FOR ')' ELE REMOVE O ULTIMO ELEMENTO DA LISTA, QUE NO CASO SERIA O '('.
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')
