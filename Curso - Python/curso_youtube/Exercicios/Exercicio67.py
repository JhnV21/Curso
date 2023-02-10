'''
Faça um programa que mostre a tabuada de vários números,
um de cada vez, para cada valor digitado pelo usuário. O programa
será interrompido quando o número solicitado for negativo.
'''
c = 1 # C é o contador que inicia em 1.
while True:
    n = int(input('Qual tabuada voce quer? ')) # N é o numero da tabuda quer o usuario quer.
    if n < 0: # Se N for negativo o programa para.
        break
    for c in range(1,11): # NAO SABIA, Para cada C = Contador no intervalo de 1 a 11, ele faz a repetição
        print(f'{n} x {c} = {n * c}')
print('Fim')