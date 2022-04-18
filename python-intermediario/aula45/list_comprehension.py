"""
Aula 45 - Compreensão de lista (List Comprehension)

Sintaxe simplificada para criação de listas, geralmente composta por
um for loop que retorna os elementos para preeenchimento.
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Preenchendo uma lista com elementos de outra lista:
ex1 = [i for i in l1]

print(ex1)

# Preenchendo uma lista com cada elemento multiplicado por 2:
ex2 = [i * 2 for i in l1]

print(ex2)

# Criando uma matriz através de for loops aninhados:
ex3 = [(i, j) for i in l1 for j in range(3)]

print(ex3)

# Mais exemplos do mesmo:
l2 = ["lUiZ", "mAuro", "maria"]

ex4 = [i.capitalize() for i in l2]

print(ex4)

tupla = (
    ("chave", "valor"),
    ("chave2", "valor2"),
)

ex5 = [(v, k) for k, v in tupla]

print(ex5)
print(dict(ex5))

# Números pares de 0 a 100 (if):
l3 = list(range(100))

ex6 = [i for i in l3 if i % 2 == 0]

print(ex6)

# FizzBuzz de 0 a 100:
ex7 = [f"FizzBuzz: {i}" for i in l3 if i % 3 == 0 and i % 5 == 0]

print(ex7)

# Mostre o número e se ele é par ou impar (if/else):
# O for loop deve ficar após o else.
ex8 = [f"Par: {i}" if i % 2 == 0 else f"Ímpar: {i}" for i in l3]

print(ex8)
