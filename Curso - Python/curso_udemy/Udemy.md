# Anotações Python Udemy - Luiz Otávio

### Aula 1
## Comentários e DocStrings
- Tudo que esta depois da (#) é um comentário somente na mesma linha.
- DocString: para mais de uma linha usar (""") ou (''') aspas triplas, o interpretador do python lê. Não pode abrir com aspas duplas e fechar com aspas simples, da mesma forma ao contrario.

### Aula 2
## Função Print
- print(): é usado para exibir coisas na tela.
recebe argumentos, para utilizr 2 argumentos utilizar (,)
- sep=: separar argumentos não nomeados
- end=: final do print
- quebra de linha: \r: Return, \n: Line Feed

### Aula 3
## Tipagem, strings e aspas
- string: textos, sempre colocados nas aspas simples ou duplas.
- escapes: \" ou (r)

### Aula 4 
## Tipos int e float
- int: qualquer número negativo ou positivo sem ponto.
- float: número com ponto flutuante, que tem casa decimal
sempre usar "." para separar casas decimais
tudo em python é um objeto

### Aula 5
## bool (boolean)
- ==: checa se um valor é igual a outro.
- tipo de dado booleano apenas para questionar ao programa Sim ou Não(True ou False).

### Aula 6
## Coerção de tipos(converter um tipo em outro)
- tipos imutáveis e primitivos: str, int ,float e bool.
usar as classes: str, int, float e bool para converter algo
exemplo: int('1'), str(11)

### Aula 7
## Variaveis em Python
- Variáveis: são usadas para salvar algo na memória do computador.
- =: sinal de atribuição.
variavel nao sao usadas para abreviar código, sao usadas para fazer o código legivel e para nao repetir coisas aonde vai se utilizar em varios outro lugares.

### Aula 8
## Exercicio
FEITO

### Aula 9
## Operadores aritméticos
- +: adição, -: subtração
- *: multiplicação, /: divisão
- //: divisão inteira, **: exponenciação/potenciação(numero elevado a outro)
- %: módulo(resto da divisão)/(saber se um número é divisivel por outro = 0 ou Par ou Impar)

### Aula 10
## Concatenação e repetição com operadores aritméticos
concatenação somente com strings para unir valores.

### Aula 12
## Exercicio
FEITO

### Aula 13
## Introdução a F-Strings
sempre que tiver f atras de strings, é uma F-String
- :.2f: casas decimais.

### Aula 14
## Formatação de strings com método format
quando uma função esta dentro de um objeto, ela é chamada de método


### Aula 15
## Como usar Input
- input: é um função que pergunta dados ao usuario.

### Aula 16 - 18
## if, elif e else + debugger do vscode
ELIF e ELSE dependem do IF, o único que pode ficar sozinho é o IF.
- if: só executa se a condição for verdadeira.
- elif: só executa se o if for falso e a condição do elif for verdadeira.
- else: só executa se a condição for falsa.

elif pode ser usado quantas vezes quiser.

### Aula 19
## Operadores de comparação
- (>): checa se é maior
- (>=): checa se é maior ou igual
- (<): checa se é menor
- (<=): menor ou igual
- (= ou ==): checa se é igual
- (!=): checa se é diferente

### Aula 20
## Exercicio
FEITO

### Aula 21 - 24
## Operadores Lógicos (and, or, not, in e not in)
- and: usado para checar mais de uma condição, caso qualquer valor for falso, tudo sera considerado falso.
- falsy: 0, 0.0 e ' ', valores falsos.
- None: um não valor.
- or: contrario do and, qualquer condição que for verdadeira, tudo sera considerado verdadeiro
- not: inverte expressões, oque for True é False, oque for False é True.
- in: checa se algo esta na variavel.
- not in: contrario de "in", checa se algo não esta na variavel.

### Aula 25
## Interpolação básica de strings
- %: utilizada com tipos. exemplos: s - string, f - float. %s e %f

### Aula 26
## Formatação básica de strings
para preencher caracteres utilizar
- >: preenche caracteres a esquerda
- <: preenche caracteres a direita
- ^: centraliza 
- =: força o número a aparecer antes dos zeros 

### Aula 27
## Fatiamento de Strings
- [i:f:p]: utilizar [::] para ir ao indice
- len: conta os caracteres da string(conta os espaços também).

### Aula 28
## Exercicio
FEITO

### Aula 29
## Introdução ao try/except
- try: tenta executar o código e qualquer tipo de erro ele captura e voce faz algo.
- isdigit: checa se o usúario digitou apenas números.(retorna bool)


### Aula 30 - 31
## Variáveis, constantes e complexidade de código
- CONSTANTE: qualquer coisa que não for pra mudar colocar em letras maiusculas.








### Aula While 34 - 42
## While, break e continue
- while: executa uma ação enquanto uma condição for verdadeira.
- break: quebra o laço / termina.
- se inverter o print com a condiçao, ele mostra o texto primeiro depois atribui mais valores.
- = += -= *= /= //= **= %=
- 
