"""
Aula 10 - Estruturas condicionais (if, elif e else)

Uma estrutura condicional determina por meio de condições,
se um bloco de código deve ser executado ou não.

Estrutura de um bloco if:

se condicao1
entao codigo1

Estrutura de um bloco if/else:

se condicao1
entao codigo1
senao codigo2

Estrutura de um bloco if/elif/else:

se condicao1
entao codigo1
senao se condicao2
entao codigo2
senao codigo3

Em um bloco if, se a condição for verdadeira, o bloco de código é executado.

Em um bloco if/else, se a condição do if for falsa, o bloco else será executado.

Em um bloco if/elif/else, se a condição do if for falsa, o bloco elif será checado
se for falso, o bloco else será executado.
"""

num = bool(input("Digite 0 ou 1: "))

if num:
    print("Verdadeiro")

if num:
    print("Verdadeiro")
elif num:
    print("Falso")
else:
    print("Falso")

if num:
    print("Verdadeiro")
else:
    print("Falso")
