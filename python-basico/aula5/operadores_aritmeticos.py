"""
Aula 5 - Operadores arítmeticos

Performam as operações matemáticas como adição, subtração, multiplicação e divisão.

+  |  adição
-  |  subtração
*  |  multiplicação
/  |  divisão - resultado sempre é um número float.
** |  potenciação
// |  divisão inteira - se ambos números forem inteiros, o resultado será int.
%  |  módulo - resultado é o resto da divisão.
() |  parênteses - indica qual cálculo terá precêndencia.

Ordem de operações aritméticas

1. Parênteses
2. Potência
3. Multiplicação, divisão, divisão inteira e módulo
4. Soma e subtração
"""

print(5 + 8)
print(0 - 250)
print(9 * 9)
print(8 / 2)

print(2 ** 63 - 1)

print(10 // 4)
print(5.0 // 2)

print(6 % 2)
print(2.0 % 3)  # Se um dos números for float, o resultado será float.

print((5 + 5) * 10)

# O + também tem papel de concatenação de strings
print("A " + "vida " + "não é " + "fácil.")

# Não é possível concatenar uma string com um número, pois Python é uma
# linguagem fortemente tipada.
# print(2 + "B")

# O * também tem papel de repetição de strings
print(3 * "HA")
