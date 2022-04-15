"""
Aula 40 - Tuplas

Coleção de dados que possue quase todos os atributos de uma lista,
porém é imutável e declarada entre parênteses ou apenas vírgula.
"""

t1 = ("A", 1, "B", 2, "C", 3)
t2 = "D", 4, "E", 5, "F", 6

print(t1)
print(t2)

# Operações com tupla:

# Adição:
t3 = t1 + t2
print(t3)

# Repetição
t4 = t1 * 3
print(t4)

# TypeError, pois tuplas são imutáveis, ou seja, o valor de seus índices não pode mudar.
# t2[-1] = 7
