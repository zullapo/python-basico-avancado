"""
Aula 43 - Sets (Conjuntos)

Coleção de dados que tem como seus elementos não-indexáveis, não-duplicáveis e
imutáveis. Porém, o conjunto em si é mutável, ou seja, é possível adicionar ou
remover elementos.

Há como realizar operação de conjuntos: união, interseccção e diferença.
"""

# Não é permitido adicionar elementos mutáveis:
# c1 = {[1,2,3]}
# c1 = {{"A": 1, "B": 2, "C": 3}}

c1 = {1, 2, 3, 4, 5}

print(c1)

print()

# Não há como criar um conjunto vazio, pois o interpretador entende como dict:
# c2 = {}
# print(c2, type(c2))

# Use a função set para criar um conjunto vazio:
c2 = set()

# Operações com elementos de conjunto:

# Adição de elementos (add):
c2.add(1)
c2.add(2)
c2.add(3)

print(c2)

# Remoção de elementos (discard):
c2.discard(3)

print(c2)

# Adição de múltiplos elementos a partir da união (update)
c2.update({3, 4, 5})  # Não repete o 3

print(c2)


# Esvaziando conjuntos (clear):
c2.clear()

print(c2)

c2.update("Python")  # Adiciona letra por letra, de forma não ordenada.

print(c2)

# Conversão de lista para conjunto, utilizada para remover elementos duplicados:
l1 = [1, 2, 3] * 3 + ["Python", "C++"]

print(l1)

c3 = set(l1)

print(c3)

print()

# Operações entre conjuntos:
c1 = {0, 1, 2}
c2 = {1, 2, 3}

print("Conjuntos:")
print("C1 =", c1)
print("C2 =", c2)

print()

# União (|):
# Soma dos conjuntos com elementos não-duplicados
c3 = c1 | c2
c3 = c1.union(c2)

print("União:")
print("C1 =", c1)
print("C2 =", c2)
print("C3 (Resultado) =", c3)

print()

# Intersecção (&):
# Elementos que estão nos dois conjuntos
c3 = c1 & c2
c3 = c1.intersection(c2)

print("Intersecção:")
print("C1 =", c1)
print("C2 =", c2)
print("C3 (Resultado) =", c3)

print()

# Diferença (-):
# Elementos diferentes que estão somente no conjunto da esquerda
c3 = c1 - c2
c3 = c1.difference(c2)

print("Diferença:")
print("C1 =", c1)
print("C2 =", c2)
print("C3 (Resultado) =", c3)

print()

# Diferença simétrica (^):
# Elementos diferentes que estão nos dois conjuntos
c3 = c1 ^ c2
c3 = c1.symmetric_difference(c2)

print("Diferença símetrica:")
print("C1 =", c1)
print("C2 =", c2)
print("C3 (Resultado) =", c3)

print()

# Checando se duas listas tem os mesmos elementos, tirando os duplicados:
l1 = ["José", "João", "João", "Maria"]
l2 = ["José", "João", "Maria", "Maria"]

print(l1)
print(l2)

if set(l1) == set(l2):
    print("Listas tem os mesmos elementos")
