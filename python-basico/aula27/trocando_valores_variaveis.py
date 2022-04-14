"""
Aula 27 - Trocando valores entre variáveis

Em Python, há uma maneira mais simples de trocar valores entre variáveis
do que outras linguagens.
"""

# Forma convencional: criando variável temporária para armazenar valor
x = 1
y = -1

z = x
x = y
y = z

print(f"X = {x}, Y = {y}")

# Em Python:
x = 1
y = -1

x, y = y, x
# x, y = -1, 1

print(f"X = {x}, Y = {y}")
