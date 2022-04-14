"""
Aula 37 - Funções Pt. 4

Variáveis locais: são declaradas e acessadas somente em um bloco de código (função, estrutura).

Variáveis globais: são declaradas e acessadas em nível de módulo.
"""

flag = True


def toggle():
    # O valor da variável global não é mudado:
    flag_local = not flag
    return flag_local


print(f"Variável local: {toggle()}")
print(f"Variável global: {flag}")


def toggle():
    # Mudando valor da variável global usando o comando gloabal:
    global flag
    flag = not flag
    return flag


print(f"Variável local: {toggle()}")
print(f"Variável global: {flag}")
