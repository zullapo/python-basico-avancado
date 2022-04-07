"""
Aula 25 - Split, join, enumerate

O método split serve para separar strings e colocar numa lista,
através de um dado delimitador cujo valor padrão é " ".

O método join junta elementos de uma sequência, concatenando
entre eles uma string.

A função enumerate retorna uma tupla com índice e valor de
elementos de uma sequência.
"""

frase = "você precisa fazer aquilo que pensa que não é capaz de fazer"

palavras = frase.split()

palavra = ""
contagem = 0
for letra in palavras:
    # Toda palavra é contada em relação a toda string.
    qtd_vezes = palavras.count(letra)
    
    # A cada iteração, será checado se a palavra atual foi mais
    # repetida do que a palavra anterior.
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = letra

print(f"{palavra} {contagem}x")

materiais_escolares = ["Lápis", "Caneta", "Borracha"]

print(", ".join(["Lápis", "Caneta", "Borracha"]))

nomes = ["João", "Maria", "José"]

for indice, valor in enumerate(nomes):
    print(indice, valor)

