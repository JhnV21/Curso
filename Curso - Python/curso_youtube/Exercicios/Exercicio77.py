'''
Crie um programa que tenhas uma tupla com várias
palavras (não usar acentos). Depois disso, você
deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('Ovo', 'Caderno', 'Orelha', 'Televisao')
for p in palavras: # ANALISA CADA PALAVRA NA TUPLA
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: # ANALISA CADA LETRA DA PALAVRA E VERIFICA SE TEM O AEIOU
        if letra.lower() in 'aeiou':
            print(letra, end=' ')