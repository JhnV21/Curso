# - list.append(x): Adiciona um item ao fim da lista.
# - 
# list.insert(i, x): Insere um item em uma dada posição i.
# - 
# del(): Deleta um elemento da lista ou a própria lista.

# - list.pop(i): Remove o item de posição i da lista e o retorna. Caso i não seja especificado, retorna o último elemento da lista.
# - 
# list.remove(x): Remove o primeiro elemento, cujo valor seja x.

# - list.clear(): Remove todos os elementos da lista.

# - list.index(x[, start[, end]]): Retorna o índice do primeiro elemento cujo valor seja x.

# - list.count(x): Retorna o número de vezes que o valor x aparece na lista.

# - list.sort(key=None, reverse=False): Ordena os items da lista (os argumentos podem ser usados para customizar a ordenação).
# - 
# list.reverse(): Reverte os elementos da lista.
# - list.copy(): Retorna uma lista com a cópia dos elementos da lista de origem.

# lanche = list[]
# lanche.append('valor') #inclui valor na última posição
# lanche.insert(0,'valor') #substitui valor na posição '0'
# del lanche[3]
# lanche.pop() #elimina o último e reposiciona os valores na lista
# if 'valor' in lanche: #evita msg de erro
#   lanche.remove('valor') #evita msg de erro
# lista2 = list(range(4,11)) #lista2 = [4,5,6,7,8,9,10]
# lista3 = [8,5,4,3,0]
# lista3.sort() #ordenar valores [0,3,4,5,8]
# lista3.sort(reverse=True) #ordenar valores de forma inversa [8,5,4,3,0]
# len(lista3) # resposta: 5


# num = [2, 5, 9, 1]
# num[2] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# if 5 in num:
#     num.remove(5)
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))

# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Fim')

a = [2, 3, 4, 7]
b = a[:] # COPIA de A
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
