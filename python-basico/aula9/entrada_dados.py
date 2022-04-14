"""
Aula 9 - Entrada de dados

Processo de comunicação entre programa e usuário, que permite
o usuário fornecer dados e o programa esperar e ler dados.

Em Python, a função input lê a linha de resposta que o usuário
inseriu no console e retorna o dado em string para o programa.
"""

dado = input("Insira um dado: ")
print(f"O usuário digitou o dado \"{dado}\" e seu tipo é {type(dado)}")

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

# Se preciso fazer algum cálculo com o dado recebido,
# é necessário converter o dado para o tipo apropriado.
# ano_nascimento = 2019 - idade
ano_nascimento = 2019 - int(idade)

print(f"{nome} tem {idade} anos. {nome} nasceu em {ano_nascimento}")

# Outro exemplo comum de operação com dados, calculadora:
numero_1 = input("Digite o primeiro número: ")
numero_2 = input("Digite o segundo número: ")

# Como os dados não foram convertidos para int,
# o resultado será a concatenação das strings.
print(numero_1 + numero_2)

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

print(numero_1 + numero_2)
