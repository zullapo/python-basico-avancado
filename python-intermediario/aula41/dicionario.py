"""
Aula 41 - Dicionário

Coleção de dados que armazena dados no formato chave-valor,
onde as chaves não podem ser duplicadas.

Se uma chave for duplicada, ela terá seu valor sobreescrito
pelo último valor atribuído a ela.

Os "índices" seriam as chaves, para acessar um valor, devemos
acessar a chave.
"""

import copy

d1 = {"A": 1, "B": 2, "C": 3}
d2 = dict(A=1, B=2, C=3)
d3 = {"A": [1, 2, 3], "B": (1, 2, 3), "C": "4", "D": False}

print(d1)
print(d2)
print(d3)

print()

# Atribuição dinâmica de chaves:
d1["D"] = 4

# Verificando se chave existe:
if "D" in d1:
    print(d1["D"])

print()

# Atualizando chaves (duplicando):
d1["D"] = 5
print(d1)

d1.update({"D": 9})
d1.update({"E": 10})  # Também pode adicionar, se não existir
print(d1)

d4 = {"E": ..., "F": None}
d3.update(d4)  # Concatenação/atualização entre dicionários
print(d3)

print()

# Removendo chaves:

# Pela chave:
print(d3.pop("E"))  # Quando remove a chave, retorna o valor removido

# Última chave:
print(d3.popitem())  # Retorna chave e valor removido em formato de tupla

print()

# Iterando sobre dicionário:

# Listando chaves do dicionário:
for k in d1:
    print(k)

print()

for k in d1.keys():
    print(k)

print()

# Listando valores do dicionário:
for k in d1:
    print(d1[k])

print()

for v in d1.values():
    print(v)

print()

# Listando chaves e valores do dicionário (itens):
for k, v in d1.items():
    print(k, v)

print()

# Dicionários aninhados:
produtos = {
    "P1": {
        "nome": "Farinha de Trigo Tipo 1 pacote 1kg - Primor",
        "preco": 4.59,
    },
    "P2": {
        "nome": "Energético lata 473ml - Monster Energy",
        "preco": 7.48,
    },
    "P3": {
        "nome": "Detergente Líquido Limão frasco 500ml - Ypê",
        "preco": 2.17
    }
}

# Iterando sobre dicionários aninhados:
for produtos_k, produtos_v in produtos.items():
    print(f"Produto {produtos_k}")
    for produto_k, produto_v in produtos_v.items():
        print(f"{produto_k.capitalize()}: {produto_v}")
    print()

# Importância de copiar dicionários:
print("d2:", d2)

d2c = d2  # Aponta para referência de d2
d2c["A"] = 4  # Muda não só o d2c, mas também o d2

print("d2c:", d2c)
print("d2:", d2)

d2c = d2.copy()  # Armazena a cópia
d2c["A"] = 3  # Muda apenas o d2c

print("d2c:", d2c)
print("d2:", d2)

print()

# Problema com o .copy():
d2["E"] = [1, 2, 3]
print("d2:", d2)

d2c = d2.copy()  # Esse método produz um shallow copy e copia apenas a referência dos objetos dentro
d2c["E"][0] = 0  # Muda o d2c e d2

print("d2c:", d2c)
print("d2:", d2)

d2c = copy.deepcopy(d2)  # O deep copy copia os objetos dentro
d2c["E"][0] = -1  # Muda só o d2c

print("d2c:", d2c)
print("d2:", d2)

print()

# Convertendo lista multidimensional em dicionário:
tabela_pontos = [
    ["P1", 35],
    ["P2", 33],
    ["P3", 30],
    ["P4", 27]
]

print(tabela_pontos, type(tabela_pontos))

tabela_pontos = dict(tabela_pontos)

print(tabela_pontos, type(tabela_pontos))
