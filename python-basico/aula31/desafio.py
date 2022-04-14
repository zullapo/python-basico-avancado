"""
Aula 31 - Desafio - Validador de CPF

CPF: 168.995.350-09

- 9 primeiros números * números decrescentes de 10 a 2
- 9 primeiros números * números decrescentes de 11 a 2

1 * 10 = 10                                1 * 11 = 11
6 * 9  = 54                                6 * 10 = 60
8 * 8  = 64                                8 * 9  = 72
9 * 7  = 63                                9 * 8  = 72
9 * 6  = 54                                9 * 7  = 63
5 * 5  = 25                                5 * 6  = 30
3 * 4  = 12                                3 * 5  = 15
5 * 3  = 15                                5 * 4  = 20
0 * 2  = 0                                 0 * 3  = 0
                                           0 * 2  = 0
    297                                        343
11 - (297 % 11) = 11                       11 - (343 % 11) = 9
11 > 9 = 0                                 
Digito 1 = 0                               Digito 2 = 9
"""

cpf = input("Insira um CPF válido sem pontuação. Ex.: 16899535009: ")

novo_cpf = cpf

while len(novo_cpf) < 11:
    sequencia = list(range(len(novo_cpf) + 1, 1, -1))
    acumulador = 0
    digito = 0

    for i in range(len(novo_cpf)):
        acumulador += int(novo_cpf[i]) * sequencia[i]
    
    formula = 11 - (acumulador % 11)

    if not formula > 9:
        digito = formula
    
    novo_cpf += str(digito)

    e_sequencia = novo_cpf == novo_cpf[0] * len(cpf)

if novo_cpf == cpf and not e_sequencia:
    print("CPF válido")
else:
    print("CPF inválido")
