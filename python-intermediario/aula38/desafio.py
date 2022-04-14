"""
Aula 38 - Desafio - Funções

1) Crie uma função que recebe como argumento uma outra função (callback) e retorne
o valor da função executada.

2) Crie uma função que recebe como argumento uma outra função e argumentos
*args, **kwargs. Assim a função mestre irá imprimir o resultado da função 2
com os argumentos passados.
"""


def aumento(valor, percentual_aumento):
    return valor * por_100(percentual_aumento)


def por_100(num):
    return num / 100


print(aumento(250, 25))


def folha_de_pagamento(funcao, *args):
    return funcao(*args)


def salarios(*cargos):
    resultado = []
    for cargo in cargos:
        if cargo == "Programador":
            resultado.append(f"{cargo}: R${1500:.2f}")
        elif cargo == "Analista de Requisitos":
            resultado.append(f"{cargo}: R${2500:.2f}")
        elif cargo == "Analista de Testes":
            resultado.append(f"{cargo}: R${2000:.2f}")
        else:
            resultado.append(f"Cargo \"{cargo}\" inválido")
    return resultado


dados = folha_de_pagamento(salarios, "Programador", "Analista de Requisitos")
print("\n".join(dados))
