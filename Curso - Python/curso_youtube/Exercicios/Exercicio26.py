'''
Faça um programa que leia uma frase pelo teclado e mostre:
> Quantas vezes aparece a letra "A".
> Em que posição ela aparece a primeira vez.
> Em que posição ela aparece a última vez.
'''
frase = input('Digite uma frase: ').strip().lower()
print(f'A letra "A" aparece {frase.count("a")} vezes na frase.')
print(f'A primeira letra "A" esta no índice: {frase.find("a") +1}')
print(f'A ultima letra "A" esta no índice: {frase.rfind("a") +1}')