"""
Aula 3 - Strings

Tipo de dado (str) que representa um conjunto de caracteres separados por aspas simples ou duplas.
"""

# A mesma informação será exibida na tela, independente do tipo de aspas:
print("Isso é uma string (str).")
print('Isso é uma string (str).')

# Ao executar o comando abaixo, o erro SyntaxError será retornado,
# pois as aspas duplas do texto entram em conflito com as aspas duplas da string.
# print("Isso é uma "string" (str).")

# Declarando a string com aspas simples e inserindo aspas duplas no texto (vice-versa),
# é uma maneira de resolver esse problema:
print("Isso é uma 'string' (str).")
print('Isso é uma "string" (str).')

# O caractere de escape (\) é utilizado para escapar aspas e outros caracteres:
print("Isso é uma \"string\" (str).")
print("Isso é uma \'string\' (str).")
print("Isso é uma \n string (str).")

# As raw strings são prefixadas pela letra r ou R, e servem para escapar barras invertidas no texto.
print(r"Isso é uma \n string")
print(r"Caminho de um arquivo: C:\Users\User\Desktop\data.txt")
