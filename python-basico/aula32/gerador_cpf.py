"""
Aula 32 - Gerador de CPF

- Gere um número com 9 dígitos válidos para um CPF.
- Use o método de validar CPF, para gerar os dois últimos dígitos.
"""

import random

numero = str(random.randint(100000000, 999999999))

novo_cpf = numero

while len(novo_cpf) < 11:
    sequencia = list(range(len(novo_cpf) + 1, 1, -1))
    total = 0
    digito = 0

    for i in range(len(novo_cpf)):
        total += int(novo_cpf[i]) * sequencia[i]

    formula = 11 - (total % 11)

    if not formula > 9:
        digito = formula

    novo_cpf += str(digito)

print(novo_cpf)
