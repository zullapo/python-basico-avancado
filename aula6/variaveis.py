"""
Aula 6 - Variável

É um dado nome que referencia um valor. É nomeado variável, pois
seu valor pode ser posteriormente mudado em outras partes do programa.

O nome de uma varíavel deve começar com letras, pode conter números,
é preferível ter letras minúsculas e se for nome composto,
ter palavras separadas por _. Ex.: minha_variavel.

O tipo de uma varíavel é inferido pelo seu valor, isto é
uma das principais características de uma linguagem dinamicamente tipada.
"""

# Observe que uma variável pode referenciar outro valor e também outro tipo de valor.
variavel = "oi"
print("variavel =", variavel, type(variavel))
variavel = 10
print("variavel =", variavel, type(variavel))

nome = "José"
idade = 42
peso = 80
altura = 1.80
e_maior = idade >= 18

print("Nome:", nome)
print("Idade:", idade)
print("Altura:", altura)
print("É maior de idade?", e_maior)
