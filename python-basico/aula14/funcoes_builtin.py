"""
Aula 14 - Funções built-in úteis

São funções que podem ser acessadas em qualquer programa Python.

As funções isnumeric, isdecimal, isdigit são utilizadas para
verificar se uma string contém apenas valores númericos -
sinais de - ou + e . não são desconsiderados.
"""

import re

num = input("Digite um número: ")

if num.isnumeric():
    print(f"{num} contém apenas números")
else:
    print(f"{num} contém valores não númericos")

# Funções customizadas para checar se um número é int ou float:
# https://github.com/luizomf/check-numbers-python

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)

num = input("Digite um número: ")

print("O valor digitado é um número?", is_number(num))

if is_int(num):
    print(f"{num} é um número decimal")
elif is_float(num):
    print(f"{num} é um número inteiro")

