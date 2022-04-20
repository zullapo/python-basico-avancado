"""
Aula 53 - Combinations, permutations e product (itertools)

São três funções que trazem o maior número possível de variações
de uma sequência, porém de formas diferentes.

Combinação - ordem de elementos não importa
Permutação - ordem de elementos importa

Ambos não repetem valores

Produto - ordem de elementos importa e repete valores
"""

from itertools import combinations, permutations, product

funcionarios = ["Paulo", "Gaspar", "Alex", "Pedro", "Luiz", "Washington"]

for combinacao in combinations(funcionarios, 2):
    print(combinacao)

print()

for permutacao in permutations(funcionarios):
    print(permutacao)

print()

for produto in product(funcionarios, repeat=2):
    print(produto)
