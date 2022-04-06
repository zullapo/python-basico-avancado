"""
Aula 11 - Operadores Relacionais

Comparam valores, retornando verdadeiro se os valores forem iguais, senão falso.

== - igual a
> - maior que
>= - maior ou igual a
< - menor que
<= - menor ou igual a
!= - diferente de
"""

num = int(input("Insira um número: "))

print("Número é igual a 10?", num == 10)
print("Número é maior que 5?", num > 5)
print("Número é maior ou igual a?", num >= 0)
print("Numero é menor que 0?", num < 0)
print("Número é menor ou igual a 2?", num <= 2)
print("Número é diferente de 4?", num != 4)

# Exemplos de operadores relacionais + if/elif/else:

num = int(input("Insira um número: "))

if num > 0:
    print("Positivo")
elif num == 0:
    print("Zero")
else:
    print("Negativo")
