"""
Aula 46 - Desafio - List Comprehension

A partir de uma string que repete os digitos (0123456789) consecutivas vezes,
faça-a com que fique nesse formato:

0123456789.0123456789.0123456789.0123456789.0123456789
"""

string = "01234567890123456789012345678901234567890123456789"

string_final = ".".join([string[i: i + 10] for i in range(0, len(string), 10)])

# string_final = "".join([string[i] + "." if string[i] == "9" and i !=
#                        len(string) - 1 else string[i] for i in range(len(string))])

print(string_final)
