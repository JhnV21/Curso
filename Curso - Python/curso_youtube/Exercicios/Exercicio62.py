'''
Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais
alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
'''

### RESOLUÇÃO PROFESSOR
primeiro = int(input('Primeiro termo: ')) # PRIMEIRO TERMO DA RAZAO
razao = int(input('Razão da PA: ')) # DE QUANTOS EM QUANTOS O NUMERO VAI PULAR
termo = primeiro # É APENAS O PRIMEIRO TERMO NA VARIAVEL
cont = 1 # CONTADOR QUE INICIA DO 1
total = 0 # ESSE TOTAL
mais = 10 # ESSE MAIS AGORA PASSA 
while mais != 0:
    total += mais
    while cont <= total: # ENQUANTO O CONTADOR FOR MENOR Q O NUMERO DE RAZOES QUE É 10 ELE MOSTRARA
        print(f'{termo} - ', end='') # PRINT DOS TERMOS 1 A 1 ATE ACABAR O WHILE
        termo += razao # CALCULO TERMO + RAZAO QUE É ONDE PULA 
        cont += 1 # CONTADOR ATE 10 QUE É O NUMERO DE TERMOS QUE QUEREMOS
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')