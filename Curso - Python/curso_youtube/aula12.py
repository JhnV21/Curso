import emoji

nome = input('Qual seu nome: ')

if nome == 'João':
    print('😁')
elif nome == 'Heloisa' or 'Michelle' or 'Claudete':
    print('😀')
elif nome in 'Elif Quantas Vezes Quiser':
    print('😎')
else:
    print('😐!!')
print(f'Tenha um bom dia {nome}')

'''
CONDIÇÃO ANINHADA 
'''