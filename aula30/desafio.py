"""
Aula 30 - Desafio - Contadores com for/while

Utilizando as estruturas for ou while, imprima os números a cada interação do loop:

0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

print("While")

i = 0
j = 10
k = 0

while k < 9:
    print(i, j)
    i += 1
    j -= 1
    k += 1

print("\nFor")

i = 0
j = 10

for k in range(9):
    print(i, j)
    i += 1
    j -= 1

print("\nEnumerate")

for i, j in enumerate(range(10, 1, -1)):
    print(i, j)
