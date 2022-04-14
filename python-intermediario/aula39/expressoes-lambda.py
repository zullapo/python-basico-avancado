"""
Aula 39 - Expressões lambdas

Também chamadas de funções anônimas, são como uma versão simplificada
de uma função que pode conter apenas uma linha de código (expressão).

Estrutura de uma expressão lambda:

lambda argumentos: expressão
"""


# Função
def mult(n1, n2):
    return n1 * n2


# Lambda
produto = lambda x, y: x * y

print(mult(10, 20))
print(produto(10, 20))


# Exemplo de lambda
lista = [
    ["P1", 9],
    ["P3", 4],
    ["P2", 5]
]


def func(item):
    return item[1]


lista.sort(key=func)
# lista.sort(key=func, reverse=True)

print(lista)

lista.sort(key=lambda i: i[1])

print(lista)
