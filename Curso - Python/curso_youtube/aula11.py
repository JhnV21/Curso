# print('\033[0;30;47mOlá, Mundo!\033[m')
# print('\033[1;31;46mOlá, Mundo!\033[m')
# print('\033[4;32;45mOlá, Mundo!\033[m')
# print('\033[7;33;44mOlá, Mundo!\033[m')
# print('\033[0;34;43mOlá, Mundo!\033[m')
# print('\033[1;35;42mOlá, Mundo!\033[m')
# print('\033[4;36;41mOlá, Mundo!\033[m')
# print('\033[7;37;40mOlá, Mundo!\033[m')

# a = 11
# b = 7
# print(f'Os valores são \033[32m{a}\033[m e \033[7;30;47m{b}')

cores = {'limpar':'\033[m', 'verde':'\033[32;40m', 'azul':'\033[34;40m'}
print(f'{cores["verde"]}Verde{cores["limpar"]}')