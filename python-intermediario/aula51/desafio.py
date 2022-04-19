"""
Aula 51 - Desafio - Soma de listas

Dada duas listas de inteiros ou floats, retorne a soma de seus elementos
em outra lista.

Exemplo:
li1 = [1, 2, 3, 4, 5, 6, 7]
li2 = [1, 2, 3, 4]

resultado = [2, 4, 6, 8]
"""

li1 = [1, 2, 3, 4, 5, 6, 7]
li2 = [1, 2, 3, 4]

lista_zippeada = list(zip(li1, li2))
soma_listas = [sum(i) for i in lista_zippeada]
# soma_listas = [i + j for i, j in lista_zippeada]

print(soma_listas)
