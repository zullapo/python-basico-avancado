"""
Aula 50 - zip e zip_longest

A função zip junta elementos de listas em tuplas, por exemplo o primeiro
elemento de cada lista irá compor uma tupla e assim sucessivamente até o
ultimo índice da menor lista que foi passada como argumento.

A função zip_longest faz a mesma coisa, porém itera sucessivamente até o
último índice da maior lista e preenche os espaços com um valor padrão.
"""

from itertools import zip_longest, count


nomes_produtos = ["AMD Ryzen 5 5600X", "Nintendo Switch com controle", "Sony WH-1000XM4",
                  "Seagate HD Externo 2TB (STGX2000400)", "Microsoft Surface Dock 2", "Moto G Power"]
precos_produtos = [1077.47, 1450.53, 1688.24, 388.05, 1101.24]
indice = count()

produtos = list(zip(nomes_produtos, precos_produtos))

for nome_produto, preco_produto in produtos:
    print(f"{nome_produto}, R$ {preco_produto}")

print()

produtos = list(zip_longest(nomes_produtos, precos_produtos,
                fillvalue="Produto indisponível"))

for nome_produto, preco_produto in produtos:
    print(f"{nome_produto}, {preco_produto}")

print()

# Usando count para criar o ID dos produtos

# Isso gera um loop infinito, pois a função count é infinita.
# produtos = list(zip_longest(indice, nomes_produtos, precos_produtos, fillvalue="Produto Indisponível"))

produtos = list(zip(indice, nomes_produtos, precos_produtos))

for indice, nome_produto, preco_produto in produtos:
    print(f"{indice}, {nome_produto}, R$ {preco_produto}")
