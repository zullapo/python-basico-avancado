"""
Aula 4 - Tipos de dados

Cada valor tem seu tipo, e cada tipo descreve a funcionalidade de cada valor.

Tipos de dados principais

str - string - textos
int - inteiro - números inteiros
float - real -  números decimais
bool - booleano - True (verdadeiro) ou False (falso)

Em Python, tipos são classes e valores são instâncias de tipos (objetos).
"""

# Para checar o tipo de dado de um valor, é utilizado a função type:
print("Nome", type("Nome"))

print("Olá", type("Olá"))
print(3, type(3))
print(6.5, type(6.5))
print(True, type(True))

# O == é utilizado para comparação de valores e retorna booleano.
print("a" == "A", type("a" == "A"))

# Conversão de tipo (type casting):

# str -> int (vice-versa):
print(int("1"), type(int("1")))
print(str(1), type(str(1)))

# int -> float (vice-versa):
print(3, float(3), type(float(3)))
print(9.999, int(9.999), type(int(9.999)))

# bool
# Os números 0 e 1 correspondem True e False.
print(bool(0), type(bool(0)))
print(bool(1), type(bool(1)))

# Objetos como strings, listas, tuplas e dicionários quando vazios e convertidos para boolean,
# passam a ser False.
print(bool(""), type(bool("")))
print(bool([]), type(bool([])))

# Se invertida a lógica, passam a ser True.
print(bool("0"), type(bool("0")))
print(bool([1, 2, 3]), type(bool([1, 2, 3])))
