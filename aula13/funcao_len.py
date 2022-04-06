"""
Aula 13 - Função len

Utilizada para retornar a quantidade de elementos de uma sequência - strings, listas...

O valor retornado é um int, para possibilitar a realização de cálculos com o número.
"""

usuario = input("Insira um usuário, mínimo 3 caracteres: ")
senha = input("Insira uma senha, mínimo 8 caracteres: ")

if len(usuario) <= 3:
    print("Informe um usuário com 3 caracteres ou mais.")

if len(senha) <= 8:
    print("Informe uma senha com 8 caracteres ou mais.")
