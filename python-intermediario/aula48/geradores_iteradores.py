"""
Aula 48 - Geradores, Iteradores e Iteráveis

Um iterador é definido pela classe Iterator, possuindo métodos como:
__iter__: retorna objeto iterador para uso em for e outros.

__next__: retorna o próximo valor da iteração até que não tenha
mais nenhuma e lance o erro StopIteration.

Um objeto iterável é aquele que retorna um iterador, ex.: função
range e coleções como lista, string...

Gerador é uma forma simples de criar iteradores, a partir do
comando yield - retorna valor como return, porém controla o
estado do valor e quando for preciso executar a função que
chama o yield novamente, o valor será retornado onde foi
parado.
"""

import sys
import time

lista = [1, 2, 3]
string = "".join([str(i) for i in lista])

# Verifica se objetos são iteráveis:
print("Lista __iter__?", hasattr(lista, "__iter__"))
print("String __iter__?", hasattr(string, "__iter__"))

for i in lista:  # Transforma lista em iterador
    print(i)

print("Lista __next__?", hasattr(lista, "__next__"))
print("String __next__?", hasattr(string, "__next__"))

# O for chama a lista com a função iter, assim ela passa a ser um iterador:
lista = iter(lista)

print("Lista __next__?", hasattr(lista, "__next__"))

print(next(lista))
print(next(lista))
print(next(lista))


# Função normal:
# def preenche_lista():
#     # Preenche toda lista e só depois retorna o valor
#     r = []
#     for i in range(100):
#         r.append(i)
#         time.sleep(0.1)  # Simulando operação lenta
#     return r


# pl = preenche_lista()

# print(pl)


# Função geradora:
def gera():
    # Retorna um valor de cada vez, mantendo o estado
    for n in range(100):
        yield n
        time.sleep(0.1)


# pl = preenche_lista()
g = gera()

for i in g:  # É preciso criar um for, pois a função retorna um objeto gerador
    print(i, end=" ")

print()


def gera2():
    # Retorna um valor por vez em sequência, esse é o controle de estado
    yield "1"
    yield "2"
    yield "3"


g2 = gera2()

print(next(g2))
print(next(g2))
print(next(g2))

# Diferença de uma lista e um gerador na memória:
lista = [x for x in range(100)]
print(f"Tamanho: {sys.getsizeof(lista)}, Tipo: {type(lista)}")
# Essa é uma forma mais fácil de criar geradores, generator expressions:
gerador = (x for x in range(100))
print(f"Tamanho: {sys.getsizeof(gerador)}, Tipo: {type(gerador)}")

# Se a lista mudar de tamanho irá consumir mais bytes, o gerador não.
# Pois o gerador só gera os elementos necessários por vez, ao invés de alocar todos de uma vez
lista = [x for x in range(10000)]
print(f"Tamanho: {sys.getsizeof(lista)}, Tipo: {type(lista)}")
gerador = (x for x in range(10000))
print(f"Tamanho: {sys.getsizeof(gerador)}, Tipo: {type(gerador)}")
