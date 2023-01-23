kmpdia = float(input('Quantidade de KM percorrido: '))
dias_alugado = float(input('Quantidade de dias Alugado: '))
preco_total = dias_alugado * 60 + kmpdia * 0.15

print(f'O total a pagar é R${preco_total:.2f}')