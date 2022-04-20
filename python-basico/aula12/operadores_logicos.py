"""
Aula 12 - Operadores lógicos

Junta duas condições ou mais, para que sejam testadas mutualmente ou exclusivamente.

and - E - todas condições devem ser verdadeiras, será retornado True. 
or - OU - se uma das condições for verdadeira, será retornado False.
not - Negação - inverte o valor de uma expressão booleana,
o que seria retornado True passa a ser False (vice-versa).
"""

num = int(input("Insira um número: "))

print("O número é maior que 0 e menor que 100?", num > 0 and num < 100)
print("O número é menor que 0 ou igual a 2?", num < 0 or num < 2)
print("O número é maior que 0? (not)", not num < 0)

# Exemplos de operadores lógicos + if/elif/else:

altura = float(input("Insira sua altura: "))
peso = float(input("Insira seu peso: "))

if altura >= 1.40 and peso <= 120:
    print("Você pode entrar em qualquer atração radical")
elif altura <= 1.40 and peso < 120:
    print("Altura mínima permitida: 1.40m")
elif altura >= 1.40 and peso > 120:
    print("Peso mínimo permitido: 120kg")

x = float(input("Insira um ângulo x: "))

if x >= 0 and x <= 90:
    print("Primeiro quadrante")
elif x >= 90 and x <= 180:
    print("Segundo quadrante")
elif x >= 180 and x <= 270:
    print("Terceiro quadrante")
elif x >= 270 and x <= 360:
    print("Quarto quadrante")
