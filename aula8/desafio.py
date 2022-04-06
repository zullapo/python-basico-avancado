"""
Aula 8 - Desafio

* Criar variáveis com nome (str), idade (int), altura (float), peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (int)
* Obter o IMC da pessoa (2 casas decimais)
* Exibir o texto com as informações usando f-strings
"""

nome = "José"
idade = 42
altura = 1.80
peso = 80.5
ano_atual = 2022
ano_nascimento = ano_atual - idade
imc = peso / altura ** 2

print(f"{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.")
print(f"O IMC de Luiz é {imc:.2f}.")
print(f"{nome} nasceu em {ano_nascimento}")
