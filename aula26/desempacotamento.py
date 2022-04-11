"""
Aula 26 - Desempacotamento de listas

Operação que consiste em armazenar valores de elementos iteráveis
varíaveis, assim cada índice corresponderá um elemento.
"""

a, b, c = [1, 2, 3]
print(a, b, c)

# O operador * serve para referenciar outra lista com o restante dos elementos.
a, b, c, *restante = [1, 2, 3, 4, 5, 6, 7]
print(restante)

# Se for desempacotado outro valor após o *, terá o ultimo valor.
a, b, c, *restante, ultimo = [1, 2, 3, 4, 5, 6, 7, 8]
print(ultimo)
