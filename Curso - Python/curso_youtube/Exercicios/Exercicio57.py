'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
novamente até ter um valor correto.
'''
sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = input('[M] - Masculino\n[F] - Feminino\nEscolha uma das opções acima: ').upper()
    if sexo != 'M' and sexo != 'F': ### SE AINDA FOR DIFERENTE DO WHILE, ELE PERGUNTA NOVAMENTE.
        print('Tente novamente, Digite [M/F] para validar: ')
    else:  ### CASO FOR CERTO ELE REGISTRA.
        print(f'Registro feito com Sucesso')

### RESPOSTA PROFESSOR
# sexo = input('Informe seu sexo: [M/F] ').strip().upper()[0]
# while sexo not in 'MmFf':
#     sexo = input('Dados invalidos. Por favor, informe seu sexo: ').strip().upper()[0]
# print(f'Sexo {sexo} registrado com sucesso')