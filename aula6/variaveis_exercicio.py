"""
Aula 6 - Exercício

Use variáveis para guardar os campos nome, idade, altura, peso,
maioridade e cálculo do IMC através do peso e altura informados.
E imprima as informações na tela.
"""

nome = "José"
idade = 42
altura = 1.80
peso = 80
e_maior = idade >= 18
imc = peso / altura ** 2

print(nome, "tem", idade, "anos de idade e seu IMC é", imc)
