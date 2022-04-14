"""
Aula 35 - Desafio - Funções

1) Crie uma função com os argumentos saudação e nome, e exiba a mensagem na tela.

2) Crie uma função que receba 3 argumentos com números, e exiba a soma entre eles.

3) Crie uma função que receba 2 números, o primeiro é um valor total e outro é o
percentual. Retorne a soma do valor com o aumento do percentual.

4) Fizz Buzz - Se um parâmetro da função for divísivel por 3, retorne fizz, se
o parâmetro for divisível por 5, retorne buzz. Agora se o parâmetro for divisível
por 5 e 3, retorne FizzBuzz, se não, retorne o número recebido.
"""


def saudacoes(saudacao, nome):
    print(saudacao, nome)


saudacoes("Olá", "João")


def soma(num1, num2, num3):
    print(num1 + num2 + num3)


soma(10, 20, 30)


def aumento(valor_total, taxa_aumento):
    print(valor_total * (taxa_aumento / 100))


aumento(300, 30)


def fizz_buzz(x):
    if x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    elif x % 5 == 0 and x % 3 == 0:
        return "FizzBuzz"
    else:
        return x


print(fizz_buzz(83))
print(fizz_buzz(3))
