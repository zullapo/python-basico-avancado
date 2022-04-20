"""
Aula 36 - Funções Pt. 3

*args: Empacota múltiplos argumentos em uma tupla, sem precisar
de criar todos os argumentos na função.

**kwargs: Lê os argumentos nomeados e armazena a chave e o valor
em um dicionário.
"""


def func(*args):
    print(args)


func(1, 2, 3, 4, 5)

# Argumentos posicionais não podem aparecer na frente de argumentos nomeados:
# def func(*args, nome="Usuário", saudacoes):
#    print(args, nome, saudacoes)
# func(1, 2, 3, 4, 5, nome="Ffs", 1)


def func(*args, nome="Usuário", saudacao="Olá"):
    print(saudacao, nome, args)


func(1, 2, 3, 4, 5)


lista = [1, 2, 3, 4, 5]
# Lista deve ser enviada desempacotada, se não todos os elementos ficarão dentro de uma tupla.
func(lista)
func(*lista)


def func(**kwargs):
    # Checando se é None, ou seja, não foi preenchido:
    if not kwargs.get("idade"):
        print("Idade não foi preenchida.")
    print(kwargs)


func(saudacao="Olá", nome="Usuário", idade=10)
func(saudacao="Olá", nome="Usuário")
