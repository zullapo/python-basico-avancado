"""
Aula 29 - Expressões condicionais com OR

Geralmente, utilizado para substituir um valor ausente com outro valor,
sem precisar de utilizar if/else.
"""

rua = input("Insira a rua: ")
quadra = input("Insira a quadra: ")
numero = input("Insira o número: ")
lote = input("Insira o lote: ")
complemento = input("Insira o complemento: ")

print(f"Rua: {rua or 'S/R'}")
print(f"Quadra: {quadra or 'S/Q'}")
print(f"Número: {numero or 'S/N'}")
print(f"Lote: {lote or 'S/L'}")
print(f"Complemento: {complemento or 'S/C'}")
