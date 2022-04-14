"""
Aula 34 - Funções Pt. 2

O comando return serve para retorna um valor ao executar uma função.
"""


def factorial(x):
    if x == 1:
        return 1  # Nada será executado abaixo, se esse return for executado.
    # Recursão é o processo de re-executar uma função dentro de outra.
    return x * factorial(x - 1)


var = factorial(9)  # O valor retornado pode ser armazenado numa variável
print(var)
print(factorial(1))  # ou ser passado como argumento para outra função.


def func(arg):
    print(arg + arg)


var = func(10)
print(var)  # Se não houver um return, o None será retornado por padrão.


def func_a(arg):
    print(arg)


def func_b():
    return func_a  # Uma função pode retornar outra função


# Essa variável passa a referenciar a função "func_a", ao executar a "func_b".
var = func_b()
var("Olá!")
# O parênteses é colocado duas vezes, pois uma função retorna outra em seguida.
func_b()("Bom dia!")
