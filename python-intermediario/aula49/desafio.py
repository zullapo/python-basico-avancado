"""
Aula 49 - Desafio - List Comprehension

Dado um carrinho como uma lista que armazena produtos em tuplas,
retorne a soma total dos preços dos produtos.
"""

carrinho = []

carrinho.append(("EXLURA Vestido longo de amarrar nas costas", 195.38))
carrinho.append(("Fitpolo Relógio inteligente", 244.80))
carrinho.append(("SOJOS Óculos de sol polarizados", 97.89))

total = sum([p for _, p in carrinho])

print(total)
