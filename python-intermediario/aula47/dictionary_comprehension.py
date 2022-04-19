"""
Aula 47 - Compreensão de dicionário (Dictionary Comprehension)

Semelhante ao List Comprehension, utiliza for loop e preenche
pares de chave-valor.
"""

pessoas = [
    (1, "andre"),
    (2, "pedro"),
    (3, "jose"),
]

d1 = {k: v.capitalize() for k, v in pessoas}
# d1 = dict(pessoas)
d2 = {k: v for k, v in enumerate(range(5))}
d3 = {x for x in range(5)}  # Isso é um conjunto
d4 = {f"Chave {x}": x * 2 for x in range(5)}

print(d1)
print(d2)
print(d3, type(d3))
print(d4)
