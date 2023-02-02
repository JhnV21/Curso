'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- A vista dinheiro/cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartao: 20% de juros 
'''

valor_produto = float(input('Digite o valor do produto: '))
pagamento = int(input('-=-=-=Métodos de Pagamento-=-=-=\n1 - Dinheiro/Cheque \n2 - Cartão Débito\n3 - Até 2x Cartão\n4 - 3x ou Mais no Cartão\nEscolha o método de pagamento: '))
dinheiro_cheque = valor_produto - valor_produto * 0.1 # 10% DESCONTO
debito = valor_produto - valor_produto * 0.05 # 5% DESCONTO
juros = (valor_produto * 0.2) + valor_produto

if pagamento == 1:
    print(f'Voce ganhou 10% desconto por escolher esse metódo de pagamento, valor total ficou R${dinheiro_cheque:.2f}')
elif pagamento == 2:
    print(f'Voce ganhou 5% desconto por escolher esse metódo de pagamento, valor total ficou R${debito:.2f}')
elif pagamento == 3:
    print(f'Voce não ganha desconto, valor R${valor_produto:.2f}')
elif pagamento == 4:
    print(f'3x ou Mais no Cartão voce paga juros de 20%, valor total ficou R${juros:.2f}')