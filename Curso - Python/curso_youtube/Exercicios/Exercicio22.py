'''
Crie um programa que leia o nome completo
de uma pessoa e mostre:
> O nome com todas as letras maiúsculas.
> O nome com todas minúsculas.
> Quantras letras ao todo(sem espaços).
> Quantas letras tem o primeiro nome.
'''
nome = input('Digite seu nome completo: ').strip()
nome_sem_espacos = nome.replace(' ','')
dividido = nome.split()
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome tem {len(nome_sem_espacos)} letras sem espaços')
print(f'Seu primeiro nome tem {len(dividido[0])} letras')
