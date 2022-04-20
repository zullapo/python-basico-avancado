"""
Aula 52 - Contador (counter)

A biblioteca itertools traz um conjunto de ferramentas sobre iteração de valores,
uma dessas ferramentas é a função counter.

O counter é um contador infinito que pode receber dois argumentos opcionais: ponto
de partida (start) e step para definir quantos números serão pulados.
"""

from itertools import count

contador = count()

# O count é um iterador
print(hasattr(contador, "__iter__") and hasattr(contador, "__next__"))

# O contador é infinito, logo o for loop também é:
for valor in contador:
    print(valor)

    if valor >= 10:  # Definindo um ponto de parada para o for
        break

print()

# O step pode ser um decimal, mesmo que espere inteiros
contador = count(start=5, step=0.1)

for valor in contador:
    # Arrendondando para obter a precisão de duas casas decimais
    print(round(valor, 2))

    if valor >= 10:
        break

print()

contador = count(start=9, step=-1)

for valor in contador:
    print(valor)

    if valor <= 0:
        break

print()

contador = count()

# O contador corresponde a cada item da lista sucessivamente
produtos = ["Meta Quest 2", "Seagate HD Externo 4TB", "Iphone XR 4G LTE"]
produtos = zip(contador, produtos)

print(list(produtos))
