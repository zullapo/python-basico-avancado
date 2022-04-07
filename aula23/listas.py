"""
Aula 23 - Listas

Lista é uma coleção de dados mutável que pode conter valores
de diferentes tipos e pode ser indexada e fatiada como uma string.

Possue métodos/comandos que auxiliam na sua manutenção, entre os principais:
append, insert, del, pop, clear, extend, +.

O objeto range pode ser convertido para uma lista de elementos, através da
função list().

As funções min e max funcionam em coleções, e retornam o maior e menor
elemento de uma lista.
"""

li = ["A", "B", "C", "D", "E"]
print(li)

# Index e fatiamento funciona da mesma forma como nas strings:
print(li[0])
print(li[:3])
print(li[::-1])

# Insere o elemento na posição final da lista:
li.append("F")
print(li)

# Insere o elemento em uma dada posição:
li.insert(0, 10)
print(li)

# O comando del pode deletar a lista, um índice ou parte dela.
li2 = li
del li2
# NameError, pois a lista foi deletada.
# print(li2)

del li[0]
print(li)

del li[4:]
print(li)

# Remove o último elemento da lista:
li.pop()
print(li)

# Esvazia a lista:
li2 = li
li2.clear()
print(li2)
del li2

# Extende uma lista com elementos de outra lista (fusão):
li2 = ["D", "E", "F"]
li.extend(li2)
print(li)

# Somar listas é quase a mesma coisa que extender, porém nenhuma das listas serão modificadas,
# só haverá o resultado da soma.
print(li + li2)
print(li)

# Convertendo o objeto range em uma lista de números:
numeros = list(range(10))
print(numeros)

# Obtendo o maior e menor elemento da lista:
print(min(numeros))
print(max(numeros))
