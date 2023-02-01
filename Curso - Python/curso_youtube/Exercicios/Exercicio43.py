'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e voce esta Abaixo do Peso.')
elif imc >= 18.5 and imc <= 24.9:
    print(f'Seu IMC é {imc:.2f} e voce esta no Peso Ideal.')
elif imc >= 25 and imc <= 29.9:
    print(f'Seu IMC é {imc:.2f} e voce esta com Sobrepeso.')
elif imc >= 30 and imc <= 39.9:
    print(f'Seu IMC é {imc:.2f} e voce esta com Obesidade.')
else:
    print(f'Seu IMC é {imc:.2f} e voce esta com Obesidade Mórbida.')