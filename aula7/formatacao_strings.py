"""
Aula 7 - Formatação de strings

Geralmente, utilizada para concatenar valores com strings.
Existem duas formas de formatação: f-strings e str.format().
"""

nome = "José"
idade = 42
altura = 1.80
peso = 80
e_maior = idade >= 18
imc = peso / altura ** 2

# String sem formatação:
print(nome, "tem", idade, "anos de idade e seu IMC é", imc)

# f-string
# Prefixada pela letra f ou F.
# Permite que valores entre chaves sejam incluídos na string.
print(f"{nome} tem {idade} anos de idade e seu imc é {imc}")
print(F"{nome} tem {idade} anos de idade e seu imc é {imc}")

# str.format()
# Método embutido na string (str).
# Cada chave da string é substituída por cada argumento
# passado para o format(), por ordem de posição.
print("{} tem {} anos de idade e seu imc é {}".format(nome, idade, imc))

# A ordem de posição pode ser mudada sem trocar a posição dos argumentos,
# e um argumento pode ser incluído duas vezes, sem repeti-lo no format.
print("{0} {0} tem {2} anos de idade e seu imc é {1}".format(nome, idade, imc))

# Ao invés de usar posições, argumentos podem receber nomes
print("{n} tem {i} anos de idade e seu imc é {im}".format(n=nome, i=idade, im=imc))

# Limitando o número de casas decimais de um número, usando o format specifier (:)
print(f"{nome} tem {idade} anos de idade e seu imc é {imc:.2f}")
print("{} tem {} anos de idade e seu imc é {:.2f}".format(nome, idade, imc))
