"""
Aula 16 - Desafio - Estruturas Condicionais

1) Faça um programa para checar se o valor digitado é um número,
se for um número, informe se é par ou ímpar. Se não for um número,
informe que não é um número válido.

2) Faça um programa que pergunte a hora atual (valor inteiro),
e exiba a saudação correspondente ao horário informado, ex.:
Bom dia (00:00 - 11:00), Boa tarde (12:00 - 17:00) e Boa noite (18:00 - 23:00).

3) Faça um programa que pergunte o primeiro nome do usuário,
e conforme o tamanho do nome, informe se é curto (4 letras),
médio (entre 5 a 6) e longo (maior que 6).
"""

# Primeiro exercício
num = input("Insira um número: ")

if num.isnumeric():
    num = int(num)
    if num % 2 == 0:
        print("Par")
    else:
        print("Impár")
else:
    print(f"{num} não é um número válido.")

# Segundo exercício
hora = input("Insira a hora atual: ")

if hora.isnumeric():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida.")
else:
    print("Informe hora em valor inteiro. Ex.: 17")

# Terceiro exercício:
nome = input("Insira seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome <= 4:
    print(f"{nome} tem {tamanho_nome} caracteres e é um nome de tamanho curto")
elif tamanho_nome <= 6:
    print(f"{nome} tem {tamanho_nome} caracteres e é um nome de tamanho médio")
else:
    print(f"{nome} tem {tamanho_nome} caracteres e é um nome de tamanho longo")
