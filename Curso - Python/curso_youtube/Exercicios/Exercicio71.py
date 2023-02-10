'''
Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuário qual será o valor a ser sacado(Número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

saque = int(input('Quanto voce quer sacar? \033[32mR$\033[m')) # VALOR QUE QUER SACAR

total = saque # O TOTAL É O VALOR DO SAQUE
notas = 50 # PRIMEIRA NOTA
total_notas = 0 # TOTAL DE NOTAS QUE VAI DAR
while True:
    if total >= notas: # SE O TOTAL FOR MAIOR OU IGUAL AO VALOR DE NOTAS
        total -= notas # ELE VAI REMOVENDO CADA NOTA DE 50 OU OUTRO VALOR
        total_notas += 1 # E VAI ADICIONANDO O TOTAL DE NOTAS QUE VAI DAR
    else:
        if total_notas > 0: # SE O TOTAL DE NOTAS FOR MAIOR QUE 0 ELE MOSTRA
            print(f'Total de {total_notas} notas de R${notas}') 
        if notas == 50: # SE AS NOTAS FOR 50 ELE ATUALIZA O VALOR PARA 20 APOS ACABAR AS NOTAS DE 50 E ASSIM SUCESSIVAMENTE ATE O FIM DO CODIGO
            notas = 20
        elif notas == 20:
            notas = 10
        elif notas == 10:
            notas = 1
        total_notas = 0 # FIM DAS NOTAS
        if total == 0:
            break
print('Fim')
