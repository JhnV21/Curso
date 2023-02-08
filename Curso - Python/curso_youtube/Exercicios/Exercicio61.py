'''
Refaça o DESAFIO 51, lendo o primeiro termo e a razao de uma PA, mostrando
os 10 primeiros termos da progressão usando a estrutura while.
'''

# termo = 0
# razao = 0
# dez_termos = termo + (10-1) * razao
# dez_termos = dez_termos + 1
# termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razão da PA: '))

# while dez_termos != 0:
#     ...

### RESOLUÇÃO PROFESSOR
primeiro = int(input('Primeiro termo: ')) # PRIMEIRO TERMO DA RAZAO
razao = int(input('Razão da PA: ')) # DE QUANTOS EM QUANTOS O NUMERO VAI PULAR
termo = primeiro # É APENAS O PRIMEIRO TERMO NA VARIAVEL
cont = 1 # CONTADOR Q INICIA DO 1
while cont <= 10: # ENQUANTO O CONTADOR FOR MENOR Q O NUMERO DE RAZOES QUE É 10 ELE MOSTRARA
    print(f'{termo} - ', end='') # PRINT DOS TERMOS 1 A 1 ATE ACABAR O WHILE
    termo += razao # CALCULO TERMO + RAZAO QUE É ONDE PULA 
    cont += 1 # CONTADOR ATE 10 QUE É O NUMERO DE TERMOS QUE QUEREMOS
print('FIM')